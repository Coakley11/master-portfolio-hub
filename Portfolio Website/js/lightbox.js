/**
 * Accessible screenshot lightbox for portfolio galleries.
 * Usage: PortfolioLightbox.registerGallery(id, items); figures use
 * data-lightbox-open + data-lightbox-gallery + data-lightbox-index.
 */
(function (global) {
  const galleries = new Map();
  let state = null;
  let modal = null;
  let scrollY = 0;

  function registerGallery(id, items) {
    if (!id || !items || !items.length) return;
    galleries.set(id, items.map((item) => ({
      src: item.src,
      caption: item.caption || '',
      alt: item.alt || item.caption || 'Screenshot'
    })));
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
        <button type="button" class="lightbox-close" aria-label="Close screenshot viewer">&times;</button>
        <button type="button" class="lightbox-nav lightbox-prev" aria-label="Previous screenshot">&#8249;</button>
        <div class="lightbox-stage">
          <img class="lightbox-image" alt="" />
        </div>
        <button type="button" class="lightbox-nav lightbox-next" aria-label="Next screenshot">&#8250;</button>
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
    modal.querySelector('[data-lightbox-close]').addEventListener('click', close);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) close();
    });

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

  function render() {
    if (!state || !modal) return;
    const items = galleries.get(state.galleryId) || [];
    const item = items[state.index];
    if (!item) return;

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
