const DATA_PATH = new URL('data/projects.json', window.location.href).pathname;

async function loadData() {
  const res = await fetch(DATA_PATH);
  if (!res.ok) {
    throw new Error(`Failed to load portfolio data (${res.status}). Start the server from the Portfolio Website folder.`);
  }
  return res.json();
}

function showPageError(message) {
  const targets = ['resume-document', 'resume-overview', 'resume-bullets', 'career-profile-content', 'executive-summary-content'];
  const html = `
    <div class="page-error" style="background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;max-width:640px;margin:0 auto;">
      <h3 style="color:var(--gold);margin-bottom:0.75rem;">Page could not load content</h3>
      <p style="color:var(--muted);margin-bottom:0.75rem;">${message}</p>
      <p style="color:var(--muted);font-size:0.9rem;margin-bottom:1rem;">
        Run from <code>Portfolio Website</code>:<br>
        <code>python -m http.server 9890</code><br>
        or <code>powershell -File scripts/start-portfolio-server.ps1</code>
      </p>
      <p><a href="resume.html" class="btn btn-secondary btn-sm">Try Resume Hub</a>
         <a href="index.html" class="btn btn-ghost btn-sm">Home</a></p>
    </div>`;
  targets.forEach(id => {
    const el = document.getElementById(id);
    if (el && !el.innerHTML.trim()) el.innerHTML = html;
  });
}

function showLoading() {
  const root = document.getElementById('resume-document');
  if (root && !root.innerHTML.trim()) {
    root.innerHTML = '<p style="text-align:center;color:var(--muted);padding:2rem;">Loading resume…</p>';
  }
}

function skillTags(skills) {
  return `<div class="skill-tags">${skills.map(s => `<span class="skill-tag">${s}</span>`).join('')}</div>`;
}

function renderResumePreview(data) {
  const r = data.resume;
  const site = data.site;
  const root = document.getElementById('resume-document');
  if (!root || !r) return;

  document.title = `${r.name} — Resume`;
  const edu = r.education.map(e => `
    <div class="resume-entry">
      <div class="resume-entry-head">
        <strong>${e.degree}</strong>
        <span>${e.school}</span>
      </div>
      ${e.detail ? `<p class="resume-entry-detail">${e.detail}</p>` : ''}
    </div>
  `).join('');

  const exp = r.experience.map(e => `
    <div class="resume-entry">
      <div class="resume-entry-head">
        <strong>${e.title}</strong>
        ${e.period ? `<span>${e.period}</span>` : ''}
      </div>
      <div class="resume-entry-org">${e.organization}</div>
      <ul>${e.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
    </div>
  `).join('');

  const projects = r.projectBullets.map(p => `
    <div class="resume-entry">
      <div class="resume-entry-head">
        <strong>${p.name}</strong>
        <span>${p.tech}</span>
      </div>
      <ul>${p.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
    </div>
  `).join('');

  root.innerHTML = `
    <header class="resume-doc-header">
      <h1>${r.name}</h1>
      <p class="resume-doc-headline">${r.headline}</p>
      <p class="resume-doc-contact">
        <a href="${site.github}" target="_blank" rel="noopener">GitHub: ${site.github.replace('https://', '')}</a>
        · <a href="index.html">Portfolio</a>
      </p>
    </header>

    <section class="resume-doc-section">
      <h2>Professional Summary</h2>
      <p>${r.summary}</p>
    </section>

    <section class="resume-doc-section">
      <h2>Education</h2>
      ${edu}
    </section>

    <section class="resume-doc-section">
      <h2>Experience</h2>
      ${exp}
    </section>

    <section class="resume-doc-section">
      <h2>Selected Projects</h2>
      ${projects}
    </section>

    <section class="resume-doc-section">
      <h2>Technical Skills</h2>
      ${skillTags(r.technicalSkills)}
    </section>

    <section class="resume-doc-section">
      <h2>Target Roles</h2>
      <p class="resume-roles">${r.targetRoles.join(' · ')}</p>
    </section>
  `;

  const cta = document.getElementById('resume-preview-cta');
  if (cta) {
    cta.innerHTML = `
      <a href="${site.resumePdf}" class="btn btn-primary" download>Download PDF</a>
      <button type="button" class="btn btn-secondary" onclick="window.print()">Print / Save as PDF</button>
      <a href="${site.resumeHub || 'resume.html'}" class="btn btn-ghost">Resume Hub</a>
      <a href="${site.github}" class="btn btn-ghost" target="_blank" rel="noopener">GitHub</a>
    `;
  }
}

function renderResumeHub(data) {
  const r = data.resume;
  const site = data.site;

  const cta = document.getElementById('resume-cta');
  if (cta) {
    cta.innerHTML = `
      <a href="${site.resumeView}" class="btn btn-primary">View Resume Preview</a>
      <a href="${site.resumePdf}" class="btn btn-secondary" download>Download PDF</a>
      <a href="${site.careerProfile}" class="btn btn-ghost">Career Profile</a>
      <a href="${site.executiveSummary}" class="btn btn-ghost">Executive Summary</a>
    `;
  }

  const overview = document.getElementById('resume-overview');
  if (overview && r) {
    overview.innerHTML = `
      <div class="pro-grid pro-grid--2">
        <div class="pro-card">
          <h3>Education</h3>
          <ul class="pro-list">
            ${r.education.map(e => `<li><strong>${e.degree}</strong> — ${e.school}</li>`).join('')}
          </ul>
        </div>
        <div class="pro-card">
          <h3>Technical Skills</h3>
          ${skillTags(r.technicalSkills)}
        </div>
      </div>
      <p class="pro-lead" style="margin-top:1.5rem;">${r.summary}</p>
    `;
  }

  const bullets = document.getElementById('resume-bullets');
  if (bullets && r) {
    bullets.innerHTML = `
      <h3 class="section-subtitle">Experience Highlights</h3>
      ${r.experience.map(e => `
        <div class="content-block">
          <h3>${e.title} <span style="color:var(--muted);font-weight:400;">— ${e.organization}</span></h3>
          <ul>${e.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
        </div>
      `).join('')}
      <h3 class="section-subtitle" style="margin-top:2rem;">Project Bullets (copy-ready)</h3>
      ${r.projectBullets.map(p => `
        <div class="content-block">
          <h3>${p.name} <span style="color:var(--muted);font-weight:400;">| ${p.tech}</span></h3>
          <ul>${p.bullets.map(b => `<li>${b}</li>`).join('')}</ul>
        </div>
      `).join('')}
      <p style="margin-top:1.5rem;color:var(--muted);font-size:0.9rem;">
        Extended project descriptions:
        <a href="${site.resumeProjectBullets || '#'}" download>resume-project-descriptions.md</a>
      </p>
    `;
  }
}

function renderCareerProfile(data) {
  const cp = data.careerProfile;
  const root = document.getElementById('career-profile-content');
  if (!root || !cp) return;

  document.title = `${cp.title} — Daniel Cohen`;
  const s = cp.sections;

  root.innerHTML = `
    <div class="pro-lead-block">
      <h2>${s.professionalBackground.title}</h2>
      ${s.professionalBackground.paragraphs.map(p => `<p>${p}</p>`).join('')}
    </div>
    <div class="pro-lead-block">
      <h2>${s.analyticsAiTransition.title}</h2>
      ${s.analyticsAiTransition.paragraphs.map(p => `<p>${p}</p>`).join('')}
    </div>
    <div class="pro-lead-block">
      <h2>${s.portfolioHighlights.title}</h2>
      <div class="highlight-cards">
        ${s.portfolioHighlights.items.map(item => `
          <article class="highlight-card">
            <h3>${item.title}</h3>
            <p>${item.text}</p>
          </article>
        `).join('')}
      </div>
    </div>
    <div class="pro-lead-block">
      <h2>${s.coreTechnicalSkills.title}</h2>
      ${skillTags(s.coreTechnicalSkills.skills)}
    </div>
    <div class="pro-lead-block">
      <h2>${s.targetRoles.title}</h2>
      <div class="role-fit-grid">
        ${s.targetRoles.roles.map(r => `
          <article class="role-fit-card">
            <h3>${r.role}</h3>
            <p>${r.fit}</p>
          </article>
        `).join('')}
      </div>
    </div>
  `;

  const hero = document.getElementById('career-hero-subtitle');
  if (hero) hero.textContent = cp.subtitle;
}

function renderExecutiveSummary(data) {
  const doc = data.executiveSummaryDoc;
  const root = document.getElementById('executive-summary-content');
  if (!root || !doc) return;

  document.title = `${doc.title} — Daniel Cohen`;

  root.innerHTML = `
    <section class="exec-block exec-block--lead">
      <ul class="exec-strengths">
        ${doc.keyStrengths.map(s => `<li>${s}</li>`).join('')}
      </ul>
    </section>

    <section class="exec-block">
      <h2>${doc.quantitativeBackground.title}</h2>
      <p>${doc.quantitativeBackground.text}</p>
    </section>

    <section class="exec-block">
      <h2>${doc.technicalSkills.title}</h2>
      ${skillTags(doc.technicalSkills.skills)}
    </section>

    <section class="exec-block">
      <h2>${doc.analyticsProjects.title}</h2>
      <ul>${doc.analyticsProjects.items.map(i => `<li>${i}</li>`).join('')}</ul>
    </section>

    <section class="exec-block">
      <h2>${doc.aiRelatedWork.title}</h2>
      <ul>${doc.aiRelatedWork.items.map(i => `<li>${i}</li>`).join('')}</ul>
    </section>

    <section class="exec-block exec-block--direction">
      <h2>${doc.careerDirection.title}</h2>
      <p>${doc.careerDirection.text}</p>
    </section>
  `;

  const hero = document.getElementById('executive-hero-subtitle');
  if (hero) hero.textContent = doc.subtitle;

  const cta = document.getElementById('executive-cta');
  const site = data.site;
  if (cta) {
    cta.innerHTML = `
      <a href="${site.resumeView}" class="btn btn-primary">View Resume</a>
      <a href="${site.resumePdf}" class="btn btn-secondary" download>Download PDF</a>
      <a href="${site.careerProfile}" class="btn btn-ghost">Career Profile</a>
      <a href="contact.html" class="btn btn-ghost">Contact</a>
    `;
  }
}

async function init() {
  const page = document.body.dataset.page;
  if (page === 'resume-preview' || page === 'resume') showLoading();
  try {
    const data = await loadData();
    if (!data.resume && (page === 'resume-preview' || page === 'resume')) {
      throw new Error('Resume data missing from projects.json');
    }
    if (page === 'resume-preview') renderResumePreview(data);
    if (page === 'resume') renderResumeHub(data);
    if (page === 'career') renderCareerProfile(data);
    if (page === 'executive') renderExecutiveSummary(data);
  } catch (err) {
    console.error(err);
    showPageError(err.message || 'Unknown error loading portfolio data.');
  }
}

document.addEventListener('DOMContentLoaded', init);
