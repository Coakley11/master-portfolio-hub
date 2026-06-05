const DATA_PATH = 'data/projects.json';
const MANIFEST_PATH = 'assets/screenshots/screenshot-manifest.json';

let screenshotManifest = null;

async function loadData() {
  const res = await fetch(DATA_PATH);
  if (!res.ok) throw new Error('Failed to load portfolio data');
  return res.json();
}

async function loadManifest() {
  try {
    const res = await fetch(MANIFEST_PATH);
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}

function tierBadge(tier) {
  const labels = { 1: 'Tier 1 — Anchor', 2: 'Tier 2', 3: 'Tier 3' };
  return `<span class="tier-badge tier-${tier}">${labels[tier] || 'Project'}</span>`;
}

function techTags(technologies) {
  return (technologies || []).map(t => `<span class="tech-tag">${t}</span>`).join('');
}

function screenshotPlaceholder(name, hint) {
  const sub = hint ? `<div class="screenshot-hint">${hint}</div>` : '';
  return `<div class="screenshot-placeholder">Screenshot: ${name}${sub}</div>`;
}

function screenshotImg(src, alt, label) {
  const cap = label ? `<div class="screenshot-caption">${label}</div>` : '';
  const fname = src.split('/').pop() || 'screenshot.png';
  return `
    <figure class="screenshot-figure">
      <img src="${src}" alt="${alt}" class="screenshot-img" loading="lazy"
        onerror="this.classList.add('screenshot-img--missing');this.nextElementSibling?.classList.add('screenshot-missing--show')">
      <div class="screenshot-missing">Add file: <code>${fname}</code><br><span>Drop into <code>assets/screenshots/</code> — see Screenshots/HOW_TO_CAPTURE.md</span></div>
      ${cap}
    </figure>`;
}

function heroScreenshot(project) {
  const shots = project.screenshots || [];
  if (!shots.length) {
    const hint = project.heroScreenshot
      ? `Expected: assets/screenshots/${project.screenshotFolder}/${project.heroScreenshot}`
      : '';
    return screenshotPlaceholder(project.displayName || project.name, hint);
  }
  const hero = shots[0];
  const label = (project.heroScreenshot || '').replace('.png', '');
  return screenshotImg(hero, project.name, label);
}

function renderScreenshotGallery(project) {
  const shots = project.screenshots || [];
  if (!shots.length) {
    const hint = project.heroScreenshot
      ? `Expected: assets/screenshots/${project.screenshotFolder}/${project.heroScreenshot}`
      : '';
    return screenshotPlaceholder(project.name, hint);
  }

  const hero = shots[0];
  const heroLabel = project.heroScreenshot || '';
  let html = screenshotImg(hero, project.name, heroLabel ? heroLabel.replace('.png', '') : '');

  if (shots.length > 1) {
    html += `<div class="screenshot-thumbs">`;
    shots.slice(1, 5).forEach((src, i) => {
      const fname = src.split('/').pop() || `view-${i + 2}`;
      html += screenshotImg(src, `${project.name} — ${fname}`, fname.replace('.png', ''));
    });
    html += `</div>`;
  }
  return html;
}

function liveAppButton(project) {
  if (project.liveUrl) {
    return `<a href="${project.liveUrl}" class="btn btn-primary btn-sm" target="_blank" rel="noopener">Live App</a>`;
  }
  return `<span class="btn btn-sm btn-disabled" title="Add liveUrl in projects.json after Streamlit deploy">Live App</span>`;
}

function showcaseCard(project) {
  const features = (project.keyFeatures || []).slice(0, 5)
    .map(f => `<li>${f}</li>`).join('');
  const title = project.displayName || project.name;
  return `
    <article class="showcase-card" id="${project.id}">
      ${heroScreenshot(project)}
      <div class="showcase-body">
        <h3>${title}</h3>
        <p class="showcase-oneliner">${project.oneLiner || project.purpose}</p>
        <p class="showcase-value"><strong>Business value:</strong> ${project.businessValue}</p>
        <ul class="feature-list">${features}</ul>
        <div class="tech-tags">${techTags(project.technologies)}</div>
        <div class="showcase-actions">
          ${liveAppButton(project)}
          <a href="${project.github}" class="btn btn-outline btn-sm" target="_blank" rel="noopener">GitHub</a>
          <a href="project.html?id=${project.id}" class="btn btn-secondary btn-sm">Details</a>
        </div>
      </div>
    </article>`;
}

function projectCard(project) {
  return `
    <article class="project-card" id="${project.id}">
      ${tierBadge(project.tier)}
      ${renderScreenshotGallery(project)}
      <h3>${project.displayName || project.name}</h3>
      <div class="status">${project.status}</div>
      <p class="desc">${project.executiveSummary}</p>
      <div class="takeaway">${project.recruiterTakeaway}</div>
      <div class="tech-tags">${techTags(project.technologies)}</div>
      <div class="readiness">Portfolio Readiness: ${project.readiness}/10</div>
      <div class="card-links">
        <a href="${project.github}" target="_blank" rel="noopener">GitHub</a>
        <a href="${project.readme}" target="_blank" rel="noopener">README</a>
        ${project.featured ? `<a href="project.html?id=${project.id}">Details</a>` : ''}
      </div>
    </article>`;
}

function sqlWorkbookScreenshot(wb) {
  const map = {
    'ai-evaluator-analytics': 'assets/screenshots/SQL-Excel/sql-excel-ai-evaluator-dashboard.png',
    'investment-app-analysis': 'assets/screenshots/SQL-Excel/sql-excel-investment-workbook-dashboard.png',
    'quant-analytics': 'assets/screenshots/SQL-Excel/sql-excel-quant-claims.png',
    'real-world-data': 'assets/screenshots/SQL-Excel/sql-excel-real-world-credit-risk.png'
  };
  const src = map[wb.id];
  if (!src) return '';
  return screenshotImg(src, wb.name, wb.id);
}

function renderFeaturedAnalytics(data) {
  const container = document.getElementById('featured-analytics');
  if (!container || !data.featuredAnalytics) return;
  container.innerHTML = data.featuredAnalytics.map(item => `
    <article class="analytics-card">
      <div class="icon">${item.icon}</div>
      <h3>${item.title}</h3>
      <p>${item.text}</p>
    </article>
  `).join('');
}

function renderAboutMe(data) {
  const container = document.getElementById('about-me');
  const about = data.aboutMe;
  if (!container || !about) return;
  const pillars = (about.pillars || []).map(p => `
    <div class="pillar-card">
      <h4>${p.title}</h4>
      <p>${p.text}</p>
    </div>
  `).join('');
  container.innerHTML = `
    <div class="about-intro">
      <h3>${about.headline}</h3>
      <p class="sub">${about.subheadline}</p>
      ${about.paragraphs.map(p => `<p>${p}</p>`).join('')}
    </div>
    <div class="about-pillars">${pillars}</div>
  `;
}

function renderSkillsDashboard(data) {
  const container = document.getElementById('skills-dashboard');
  if (!container || !data.skillsDashboard) return;
  container.innerHTML = data.skillsDashboard.map(skill => `
    <div class="skill-meter">
      <div class="skill-meter-header">
        <strong>${skill.name}</strong>
        <span>${skill.category}</span>
      </div>
      <div class="skill-meter-bar">
        <div class="skill-meter-fill" style="width: ${skill.level}%"></div>
      </div>
    </div>
  `).join('');
}

function renderShowcaseProjects(data) {
  const container = document.getElementById('showcase-projects');
  if (!container) return;
  const ids = data.flagshipIds || [];
  const projects = data.repos.filter(p => ids.includes(p.id));
  container.innerHTML = projects.map(showcaseCard).join('');
}

function renderCaseStudies(data) {
  const container = document.getElementById('case-studies');
  if (!container) return;
  const ids = data.flagshipIds || [];
  const projects = data.repos.filter(p => ids.includes(p.id) && p.caseStudy);
  container.innerHTML = projects.map(p => {
    const cs = p.caseStudy;
    const steps = ['problem', 'data', 'analysis', 'modeling', 'insights', 'results'];
    const labels = {
      problem: 'Problem', data: 'Data', analysis: 'Analysis',
      modeling: 'Modeling', insights: 'Insights', results: 'Results'
    };
    return `
      <article class="case-study-card">
        <h3>${p.displayName || p.name}</h3>
        ${steps.map(key => `
          <div class="case-step">
            <strong>${labels[key]}</strong>
            <p>${cs[key]}</p>
          </div>
        `).join('')}
        <div class="case-study-link">
          <a href="project.html?id=${p.id}">View project detail →</a>
        </div>
      </article>
    `;
  }).join('');
}

function renderCtaSection(data) {
  const btns = document.getElementById('cta-buttons');
  const contact = document.getElementById('cta-contact');
  if (!btns || !contact) return;
  const site = data.site;
  btns.innerHTML = `
    <a href="${site.resumeView || 'resume.html'}" class="btn btn-primary">View Resume</a>
    <a href="${site.resumeDownload || '#'}" class="btn btn-secondary" download>Download Resume</a>
    <a href="contact.html" class="btn btn-ghost">Contact</a>
  `;
  const linkedInLine = site.linkedin
    ? `<span>💼 <a href="${site.linkedin}" target="_blank" rel="noopener">LinkedIn</a></span>`
    : `<span>💼 <span style="color:var(--muted)">${site.linkedinPlaceholder || 'LinkedIn — coming soon'}</span></span>`;
  contact.innerHTML = `
    <span>🔗 <a href="${site.github}" target="_blank" rel="noopener">GitHub</a></span>
    ${linkedInLine}
    <span><a href="contact.html">Contact page →</a></span>
  `;
}

function renderProjectsByCategory(data, categoryId, containerId) {
  const container = document.getElementById(containerId);
  if (!container) return;

  const projects = data.repos
    .filter(p => p.category === categoryId || p.secondaryCategories?.includes(categoryId))
    .sort((a, b) => a.tier - b.tier);

  container.innerHTML = `<div class="card-grid">${projects.map(projectCard).join('')}</div>`;
}

function renderHomeTiers(data) {
  const container = document.getElementById('home-projects');
  if (!container) return;

  const flagship = new Set(data.flagshipIds || []);
  const tiers = [
    { tier: 1, label: 'Tier 1 — Anchor Projects' },
    { tier: 2, label: 'Tier 2 — Strong Support' },
    { tier: 3, label: 'Tier 3 — Ecosystem & Development' }
  ];

  container.innerHTML = tiers.map(({ tier, label }) => {
    const projects = data.repos.filter(p => p.tier === tier && !flagship.has(p.id));
    if (!projects.length) return '';
    return `
      <div class="tier-section">
        <div class="tier-label">${label}</div>
        <div class="card-grid">${projects.map(projectCard).join('')}</div>
      </div>`;
  }).join('');
}

function renderSkills(data) {
  const container = document.getElementById('skill-tags');
  if (!container) return;
  container.innerHTML = data.summary.skills
    .map(s => `<span class="skill-tag">${s}</span>`)
    .join('');
}

function renderSummary(data) {
  const container = document.getElementById('summary-text');
  if (!container) return;
  container.innerHTML = data.summary.paragraphs.map(p => `<p>${p}</p>`).join('');
}

function renderSqlWorkbooks(data) {
  const container = document.getElementById('sql-workbooks');
  if (!container) return;

  container.innerHTML = `<div class="card-grid">${data.sqlExcelWorkbooks.map(wb => `
    <article class="project-card">
      ${sqlWorkbookScreenshot(wb)}
      <h3>${wb.name}</h3>
      <div class="status">${wb.domains.join(' · ')}</div>
      <p class="desc">${wb.executiveSummary}</p>
      <div class="takeaway">${wb.recruiterTakeaway}</div>
      <div class="tech-tags">
        ${wb.sqlQueryCount ? `<span class="tech-tag">${wb.sqlQueryCount} SQL queries</span>` : ''}
        ${wb.pivotExerciseCount ? `<span class="tech-tag">${wb.pivotExerciseCount} pivot exercises</span>` : ''}
        ${wb.sheets.map(s => `<span class="tech-tag">${s}</span>`).join('')}
      </div>
      ${wb.file ? `<div class="card-links"><span style="color:var(--muted);font-size:0.85rem;">📁 ${wb.file}</span></div>` : '<div class="card-links"><span style="color:var(--gold);font-size:0.85rem;">PDF only — restore .xlsx source</span></div>'}
    </article>
  `).join('')}</div>`;
}

function renderResumeBullets(data) {
  const container = document.getElementById('resume-bullets');
  if (!container) return;

  const all = [...data.repos, ...data.sqlExcelWorkbooks.filter(w => w.id !== 'actuarial-analytics')];
  container.innerHTML = all.map(item => `
    <div class="content-block">
      <h3>${item.name}</h3>
      <ul>
        <li>${item.executiveSummary}</li>
        <li><strong>Skills:</strong> ${(item.skills || item.technologies || []).join(', ')}</li>
        <li><em>${item.recruiterTakeaway}</em></li>
      </ul>
    </div>
  `).join('');
}

function renderResumeCta(data) {
  const container = document.getElementById('resume-cta');
  if (!container) return;
  const site = data.site;
  container.innerHTML = `
    <div class="cta-buttons">
      <a href="${site.resumeDownload || '#'}" class="btn btn-primary" download>Download Resume (Markdown)</a>
      <a href="${site.github}" class="btn btn-secondary" target="_blank" rel="noopener">GitHub</a>
    </div>
  `;
}

function renderContactPage(data) {
  const grid = document.getElementById('contact-grid');
  if (!grid) return;
  const site = data.site;
  const linkedInCard = site.linkedin
    ? `<div class="contact-card">
        <h3>LinkedIn</h3>
        <p><a href="${site.linkedin}" target="_blank" rel="noopener">View LinkedIn Profile</a></p>
        <p>Professional networking & featured projects</p>
      </div>`
    : `<div class="contact-card">
        <h3>LinkedIn</h3>
        <p style="color:var(--muted)">${site.linkedinPlaceholder || 'Profile link coming soon'}</p>
        <p>Will be added when final URL is available</p>
      </div>`;
  grid.innerHTML = `
    <div class="contact-card contact-card--primary">
      <h3>Get in Touch</h3>
      <p>Open to Data Analyst, BI, Quant, Financial Analyst, AI Evaluator, and AI Trainer roles.</p>
      <a href="mailto:${site.email}" class="btn btn-primary" style="margin-top:0.75rem;">Send Email</a>
      <p class="contact-note">Email is available via the button above — not displayed on the public homepage.</p>
    </div>
    <div class="contact-card">
      <h3>GitHub</h3>
      <p><a href="${site.github}" target="_blank" rel="noopener">${site.github.replace('https://', '')}</a></p>
      <p>7 public repositories in the Daniel AI Suite</p>
    </div>
    ${linkedInCard}
    <div class="contact-card">
      <h3>Resume</h3>
      <p><a href="${site.resumeView || 'resume.html'}" class="btn btn-secondary btn-sm">View Resume</a></p>
      <p style="margin-top:0.5rem;"><a href="${site.resumeDownload || '#'}" download>Download project descriptions (Markdown)</a></p>
    </div>
    <div class="contact-card">
      <h3>Target Roles</h3>
      <p>Data Analyst · BI Analyst · Research Analyst</p>
      <p>Quant Analyst · Financial Analyst · AI Evaluator · AI Trainer</p>
    </div>
  `;
}

function renderLinkedIn(data) {
  const container = document.getElementById('linkedin-posts');
  if (!container) return;

  const anchors = data.repos.filter(p => p.tier === 1);
  container.innerHTML = anchors.map(p => `
    <div class="content-block">
      <h3>${p.name}</h3>
      <p style="color:var(--muted);margin-bottom:0.75rem;">${p.executiveSummary}</p>
      <p><strong>Technologies:</strong> ${p.technologies.join(' · ')}</p>
      <p style="margin-top:0.5rem;font-style:italic;">${p.recruiterTakeaway}</p>
      <p style="margin-top:0.75rem;"><a href="${p.github}" target="_blank">${p.github}</a></p>
      <button class="copy-btn" onclick="copyText(this)">Copy to clipboard</button>
    </div>
  `).join('');
}

function copyText(btn) {
  const block = btn.closest('.content-block');
  const text = block.innerText.replace('Copy to clipboard', '').trim();
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => { btn.textContent = 'Copy to clipboard'; }, 2000);
  });
}

function setActiveNav() {
  const page = document.body.dataset.page;
  if (!page) return;
  document.querySelectorAll('.nav-links a').forEach(a => {
    if (a.dataset.page === page) a.classList.add('active');
  });
}

async function init() {
  try {
    screenshotManifest = await loadManifest();
    const data = await loadData();
    setActiveNav();
    renderSkills(data);
    renderSummary(data);
    renderFeaturedAnalytics(data);
    renderAboutMe(data);
    renderSkillsDashboard(data);
    renderShowcaseProjects(data);
    renderCaseStudies(data);
    renderHomeTiers(data);
    renderCtaSection(data);
    renderProjectsByCategory(data, 'analytics', 'analytics-projects');
    renderProjectsByCategory(data, 'ai', 'ai-projects');
    renderProjectsByCategory(data, 'applications', 'app-projects');
    renderProjectsByCategory(data, 'infrastructure', 'infra-projects');
    renderSqlWorkbooks(data);
    renderResumeBullets(data);
    renderResumeCta(data);
    renderContactPage(data);
    renderLinkedIn(data);

    const title = document.getElementById('site-title');
    if (title) title.textContent = data.site.title;
    const tagline = document.getElementById('site-tagline');
    if (tagline) tagline.textContent = data.site.tagline;
  } catch (err) {
    console.error(err);
  }
}

document.addEventListener('DOMContentLoaded', init);
