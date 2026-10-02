/**
 * UGS - UNITED GAS SOLUTIONS - THE LEADER BY DESIGN
 * Interactive Application Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  // Service Data Directory for interactive detail modals
  const SERVICES_DATA = {
    1: {
      title: "GAS SERVICE OPERATIONS",
      image: "assets/service_gas_service_operations.jpg",
      scope: "Comprehensive gas distribution field services with operator-qualified technicians adhering strictly to local, state, and DOT 49 CFR Part 192 compliance standards.",
      chips: ["✓ Veriforce OQ Certified", "✓ GPS Telemetry Dispatched", "✓ Live CGI Testing"],
      deliverables: [
        "Trained and evaluated under rigorous Operator Qualification (OQ) programs.",
        "Real-time work order submission with timestamped photographic proof of completion.",
        "Equipped with calibrated combustible gas indicators (CGI) and digital pressure gauges.",
        "Adherence to strict OSHA PPE standards and utility partner operating manuals."
      ]
    },
    2: {
      title: "METER SERVICES",
      image: "assets/service_meter_services.jpg",
      scope: "Precision gas meter installations, exchanges, index readings, AMR/AMI retrofits, and high-accuracy regulator testing for commercial and residential utility networks.",
      chips: ["✓ AMR / AMI Retrofits", "✓ Digital Barcode Verification", "✓ Bubble Leak Audited"],
      deliverables: [
        "Automated optical scan and serial number verification into client GIS databases.",
        "Digital soap bubble leak detection and electronic sniffer clearance on all spuds and unions.",
        "Regulator set-point calibration and lockup pressure checks.",
        "Customer notification protocols and secure property access management."
      ]
    },
    3: {
      title: "TURN-ONS & RECONNECTS",
      image: "assets/service_turn_ons_reconnects.jpg",
      scope: "Safe reactivation of gas services, appliance lighting, house line pressure drop testing, and appliance burner inspections to ensure complete household safety.",
      chips: ["✓ Pressure Drop Manometer Test", "✓ Flame Pattern Certification", "✓ Carbon Monoxide Checked"],
      deliverables: [
        "10-minute digital or water manometer pressure drop test verifying zero house line leaks.",
        "Safe appliance purge, pilot lighting, and operational burner checks.",
        "Inspection of appliance venting and combustion air requirements.",
        "Customer signature capture and digital certificate of safe reactivation."
      ]
    },
    4: {
      title: "DISCONNECT & SHUT OFF OPERATIONS",
      image: "assets/service_disconnect_shutoff.jpg",
      scope: "Controlled valve isolation, lock-out/tag-out (LOTO), blind flange installation, and physical curb valve disconnections for maintenance or non-payment workflows.",
      chips: ["✓ Tamper-Proof Locking", "✓ GPS Date/Time Verification", "✓ Safe Purging Protocol"],
      deliverables: [
        "Implementation of utility-mandated lock-out hardware and serialized security seals.",
        "Riser valve closure with documented bubble leak verification on valve seat.",
        "Photographic capture of final meter index and seal number.",
        "Immediate real-time sync with utility billing and customer service systems."
      ]
    },
    5: {
      title: "METER RENEWALS",
      image: "assets/service_meter_renewals.jpg",
      scope: "Scheduled and programmatic meter change-out (MCO) campaigns, obsolete diaphragm meter replacements, and ultrasonic meter upgrades at high-volume scale.",
      chips: ["✓ Mass MCO Campaigns", "✓ Hazmat Safe Disposal", "✓ High-Volume Output"],
      deliverables: [
        "Turnkey route planning and programmatic customer pre-notification letters.",
        "Replacement of aged meters, swivels, and rusted regulator brackets.",
        "Corrosion remediation and primer/topcoat painting on customer risers.",
        "Reclaimed meter logistics and chain-of-custody return to utility testing yards."
      ]
    },
    6: {
      title: "FIELD INSPECTIONS",
      image: "assets/service_field_inspections.jpg",
      scope: "Thorough visual, atmospheric corrosion, and leak surveys utilizing optical methane detectors (OMD) and handheld laser spectroscopy.",
      chips: ["✓ Laser Spectroscopy", "✓ Atmospheric Corrosion Audits", "✓ GIS Heatmaps"],
      deliverables: [
        "Walking and mobile flame ionization/laser methane surveys.",
        "Atmospheric corrosion grading (Grade 1, 2, 3) with photo documentation.",
        "Immediate Grade 1 emergency leak response protocol with standby capability.",
        "Full spatial GIS compliance reporting for state public service commissions."
      ]
    },
    7: {
      title: "UTILITY WORKFORCE SUPPORT",
      image: "assets/service_utility_workforce_support.jpg",
      scope: "Dedicated, badged, and fully equipped workforce augmentation for regulated utilities experiencing seasonal surges, capital improvement initiatives, or staffing gaps.",
      chips: ["✓ Scalable Crew Mobilization", "✓ Fully Outfitted Fleets", "✓ Zero OJT Delay"],
      deliverables: [
        "Operator Qualified (OQ) field personnel integrated directly into utility workflows.",
        "Equipped with late-model utility service vehicles, calibrated tools, and rugged tablets.",
        "Daily field supervisor oversight, tailboards, and safety audits.",
        "Flexible staff augmentation under performance-based SLA contracts."
      ]
    },
    8: {
      title: "MANAGED FIELD OPERATIONS",
      image: "assets/service_managed_field_operations.jpg",
      scope: "Turnkey program management covering complete regional field operations, dispatch optimization, quality assurance, and KPI-driven performance accountability.",
      chips: ["✓ End-to-End SLAs", "✓ 24/7 Dispatch Control", "✓ Custom KPI Dashboards"],
      deliverables: [
        "Centralized routing and dispatch managed by veteran gas operations coordinators.",
        "Automated customer appointment scheduling and SMS arrival updates.",
        "Weekly executive KPI reporting on completion rates, first-time resolution, and QA scores.",
        "Emergency on-call crews ready for storm mobilization and rapid mutual aid."
      ]
    }
  };

  // Header Scroll State
  const header = document.getElementById('site-header');
  const backToTopBtn = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    const scrollPos = window.scrollY;

    if (scrollPos > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    if (scrollPos > 350) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  }, { passive: true });

  // Back to Top Click
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Mobile Navigation Drawer
  const menuToggle = document.getElementById('mobile-menu-toggle');
  const mobileDrawer = document.getElementById('mobile-drawer');
  const drawerClose = document.getElementById('drawer-close');

  function openDrawer() {
    mobileDrawer.classList.add('open');
    menuToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    mobileDrawer.classList.remove('open');
    menuToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  if (menuToggle && mobileDrawer && drawerClose) {
    menuToggle.addEventListener('click', openDrawer);
    drawerClose.addEventListener('click', closeDrawer);

    // Close when clicking any nav link inside drawer
    document.querySelectorAll('.drawer-link').forEach(link => {
      link.addEventListener('click', closeDrawer);
    });
  }

  // Active Nav Link Spy on Scroll
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
      const sectionHeight = section.offsetHeight;
      const sectionTop = section.offsetTop - 120;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  }, { passive: true });

  // Modal Management
  const modals = document.querySelectorAll('.modal-backdrop');

  function openModal(modalId) {
    const targetModal = document.getElementById(modalId);
    if (targetModal) {
      targetModal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeAllModals() {
    modals.forEach(m => m.classList.remove('open'));
    document.body.style.overflow = '';
  }

  // Close modal button listeners
  document.querySelectorAll('[data-close-modal]').forEach(btn => {
    btn.addEventListener('click', closeAllModals);
  });

  // Close when clicking modal backdrop outside dialog
  modals.forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeAllModals();
      }
    });
  });

  // Close on Escape Key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllModals();
      closeDrawer();
    }
  });

  // Partner Modal Triggers
  document.querySelectorAll('.btn-partner-modal').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      closeDrawer();
      openModal('partner-modal');
    });
  });

  // Discuss A Project Button
  const btnDiscuss = document.getElementById('btn-discuss-project');
  if (btnDiscuss) {
    btnDiscuss.addEventListener('click', () => {
      openModal('partner-modal');
    });
  }

  // Safety Standards Modal Trigger
  const btnSafety = document.getElementById('btn-safety-standards');
  if (btnSafety) {
    btnSafety.addEventListener('click', () => {
      openModal('safety-modal');
    });
  }

  // Explore Careers Modal Trigger
  const btnCareers = document.getElementById('btn-explore-careers');
  if (btnCareers) {
    btnCareers.addEventListener('click', () => {
      openModal('careers-modal');
    });
  }

  // Coverage Button Trigger
  const btnCoverage = document.getElementById('btn-our-coverage');
  if (btnCoverage) {
    btnCoverage.addEventListener('click', () => {
      showToast("📍 UGS South Florida Network: Active field operations in Miami-Dade, Broward, Palm Beach, Martin, and St. Lucie counties.");
    });
  }

  // The UGS Advantage Button Trigger
  const btnAdvantage = document.getElementById('btn-tech-advantage');
  if (btnAdvantage) {
    btnAdvantage.addEventListener('click', () => {
      showToast("⚡ UGS SmartDispatch: Live GPS telemetry and automatic route balancing reduce transit times by 28%.");
    });
  }

  // Learn More About Us Trigger
  const btnLearnMore = document.getElementById('btn-learn-more');
  if (btnLearnMore) {
    btnLearnMore.addEventListener('click', () => {
      document.querySelector('#solutions').scrollIntoView({ behavior: 'smooth' });
    });
  }

  // View All Services Button Trigger
  const btnViewAll = document.getElementById('btn-view-all-services');
  if (btnViewAll) {
    btnViewAll.addEventListener('click', () => {
      openServiceModal(1);
    });
  }

  // Service Card Click Handler
  function openServiceModal(serviceId) {
    const data = SERVICES_DATA[serviceId] || SERVICES_DATA[1];
    
    document.getElementById('modal-service-title').textContent = data.title;
    document.getElementById('modal-service-img').src = data.image;
    document.getElementById('modal-service-img').alt = data.title;
    document.getElementById('modal-service-desc').textContent = data.scope;

    const listEl = document.getElementById('modal-service-list');
    listEl.innerHTML = '';
    data.deliverables.forEach(item => {
      const li = document.createElement('li');
      li.textContent = item;
      listEl.appendChild(li);
    });

    openModal('service-modal');
  }

  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('click', () => {
      const id = card.getAttribute('data-service-id');
      openServiceModal(id);
    });
  });

  // Interactive Tech Feature Click
  document.querySelectorAll('.tech-feature-item').forEach(item => {
    item.addEventListener('click', () => {
      const techType = item.getAttribute('data-tech');
      const name = item.querySelector('.tech-feature-name').textContent;
      showToast(`⚡ ${name}: Active 24/7 in our regional South Florida dispatch centers.`);
    });
  });

  // Apply Now buttons inside Careers Modal
  document.querySelectorAll('.apply-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const jobTitle = e.target.closest('.job-item').querySelector('.job-title').textContent;
      closeAllModals();
      openModal('partner-modal');
      const messageField = document.getElementById('p-message');
      if (messageField) {
        messageField.value = `Application for: ${jobTitle}\n\nPlease review my interest and contact me regarding the recruitment process.`;
      }
      showToast(`📝 Started application for: ${jobTitle}`);
    });
  });

  // Partner Form Submission Handler
  const partnerForm = document.getElementById('partner-form');
  if (partnerForm) {
    partnerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('p-name').value;
      const company = document.getElementById('p-company').value;
      
      closeAllModals();
      partnerForm.reset();
      showToast(`✅ Thank you, ${name}! Your inquiry for ${company} has been received. A UGS operational director will contact you within 24 hours.`);
    });
  }

  // Toast Notification System
  function showToast(message) {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }

  // Animated Numbers Counter for Performance Stats
  const statCards = document.querySelectorAll('.stat-card');
  let animated = false;

  function animateStats() {
    if (animated) return;
    
    statCards.forEach(card => {
      const numberEl = card.querySelector('.stat-number');
      const target = parseInt(card.getAttribute('data-target'), 10);
      const suffix = card.getAttribute('data-suffix') || '';
      
      if (isNaN(target)) return;

      const duration = 1600;
      const startTime = performance.now();

      function updateNumber(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing: easeOutExpo
        const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const currentVal = Math.floor(ease * target);

        numberEl.textContent = currentVal.toLocaleString() + suffix;

        if (progress < 1) {
          requestAnimationFrame(updateNumber);
        } else {
          numberEl.textContent = target.toLocaleString() + suffix;
        }
      }

      requestAnimationFrame(updateNumber);
    });

    animated = true;
  }

  // Observe Stats Section
  const statsSection = document.querySelector('.performance-stats-bar');
  if (statsSection && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateStats();
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.35 });

    observer.observe(statsSection);
  } else {
    animateStats();
  }

  // Privacy Policy and Contact Links
  const privacyLink = document.getElementById('footer-privacy-link');
  if (privacyLink) {
    privacyLink.addEventListener('click', (e) => {
      e.preventDefault();
      showToast("🔒 Privacy & Compliance Policy: UGS enforces strict data governance under SOC2 & utility regulatory standards.");
    });
  }

  const contactLink = document.getElementById('footer-contact-link');
  if (contactLink) {
    contactLink.addEventListener('click', (e) => {
      e.preventDefault();
      document.querySelector('#contact').scrollIntoView({ behavior: 'smooth' });
    });
  }

});
