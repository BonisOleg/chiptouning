/* ============================================
   main.js — Mobile menu, scroll, animations,
   services tabs, FAQ, HTMX, modal
   ============================================ */

(function () {
  'use strict';

  /* ── Mobile menu ── */
  var burger = document.querySelector('.header__burger');
  var mobileNav = document.getElementById('mobile-nav');

  function toggleNav(open) {
    if (!burger || !mobileNav) return;
    burger.setAttribute('aria-expanded', String(open));
    mobileNav.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  }

  if (burger) {
    burger.addEventListener('click', function () {
      var isOpen = burger.getAttribute('aria-expanded') === 'true';
      toggleNav(!isOpen);
    });
  }

  document.querySelectorAll('[data-close-nav]').forEach(function (el) {
    el.addEventListener('click', function () { toggleNav(false); });
  });

  document.addEventListener('click', function (e) {
    if (
      mobileNav &&
      mobileNav.classList.contains('open') &&
      !mobileNav.contains(e.target) &&
      e.target !== burger &&
      !burger.contains(e.target)
    ) {
      toggleNav(false);
    }
  });

  /* ── Header scroll shadow ── */
  var header = document.getElementById('header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('scrolled', window.scrollY > 10);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── Active nav link on scroll ── */
  var sections = document.querySelectorAll('section[id]');
  var navLinks = document.querySelectorAll('.nav__link[href^="#"]');

  if ('IntersectionObserver' in window && sections.length) {
    var sectionObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          navLinks.forEach(function (link) {
            var href = link.getAttribute('href');
            link.classList.toggle('active', href === '#' + entry.target.id);
          });
        }
      });
    }, { rootMargin: '-50% 0px -50% 0px' });

    sections.forEach(function (s) { sectionObserver.observe(s); });
  }

  /* ── Reveal animations ── */
  var revealObserver;
  if ('IntersectionObserver' in window) {
    revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var delay = entry.target.style.getPropertyValue('--reveal-delay') || '0s';
          entry.target.style.transitionDelay = delay;
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0 });

    document.querySelectorAll('.js-reveal').forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    document.querySelectorAll('.js-reveal').forEach(function (el) {
      el.classList.add('revealed');
    });
  }

  /* ── Services tabs ── */
  var tabs = document.querySelectorAll('.services__tab');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      var panelId = tab.getAttribute('data-tab');
      tabs.forEach(function (t) {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
      });
      document.querySelectorAll('.services__panel').forEach(function (p) {
        p.classList.remove('active');
      });
      tab.classList.add('active');
      tab.setAttribute('aria-selected', 'true');
      var panel = document.querySelector('[data-panel="' + panelId + '"]');
      if (panel) panel.classList.add('active');
    });
  });

  /* ── FAQ: exclusive accordion ── */
  var faqItems = document.querySelectorAll('details.faq__item');
  faqItems.forEach(function (det) {
    var summary = det.querySelector('summary');
    if (!summary) return;
    summary.addEventListener('click', function () {
      faqItems.forEach(function (other) {
        if (other !== det && other.open) {
          other.removeAttribute('open');
        }
      });
    });
  });

  /* ── HTMX: re-observe reveals after swap ── */
  document.body.addEventListener('htmx:afterSwap', function () {
    if (!revealObserver) return;
    document.querySelectorAll('.js-reveal:not(.revealed)').forEach(function (el) {
      revealObserver.observe(el);
    });
  });

  /* ── Modal ── */
  var modalOverlay = document.getElementById('hero-modal');

  function openModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    var closeBtn = modalOverlay.querySelector('[data-close-modal]');
    if (closeBtn) closeBtn.focus();
  }

  function closeModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }

  document.querySelectorAll('[data-open-modal]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      openModal();
    });
  });

  document.querySelectorAll('[data-close-modal]').forEach(function (btn) {
    btn.addEventListener('click', closeModal);
  });

  if (modalOverlay) {
    modalOverlay.addEventListener('click', function (e) {
      if (e.target === modalOverlay) closeModal();
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('is-open')) {
      closeModal();
    }
  });

})();
