<!-- ============================================================
     RS Cinema Villa — Booking Enquiry Form
     Version A: Direct HTML Embed (Self-contained)
     Place inside any HTML page or Jekyll layout file
     ============================================================ -->

<style>
  /* ── BOOKING SECTION WRAPPER ── */
  .rsv-booking-section {
    background: #faf9f7;
    padding: 96px 24px;
    font-family: 'Jost', sans-serif;
    color: #1a1a1a;
  }

  .rsv-booking-inner {
    max-width: 780px;
    margin: 0 auto;
  }

  /* ── EYEBROW ── */
  .rsv-eyebrow {
    display: block;
    font-family: 'Jost', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #c9a96e;
    margin-bottom: 16px;
    text-align: center;
  }

  /* ── HEADING ── */
  .rsv-booking-section h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 20px;
    text-align: center;
    letter-spacing: 0.5px;
  }

  /* ── INTRO TEXT ── */
  .rsv-booking-intro {
    font-size: 15px;
    line-height: 1.8;
    color: #555;
    text-align: center;
    max-width: 640px;
    margin: 0 auto 48px;
  }

  /* ── GOLD DIVIDER ── */
  .rsv-divider {
    width: 48px;
    height: 1px;
    background: #c9a96e;
    margin: 0 auto 48px;
    display: block;
  }

  /* ── FORM CARD ── */
  .rsv-form-card {
    background: #fff;
    border: 1px solid rgba(201, 169, 110, 0.25);
    border-radius: 4px;
    padding: 48px 40px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.06);
  }

  /* ── FORM ROW (two-column on desktop) ── */
  .rsv-form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }

  .rsv-form-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 24px;
  }

  .rsv-form-group.full-width {
    grid-column: 1 / -1;
  }

  /* ── LABELS ── */
  .rsv-form-group label {
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #1a1a1a;
    margin-bottom: 8px;
  }

  .rsv-form-group label span.req {
    color: #c9a96e;
    margin-left: 2px;
  }

  /* ── INPUTS ── */
  .rsv-form-group input,
  .rsv-form-group select,
  .rsv-form-group textarea {
    font-family: 'Jost', sans-serif;
    font-size: 14px;
    color: #1a1a1a;
    background: #faf9f7;
    border: 1px solid rgba(0,0,0,0.15);
    border-radius: 3px;
    padding: 13px 16px;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
    width: 100%;
    box-sizing: border-box;
    appearance: none;
    -webkit-appearance: none;
  }

  .rsv-form-group input:focus,
  .rsv-form-group select:focus,
  .rsv-form-group textarea:focus {
    border-color: #c9a96e;
    box-shadow: 0 0 0 3px rgba(201,169,110,0.12);
    background: #fff;
  }

  .rsv-form-group input::placeholder,
  .rsv-form-group textarea::placeholder {
    color: #aaa;
  }

  .rsv-form-group select {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23c9a96e' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 16px center;
    padding-right: 40px;
    cursor: pointer;
  }

  .rsv-form-group textarea {
    resize: vertical;
    min-height: 110px;
    line-height: 1.6;
  }

  /* ── CHECKBOX ── */
  .rsv-checkbox-wrap {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 32px;
    padding: 18px 20px;
    background: #f0ebe1;
    border-left: 3px solid #c9a96e;
    border-radius: 2px;
  }

  .rsv-checkbox-wrap input[type="checkbox"] {
    width: 18px;
    height: 18px;
    min-width: 18px;
    accent-color: #c9a96e;
    cursor: pointer;
    margin-top: 2px;
  }

  .rsv-checkbox-wrap label {
    font-size: 13px;
    line-height: 1.7;
    color: #555;
    cursor: pointer;
  }

  .rsv-checkbox-wrap label strong {
    color: #1a1a1a;
  }

  /* ── SUBMIT BUTTON ── */
  .rsv-submit-btn {
    display: block;
    width: 100%;
    padding: 16px 32px;
    background: #1a1a1a;
    color: #fff;
    font-family: 'Jost', sans-serif;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    border: 2px solid #1a1a1a;
    border-radius: 3px;
    cursor: pointer;
    transition: background 0.2s, color 0.2s, border-color 0.2s;
    margin-bottom: 16px;
  }

  .rsv-submit-btn:hover {
    background: #c9a96e;
    border-color: #c9a96e;
    color: #fff;
  }

  .rsv-submit-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }

  /* ── WHATSAPP BUTTON ── */
  .rsv-wa-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
    padding: 14px 32px;
    background: transparent;
    color: #1a1a1a;
    font-family: 'Jost', sans-serif;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    border: 2px solid rgba(0,0,0,0.2);
    border-radius: 3px;
    text-decoration: none;
    transition: border-color 0.2s, background 0.2s;
    box-sizing: border-box;
    margin-bottom: 32px;
  }

  .rsv-wa-btn:hover {
    border-color: #25d366;
    background: rgba(37,211,102,0.06);
    color: #1a1a1a;
  }

  .rsv-wa-btn svg {
    flex-shrink: 0;
  }

  /* ── PAYMENT NOTE ── */
  .rsv-payment-note {
    font-size: 13px;
    line-height: 1.8;
    color: #777;
    text-align: center;
    padding: 20px;
    background: #faf9f7;
    border-top: 1px solid rgba(201,169,110,0.2);
    margin-top: 8px;
    border-radius: 0 0 3px 3px;
  }

  .rsv-payment-note strong {
    color: #1a1a1a;
  }

  /* ── SUCCESS MESSAGE ── */
  .rsv-success {
    display: none;
    text-align: center;
    padding: 48px 24px;
    animation: rsvFadeIn 0.5s ease;
  }

  .rsv-success-icon {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: rgba(201,169,110,0.12);
    border: 2px solid #c9a96e;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 24px;
  }

  .rsv-success h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.8rem;
    font-weight: 400;
    color: #1a1a1a;
    margin: 0 0 12px;
  }

  .rsv-success p {
    font-size: 14px;
    line-height: 1.8;
    color: #555;
    max-width: 480px;
    margin: 0 auto 24px;
  }

  .rsv-success .rsv-wa-btn {
    max-width: 320px;
    margin: 0 auto;
  }

  /* ── ERROR MESSAGE ── */
  .rsv-error-msg {
    display: none;
    font-size: 13px;
    color: #c0392b;
    text-align: center;
    padding: 12px;
    background: rgba(192,57,43,0.06);
    border-radius: 3px;
    margin-bottom: 16px;
  }

  /* ── FIELD ERROR ── */
  .rsv-field-error {
    font-size: 11px;
    color: #c0392b;
    margin-top: 5px;
    display: none;
  }

  .rsv-form-group.has-error input,
  .rsv-form-group.has-error select,
  .rsv-form-group.has-error textarea {
    border-color: #c0392b;
  }

  .rsv-form-group.has-error .rsv-field-error {
    display: block;
  }

  /* ── ANIMATION ── */
  @keyframes rsvFadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── RESPONSIVE ── */
  @media (max-width: 640px) {
    .rsv-form-card {
      padding: 32px 20px;
    }

    .rsv-form-row {
      grid-template-columns: 1fr;
    }

    .rsv-form-group.full-width {
      grid-column: 1;
    }

    .rsv-booking-section {
      padding: 64px 16px;
    }
  }
</style>

<!-- ── BOOKING SECTION ── -->
<section class="rsv-booking-section" id="book-your-stay">
  <div class="rsv-booking-inner">

    <span class="rsv-eyebrow">Reserve Your Dates</span>
    <h2>Book Your Stay</h2>
    <p class="rsv-booking-intro">
      Hello! Thank you so much for your interest in staying with us. RS Cinema Villa is a luxury private villa in Moinabad, Hyderabad — perfect for celebrations, staycations, film screenings, and intimate gatherings. Please fill in the form below and we'll check availability for your dates right away.
    </p>
    <span class="rsv-divider"></span>

    <!-- FORM CARD -->
    <div class="rsv-form-card">

      <!-- SUCCESS STATE (hidden by default) -->
      <div class="rsv-success" id="rsvSuccess">
        <div class="rsv-success-icon">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M6 14.5l5.5 5.5L22 9" stroke="#c9a96e" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
        <h3>Enquiry Received — Thank You!</h3>
        <p>
          We've received your booking enquiry and will get back to you shortly to confirm availability for your selected dates. Once confirmed, please make the advance payment and send the screenshot to <strong>9206845678</strong> on WhatsApp to complete your booking.
        </p>
        <a
          href="https://wa.me/919206845678?text=Hello%2C%20I%20just%20submitted%20a%20booking%20enquiry%20for%20RS%20Cinema%20Villa.%20Please%20confirm%20my%20dates."
          target="_blank"
          rel="noopener"
          class="rsv-wa-btn"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="#25d366" xmlns
