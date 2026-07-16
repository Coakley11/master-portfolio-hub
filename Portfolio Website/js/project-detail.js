const DATA_PATH = 'data/projects.json';

function humanizeScreenshotName(filename) {
  const stem = (filename || '').replace(/\.png$/i, '');
  return stem
    .replace(/^\d+-/, '')
    .replace(/[-_]+/g, ' ')
    .replace(/\b\w/g, (c) => c.toUpperCase());
}

function escapeAttr(value) {
  return String(value || '')
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function galleryItemsFromShots(shots, title) {
  return (shots || []).map((src) => {
    const fname = src.split('/').pop() || 'screenshot.png';
    const caption = humanizeScreenshotName(fname);
    return {
      src,
      caption,
      alt: `${title} — ${caption}`
    };
  });
}

function screenshotImg(src, alt, galleryId, index) {
  const fname = src.split('/').pop() || 'screenshot.png';
  const caption = humanizeScreenshotName(fname);
  return `
    <figure class="screenshot-figure">
      <button type="button" class="screenshot-trigger"
        data-lightbox-open data-lightbox-gallery="${escapeAttr(galleryId)}" data-lightbox-index="${Number(index) || 0}"
        aria-label="Enlarge screenshot: ${escapeAttr(caption)}">
        <img src="${src}" alt="${escapeAttr(alt)} — ${escapeAttr(caption)}" class="screenshot-img" loading="lazy"
          onerror="this.classList.add('screenshot-img--missing');this.nextElementSibling?.classList.add('screenshot-missing--show')">
        <span class="screenshot-missing">Add file: <code>${escapeAttr(fname)}</code></span>
        <span class="screenshot-zoom-hint" aria-hidden="true">Expand</span>
      </button>
      <figcaption class="screenshot-caption">${caption}</figcaption>
    </figure>`;
}

function liveAppButton(project) {
  if (project.liveUrl) {
    return `<a href="${project.liveUrl}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">Live App</a>`;
  }
  return `<span class="btn btn-sm btn-disabled" title="Add liveUrl in projects.json">Live App</span>`;
}

function caseStudyHtml(cs) {
  if (!cs) return '';
  const steps = [
    ['Problem', cs.problem],
    ['Data', cs.data],
    ['Analysis', cs.analysis],
    ['Modeling', cs.modeling],
    ['Insights', cs.insights],
    ['Results', cs.results]
  ];
  return `
    <div class="detail-block">
      <h3>Analytics Case Study</h3>
      ${steps.map(([label, text]) => `
        <div class="case-step">
          <strong>${label}</strong>
          <p>${text}</p>
        </div>
      `).join('')}
    </div>`;
}

function renderProject(project) {
  const title = project.displayName || project.name;
  document.getElementById('project-title').textContent = title;
  document.getElementById('project-tagline').textContent = project.oneLiner || project.purpose;
  document.title = `${title} — Daniel Cohen Portfolio`;

  const shots = project.screenshots || [];
  if (window.PortfolioLightbox && shots.length) {
    window.PortfolioLightbox.registerGallery(project.id, galleryItemsFromShots(shots, title));
  }
  const hero = shots.length ? screenshotImg(shots[0], title, project.id, 0) : '';
  const gallery = shots.length > 1
    ? `<div class="screenshot-gallery">${shots.slice(1).map((s, i) => screenshotImg(s, title, project.id, i + 1)).join('')}</div>`
    : '';

  const highlights = (project.detailHighlights || [])
    .map(h => `<li>${h}</li>`).join('');
  const features = (project.keyFeatures || [])
    .map(f => `<li>${f}</li>`).join('');

  document.getElementById('project-detail').innerHTML = `
    <div class="detail-layout">
      <div class="detail-main">
        ${hero}
        ${gallery}
        <div class="detail-block">
          <h3>Overview</h3>
          <p>${project.executiveSummary}</p>
        </div>
        <div class="detail-block">
          <h3>Analytics & Business Value</h3>
          <p>${project.businessValue}</p>
          <p style="margin-top:0.75rem;font-style:italic;">${project.recruiterTakeaway}</p>
        </div>
        ${highlights ? `
          <div class="detail-block">
            <h3>Portfolio Highlights</h3>
            <ul>${highlights}</ul>
          </div>` : ''}
        ${(project.detailSections || []).map(sec => `
          <div class="detail-block">
            <h3>${sec.title}</h3>
            <p>${sec.body}</p>
          </div>
        `).join('')}
        ${caseStudyHtml(project.caseStudy)}
      </div>
      <aside class="detail-sidebar">
        <h4>Actions</h4>
        <div class="showcase-actions" style="margin-bottom:1.25rem;">
          ${liveAppButton(project)}
          <a href="${project.github}" class="btn btn-outline btn-sm" target="_blank" rel="noopener">GitHub</a>
          <a href="${project.readme}" class="btn btn-secondary btn-sm" target="_blank" rel="noopener">README</a>
        </div>
        <h4>Status</h4>
        <p style="color:var(--accent-2);font-size:0.88rem;margin-bottom:1rem;">${project.status}</p>
        <h4>Readiness</h4>
        <p style="color:var(--gold);font-size:0.88rem;margin-bottom:1rem;">${project.readiness}/10</p>
        <h4>Technologies</h4>
        <div class="tech-tags" style="margin-bottom:1rem;">${(project.technologies || []).map(t => `<span class="tech-tag">${t}</span>`).join('')}</div>
        ${features ? `<h4>Key Features</h4><ul style="list-style:none;padding:0;">${features.replace(/<li>/g, '<li style="font-size:0.84rem;color:var(--muted);margin-bottom:0.35rem;">▸ ')}</ul>` : ''}
      </aside>
    </div>
  `;
}

async function init() {
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id');
  if (!id) {
    document.getElementById('project-detail').innerHTML = '<p>Project not specified. <a href="index.html#projects">Return to projects</a>.</p>';
    return;
  }
  try {
    const res = await fetch(DATA_PATH);
    const data = await res.json();
    const project = data.repos.find(p => p.id === id);
    if (!project) {
      document.getElementById('project-detail').innerHTML = '<p>Project not found. <a href="index.html#projects">Return to projects</a>.</p>';
      return;
    }
    renderProject(project);
  } catch (err) {
    console.error(err);
    document.getElementById('project-detail').innerHTML = '<p>Failed to load project data.</p>';
  }
}

document.addEventListener('DOMContentLoaded', init);
