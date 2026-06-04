/* ============================================================
   Barky Weight Selector — orchestration des 3 étapes
   Architecture : mapping bundle dynamique selon le poids
   ============================================================ */
(function () {
  'use strict';

  const cfg = window.barkyConfig;
  if (!cfg) {
    console.warn('[Barky] window.barkyConfig manquant.');
    return;
  }

  const form = document.getElementById('barky-selector-form');
  if (!form) return;

  // État applicatif
  const state = {
    weight: null,            // 'small' | 'medium' | 'large'
    bundleIndex: 0,          // index dans weightProfiles[weight].bundles (0, 1, 2)
    frequency: 'oneoff',     // 'oneoff' | 'subscription'
    cadence: null            // 'monthly' | 'bimonthly' | 'quarterly'
  };

  const $  = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const formatEUR = (n) => n.toFixed(2).replace('.', ',') + ' €';
  const formatPerDay = (n) => n.toFixed(2).replace('.', ',') + ' €/jour';

  function describeDuration(days) {
    if (days >= 60 && days % 30 === 0) {
      const months = days / 30;
      return months === 1 ? '1 mois' : months + ' mois';
    }
    if (days === 30) return '1 mois';
    if (days % 10 === 0 && days < 60) return days + ' jours';
    // approximation en mois pour les durées non rondes
    const months = Math.round((days / 30) * 10) / 10;
    return '~' + String(months).replace('.', ',') + ' mois';
  }

  function potImage(count) {
    // packshot pot fermé bleu pastel
    return 'https://cdn.shopify.com/s/files/1/1068/0146/3645/files/packshot-pot-ferme-bleu-pastel.webp?v=1777297630';
  }

  // ---------- ÉTAPE 2 : génération dynamique des cartes bundle ----------
  function renderBundles() {
    const grid = $('[data-bundle-grid]');
    if (!grid) return;

    if (!state.weight) {
      grid.innerHTML = '';
      return;
    }

    const profile = cfg.weightProfiles[state.weight];
    grid.innerHTML = profile.bundles.map((b, idx) => {
      const days = b.potsCount * profile.daysPerPot;
      const duration = describeDuration(days);
      const xBadge = b.potsCount > 1 ? `<span class="barky-bundle-x">×${b.potsCount}</span>` : '';
      const compareHtml = b.compare ? `<span class="barky-bundle-compare">${formatEUR(b.compare)}</span>` : '';
      return `
        <button type="button" class="barky-bundle-btn" data-bundle-index="${idx}"
          data-variant-id="${b.variantId}" data-price="${b.price}"
          ${b.isRecommended ? 'data-is-recommended="true"' : ''}
          aria-pressed="${idx === state.bundleIndex ? 'true' : 'false'}">
          <span class="barky-bundle-ribbon" data-recommend>Recommandé</span>
          <span class="barky-bundle-img-wrap">
            <img src="${potImage(b.potsCount)}" alt="${b.potsCount} pot${b.potsCount > 1 ? 's' : ''} Barky" loading="lazy">
            ${xBadge}
          </span>
          <span class="barky-bundle-label">${b.potsCount} pot${b.potsCount > 1 ? 's' : ''}</span>
          <span class="barky-bundle-prices">
            ${compareHtml}
            <span class="barky-bundle-price">${formatEUR(b.price)}</span>
          </span>
          <span class="barky-bundle-duration">${duration}</span>
        </button>
      `;
    }).join('');

    // Bind clicks
    $$('.barky-bundle-btn', grid).forEach(btn => {
      btn.addEventListener('click', () => {
        const idx = Number(btn.dataset.bundleIndex);
        selectBundle(idx);
      });
    });
  }

  // ---------- ÉTAPE 1 : POIDS ----------
  $$('.barky-weight-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const w = btn.dataset.weight;
      state.weight = w;

      // Visuel sélection poids
      $$('.barky-weight-btn').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));

      // Déverrouille les étapes 2 et 3
      $$('.barky-step--locked').forEach(s => {
        s.classList.remove('barky-step--locked');
        s.classList.add('barky-step--unlocked');
      });

      // Posologie
      const posologyEl = $('[data-posology]');
      if (posologyEl) posologyEl.textContent = cfg.weightProfiles[w].posology;

      // Sélectionne le bundle recommandé par défaut (index 0)
      const profile = cfg.weightProfiles[w];
      const defaultIdx = profile.bundles.findIndex(b => b.isRecommended);
      state.bundleIndex = defaultIdx >= 0 ? defaultIdx : 0;

      // Cadence par défaut selon poids
      state.cadence = profile.defaultCadence;
      const cadenceRadio = $(`.barky-cadence-btn[data-cadence="${state.cadence}"] input`);
      if (cadenceRadio) cadenceRadio.checked = true;
      syncCadenceVisuals();

      renderBundles();
      updateVariantInput();
      updatePrices();
    });
  });

  function selectBundle(idx) {
    state.bundleIndex = idx;
    $$('.barky-bundle-btn').forEach(b => {
      b.setAttribute('aria-pressed', String(Number(b.dataset.bundleIndex) === idx));
    });
    updateVariantInput();
    updatePrices();
  }

  // ---------- ÉTAPE 3 : FRÉQUENCE ----------
  $$('input[name="barky-freq"]').forEach(input => {
    input.addEventListener('change', () => {
      state.frequency = input.value;
      // Show/hide cadence selector
      const cadenceWrap = $('[data-cadence-wrap]');
      if (cadenceWrap) {
        if (state.frequency === 'subscription') cadenceWrap.removeAttribute('hidden');
        else cadenceWrap.setAttribute('hidden', '');
      }
      updateSellingPlan();
      updatePrices();
    });
  });

  // ---------- ÉTAPE 3 bis : CADENCE ----------
  $$('input[name="barky-cadence"]').forEach(input => {
    input.addEventListener('change', () => {
      state.cadence = input.value;
      syncCadenceVisuals();
      updateSellingPlan();
    });
  });

  function syncCadenceVisuals() {
    $$('.barky-cadence-btn').forEach(btn => {
      const input = btn.querySelector('input');
      btn.setAttribute('data-active', String(input && input.checked));
    });
  }

  // ---------- HELPERS ----------
  function currentBundle() {
    if (!state.weight) return null;
    return cfg.weightProfiles[state.weight].bundles[state.bundleIndex];
  }

  function updateVariantInput() {
    const b = currentBundle();
    const inp = $('#barky-input-variant');
    if (b && inp) inp.value = b.variantId;
  }

  function updateSellingPlan() {
    const inp = $('#barky-input-selling-plan');
    if (!inp) return;
    if (state.frequency === 'subscription' && state.cadence) {
      inp.value = cfg.sellingPlans[state.cadence] || '';
    } else {
      inp.value = '';
    }
  }

  function updatePrices() {
    const b = currentBundle();
    if (!b) return;
    const profile = cfg.weightProfiles[state.weight];
    const totalDays = b.potsCount * profile.daysPerPot;
    const oneoff = b.price;
    const sub    = Math.round(b.price * 0.75 * 100) / 100;

    $('[data-freq-price="oneoff"]').textContent       = formatEUR(oneoff);
    $('[data-freq-price="subscription"]').textContent = formatEUR(sub);
    const compareEl = $('[data-freq-compare]');
    if (compareEl) compareEl.textContent = formatEUR(oneoff);

    const ctaPriceEl = $('[data-cta-price]');
    const ctaPerDayEl = $('[data-cta-perday]');
    const currentTotal = state.frequency === 'subscription' ? sub : oneoff;
    const perDay = currentTotal / totalDays;
    if (ctaPriceEl)  ctaPriceEl.textContent  = formatEUR(currentTotal);
    if (ctaPerDayEl) ctaPerDayEl.textContent = 'Soit ' + formatPerDay(perDay);

    // D.3 — Trust signal livraison : conditionné à l'abo
    const shippingEl = $('[data-trust-shipping]');
    if (shippingEl) {
      shippingEl.textContent = state.frequency === 'subscription'
        ? '✓ Livraison offerte'
        : '✓ Port à ' + formatEUR(cfg.shipping.oneoff);
    }
  }

  // A.4 — Bannière LANCEMENT10 : afficher les places restantes
  function initLaunchBanner() {
    const banner = $('[data-launch-banner]');
    if (!banner || !cfg.launchOffer) return;
    if (cfg.launchOffer.remaining <= 0) {
      banner.hidden = true;
      return;
    }
    const remainingEl = banner.querySelector('[data-launch-remaining]');
    if (remainingEl) remainingEl.textContent = String(cfg.launchOffer.remaining);
  }

  // ---------- SOUMISSION ----------
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!state.weight) {
      const step1 = document.querySelector('[data-step="1"]');
      if (step1) {
        step1.scrollIntoView({ behavior: 'smooth', block: 'center' });
        step1.style.outline = '2px solid #463432';
        setTimeout(() => { step1.style.outline = ''; }, 1600);
      }
      return;
    }

    const cta = $('#barky-cta');
    const originalLabel = cta.querySelector('.barky-cta-label').textContent;
    cta.disabled = true;
    cta.querySelector('.barky-cta-label').textContent = 'Ajout au panier…';

    try {
      // 1) Ajoute le produit au panier
      const formData = new FormData(form);
      const items = { id: formData.get('id'), quantity: 1 };
      const sp = formData.get('selling_plan');
      if (sp) items.selling_plan = sp;

      const res = await fetch('/cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({ items: [items] })
      });

      if (!res.ok) {
        const errBody = await res.json().catch(() => ({}));
        console.error('[Barky] /cart/add.js error', res.status, errBody);
        throw new Error('Erreur ajout panier');
      }

      // 2) Redirection top-level via /discount/CODE → pose le cookie de code promo de manière fiable
      //    puis lande sur /cart où le client voit son panier (la remise -10% s'affiche au checkout)
      const launchCode = (cfg.launchOffer && cfg.launchOffer.code) || '';
      window.location.href = launchCode
        ? '/discount/' + encodeURIComponent(launchCode) + '?redirect=/cart'
        : '/cart';
    } catch (err) {
      console.error(err);
      cta.disabled = false;
      cta.querySelector('.barky-cta-label').textContent = originalLabel;
      alert('Une erreur est survenue. Réessayez ou contactez-nous.');
    }
  });

  // ---------- INIT ----------
  // Aucun poids sélectionné → bundle grid vide, étapes 2 et 3 verrouillées
  renderBundles();
  initLaunchBanner();
})();
