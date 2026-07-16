/**
 * Accessible screenshot lightbox with near-fullscreen fit and zoom/pan.
 * Usage: PortfolioLightbox.registerGallery(id, items); figures use
 * data-lightbox-open + data-lightbox-gallery + data-lightbox-index.
 */
(function (global) {
  const galleries = new Map();
  const MIN_ZOOM = 0.25;
  const MAX_ZOOM = 4;
  let state = null;
  let modal = null;
  let scrollY = 0;
  let zoomMode = 'fit'; // 'fit' | 'custom'
  let zoomScale = 1; // fraction of natural width when custom
  let drag = null;

  function registerGallery(id, items) {
    if (!id || !items || !items.length) return;
    galleries.set(id, items.map((item) => ({
      src: item.src,
      caption: item.caption || '',
      alt: item.alt || item.caption || 'Screenshot'
    })));
  }

  function clamp(n, min, max) {
    return Math.min(max, Math.max(min, n));
  }

  function ensureModal() {
    if (modal) return modal;

    modal = document.createElement('div');
    modal.id = 'lightbox';
    modal.className = 'lightbox';
    modal.hidden = true;
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Screenshot gallery');
    modal.innerHTML = `
      <div class="lightbox-backdrop" data-lightbox-close tabindex="-1"></div>
      <div class="lightbox-panel" role="document">
        <div class="lightbox-toolbar">
          <div class="lightbox-zoom-controls" role="group" aria-label="Zoom controls">
            <button type="button" class="lightbox-zoom-out" aria-label="Zoom out">−</button>
            <button type="button" class="lightbox-zoom-reset" aria-label="Toggle fit and actual size">Fit</button>
            <button type="button" class="lightbox-zoom-in" aria-label="Zoom in">+</button>
          </div>
          <button type="button" class="lightbox-close" aria-label="Close screenshot viewer">&times;</button>
        </div>
        <button type="button" class="lightbox-nav lightbox-prev" aria-label="Previous screenshot">&#8249;</button>
        <button type="button" class="lightbox-nav lightbox-next" aria-label="Next screenshot">&#8250;</button>
        <div class="lightbox-stage">
          <img class="lightbox-image" alt="" draggable="false" />
        </div>
        <div class="lightbox-meta">
          <p class="lightbox-caption" id="lightbox-caption"></p>
          <p class="lightbox-counter" aria-live="polite"></p>
        </div>
      </div>
    `;
    document.body.appendChild(modal);

    modal.querySelector('.lightbox-close').addEventListener('click', close);
    modal.querySelector('.lightbox-prev').addEventListener('click', () => step(-1));
    modal.querySelector('.lightbox-next').addEventListener('click', () => step(1));
    modal.querySelector('.lightbox-zoom-in').addEventListener('click', () => adjustZoom(1.25));
    modal.querySelector('.lightbox-zoom-out').addEventListener('click', () => adjustZoom(0.8));
    modal.querySelector('.lightbox-zoom-reset').addEventListener('click', toggleFitActual);
    modal.querySelector('[data-lightbox-close]').addEventListener('click', close);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) close();
    });

    const stage = modal.querySelector('.lightbox-stage');
    const img = modal.querySelector('.lightbox-image');

    img.addEventListener('load', () => {
      if (!state) return;
      applyZoom();
    });

    img.addEventListener('dblclick', (e) => {
      e.preventDefault();
      toggleFitActual();
    });

    img.addEventListener('click', (e) => {
      // Single click toggles fit ↔ 1:1 when not dragging
      if (drag && drag.moved) return;
      e.stopPropagation();
      toggleFitActual();
    });

    stage.addEventListener('wheel', onWheel, { passive: false });

    stage.addEventListener('pointerdown', (e) => {
      if (zoomMode !== 'custom') return;
      if (e.button !== 0) return;
      drag = {
        pointerId: e.pointerId,
        x: e.clientX,
        y: e.clientY,
        left: stage.scrollLeft,
        top: stage.scrollTop,
        moved: false
      };
      stage.classList.add('lightbox-stage--panning');
      try {
        stage.setPointerCapture(e.pointerId);
      } catch (_) {
        /* ignore */
      }
    });

    stage.addEventListener('pointermove', (e) => {
      if (!drag || drag.pointerId !== e.pointerId) return;
      const dx = e.clientX - drag.x;
      const dy = e.clientY - drag.y;
      if (Math.abs(dx) > 3 || Math.abs(dy) > 3) drag.moved = true;
      stage.scrollLeft = drag.left - dx;
      stage.scrollTop = drag.top - dy;
    });

    const endDrag = (e) => {
      if (!drag || (e && drag.pointerId !== e.pointerId)) return;
      const wasMoved = drag.moved;
      drag = null;
      stage.classList.remove('lightbox-stage--panning');
      // Preserve moved flag briefly so click handler can ignore
      if (wasMoved) {
        stage.dataset.suppressClick = '1';
        setTimeout(() => { delete stage.dataset.suppressClick; }, 0);
      }
    };
    stage.addEventListener('pointerup', endDrag);
    stage.addEventListener('pointercancel', endDrag);

    return modal;
  }

  function focusableElements() {
    if (!modal) return [];
    return Array.from(
      modal.querySelectorAll('button:not([hidden]), [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
    ).filter((el) => !el.disabled && el.getAttribute('aria-hidden') !== 'true');
  }

  function lockScroll() {
    scrollY = window.scrollY || window.pageYOffset || 0;
    document.documentElement.classList.add('lightbox-open');
    document.body.classList.add('lightbox-open');
    document.body.style.top = `-${scrollY}px`;
  }

  function unlockScroll() {
    document.documentElement.classList.remove('lightbox-open');
    document.body.classList.remove('lightbox-open');
    document.body.style.top = '';
    window.scrollTo(0, scrollY);
  }

  function fitScale() {
    const img = modal.querySelector('.lightbox-image');
    const stage = modal.querySelector('.lightbox-stage');
    if (!img.naturalWidth || !img.naturalHeight) return 1;
    const sw = stage.clientWidth;
    const sh = stage.clientHeight;
    if (!sw || !sh) return 1;
    return Math.min(sw / img.naturalWidth, sh / img.naturalHeight, 1);
  }

  function updateZoomLabel() {
    const btn = modal.querySelector('.lightbox-zoom-reset');
    if (!btn) return;
    if (zoomMode === 'fit') {
      btn.textContent = 'Fit';
      btn.setAttribute('aria-label', 'Switch to actual size');
    } else if (Math.abs(zoomScale - 1) < 0.03) {
      btn.textContent = '1:1';
      btn.setAttribute('aria-label', 'Switch to fit screen');
    } else {
      btn.textContent = `${Math.round(zoomScale * 100)}%`;
      btn.setAttribute('aria-label', 'Reset to fit screen');
    }
  }

  function applyZoom() {
    if (!modal) return;
    const img = modal.querySelector('.lightbox-image');
    const stage = modal.querySelector('.lightbox-stage');
    if (!img) return;

    if (zoomMode === 'fit') {
      img.style.width = '';
      img.style.height = '';
      img.style.maxWidth = '100%';
      img.style.maxHeight = '100%';
      img.classList.remove('lightbox-image--zoomed');
      stage.classList.remove('lightbox-stage--zoomed');
      stage.scrollLeft = 0;
      stage.scrollTop = 0;
    } else {
      const w = Math.max(1, Math.round(img.naturalWidth * zoomScale));
      img.style.maxWidth = 'none';
      img.style.maxHeight = 'none';
      img.style.width = `${w}px`;
      img.style.height = 'auto';
      img.classList.add('lightbox-image--zoomed');
      stage.classList.add('lightbox-stage--zoomed');
    }
    updateZoomLabel();
  }

  function resetFit() {
    zoomMode = 'fit';
    zoomScale = 1;
    applyZoom();
  }

  function setActualSize() {
    zoomMode = 'custom';
    zoomScale = 1;
    applyZoom();
  }

  function toggleFitActual() {
    if (modal?.querySelector('.lightbox-stage')?.dataset.suppressClick) return;
    if (zoomMode === 'fit') {
      setActualSize();
    } else if (Math.abs(zoomScale - 1) < 0.03) {
      resetFit();
    } else {
      resetFit();
    }
  }

  function ensureCustomFromFit() {
    if (zoomMode === 'fit') {
      zoomMode = 'custom';
      zoomScale = fitScale() || 1;
    }
  }

  function adjustZoom(factor) {
    ensureCustomFromFit();
    zoomScale = clamp(zoomScale * factor, MIN_ZOOM, MAX_ZOOM);
    // If zoomed back near fit size, snap to fit for clarity
    const fit = fitScale();
    if (zoomScale <= fit * 1.02) {
      resetFit();
      return;
    }
    applyZoom();
  }

  function onWheel(e) {
    if (!state) return;
    e.preventDefault();
    adjustZoom(e.deltaY > 0 ? 0.9 : 1.12);
  }

  function render() {
    if (!state || !modal) return;
    const items = galleries.get(state.galleryId) || [];
    const item = items[state.index];
    if (!item) return;

    resetFit();

    const img = modal.querySelector('.lightbox-image');
    img.src = item.src;
    img.alt = item.alt;

    modal.querySelector('.lightbox-caption').textContent = item.caption || item.alt;
    modal.querySelector('.lightbox-counter').textContent =
      items.length > 1 ? `${state.index + 1} / ${items.length}` : '';

    const multi = items.length > 1;
    modal.querySelector('.lightbox-prev').hidden = !multi;
    modal.querySelector('.lightbox-next').hidden = !multi;
    modal.setAttribute('aria-labelledby', 'lightbox-caption');
  }

  function open(galleryId, index, trigger) {
    const items = galleries.get(galleryId);
    if (!items || !items.length) return;

    ensureModal();
    const i = Number(index) || 0;
    state = {
      galleryId,
      index: ((i % items.length) + items.length) % items.length,
      trigger: trigger || null
    };
    lockScroll();
    modal.hidden = false;
    render();
    modal.querySelector('.lightbox-close').focus();
  }

  function close() {
    if (!state) return;
    const trigger = state.trigger;
    state = null;
    drag = null;
    resetFit();
    if (modal) {
      modal.hidden = true;
      const img = modal.querySelector('.lightbox-image');
      if (img) img.removeAttribute('src');
    }
    unlockScroll();
    if (trigger && typeof trigger.focus === 'function') {
      try {
        trigger.focus();
      } catch (_) {
        /* ignore */
      }
    }
  }

  function step(delta) {
    if (!state) return;
    const items = galleries.get(state.galleryId) || [];
    if (items.length < 2) return;
    state.index = (state.index + delta + items.length) % items.length;
    render();
  }

  function onKeydown(e) {
    if (!state) return;
    if (e.key === 'Escape') {
      e.preventDefault();
      close();
      return;
    }
    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      step(-1);
      return;
    }
    if (e.key === 'ArrowRight') {
      e.preventDefault();
      step(1);
      return;
    }
    if (e.key === '+' || e.key === '=') {
      e.preventDefault();
      adjustZoom(1.25);
      return;
    }
    if (e.key === '-' || e.key === '_') {
      e.preventDefault();
      adjustZoom(0.8);
      return;
    }
    if (e.key === '0') {
      e.preventDefault();
      resetFit();
      return;
    }
    if (e.key === '1') {
      e.preventDefault();
      setActualSize();
      return;
    }
    if (e.key === 'Tab') {
      const nodes = focusableElements();
      if (!nodes.length) return;
      const first = nodes[0];
      const last = nodes[nodes.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  }

  function onDelegatedClick(e) {
    const btn = e.target.closest('[data-lightbox-open]');
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();
    open(btn.getAttribute('data-lightbox-gallery'), btn.getAttribute('data-lightbox-index'), btn);
  }

  function init() {
    ensureModal();
    document.addEventListener('keydown', onKeydown);
    document.addEventListener('click', onDelegatedClick);
  }

  global.PortfolioLightbox = {
    registerGallery,
    open,
    close,
    init
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})(window);
