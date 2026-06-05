/** Shared site navigation — inject into .nav-links on each page */
(function () {
  const ITEMS = [
    { href: 'index.html', page: 'home', label: 'Home' },
    { href: 'index.html#projects', page: null, label: 'Projects' },
    { href: 'career-profile.html', page: 'career', label: 'Career' },
    { href: 'executive-summary.html', page: 'executive', label: 'Summary' },
    { href: 'resume.html', page: 'resume', label: 'Resume' },
    { href: 'sql-excel.html', page: 'sql-excel', label: 'SQL & Excel' },
    { href: 'contact.html', page: 'contact', label: 'Contact' }
  ];

  function renderNav() {
    const nav = document.querySelector('.nav-links');
    if (!nav || nav.dataset.staticNav === 'true') return;
    const current = document.body.dataset.page || '';
    nav.innerHTML = ITEMS.map(item => {
      const active = item.page && item.page === current ? ' class="active"' : '';
      return `<li><a href="${item.href}" data-page="${item.page || ''}"${active}>${item.label}</a></li>`;
    }).join('');
  }

  document.addEventListener('DOMContentLoaded', renderNav);
})();
