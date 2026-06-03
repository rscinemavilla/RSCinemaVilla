---
layout: default
title: Booking Enquiry Form
permalink: /booking-enquiry-form/
---

<style>
  .rsv-booking-section {
    background: linear-gradient(180deg, #f8f4ee 0%, #f3ede4 100%);
    padding: 80px 20px;
    color: #1c1b19;
  }

  .rsv-booking-inner {
    max-width: 980px;
    margin: 0 auto;
  }

  .rsv-eyebrow {
    display: inline-block;
    margin-bottom: 14px;
    color: #b38a3f;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.24em;
    text-transform: uppercase;
  }

  .rsv-booking-section h1 {
    margin: 0 0 16px;
    font-size: clamp(2.2rem, 5vw, 3.8rem);
    line-height: 1.1;
    color: #111111;
  }

  .rsv-booking-intro {
    max-width: 760px;
    margin: 0 0 20px;
    font-size: 1rem;
    line-height: 1.85;
    color: #4f4a42;
  }

  .rsv-divider {
    display: block;
    width: 72px;
    height: 2px;
    margin: 24px 0 34px;
    background: linear-gradient(90deg, #b38a3f, rgba(179, 138, 63, 0.18));
  }

  .rsv-form-card {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(179, 138, 63, 0.22);
    border-radius: 22px;
    padding: 30px;
    box-shadow: 0 18px 42px rgba(17, 17, 17, 0.08);
  }

  .rsv-top-actions {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
  }

  .rsv-wa-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 48px;
    padding: 13px 22px;
    border-radius: 999px;
    background: #111111;
    color: #ffffff;
    text-decoration: none;
    font-weight: 700;
    transition: all 0.25s ease;
  }

  .rsv-wa-btn:hover {
    background: #222222;
    transform: translateY(-1px);
  }

  .rsv-form-row {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 18px;
  }

  .rsv-form-group {
    display: flex;
    flex-direction: column;
  }

  .rsv-form-group.full-width {
    grid-column: 1 / -1;
  }

  .rsv-form-group label {
    margin-bottom: 10px;
    font-weight: 600;
    color: #1d1b18;
  }

  .rsv-form-group input,
  .rsv-form-group textarea {
    width: 100%;
    padding: 14px 16px;
    border: 1px solid rgba(17, 17, 17, 0.14);
    border-radius: 14px;
    background: #fffdf9;
    color: #171717;
    font-size: 1rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
  }

  .rsv-form-group input:focus,
  .rsv-form-group textarea:focus {
    outline: none;
    border-color: #b38a3f;
    box-shadow: 0 0 0 4px rgba(179, 138, 63, 0.14);
  }

  .rsv-form-group textarea {
    min-height: 140px;
    resize: vertical;
  }

  .rsv-checkbox {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    padding: 14px 16px;
    border-radius: 14px;
    background: #faf6ef;
    border: 1px solid rgba(179, 138, 63, 0.16);
    line-height: 1.7;
    color: #4a453d;
  }

  .rsv-checkbox input {
    margin-top: 4px;
    accent-color: #b38a3f;
  }

  .rsv-submit-btn {
    margin-top: 24px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 52px;
    padding: 15px 28px;
    border: none;
    border-radius: 999px;
    background: linear-gradient(135deg, #c8a15a 0%, #a8803a 100%);
    color: #ffffff;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.25s ease;
  }

  .rsv-submit-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 14px 28px rgba(168, 128, 58, 0.24);
  }

  .rsv-form-note {
    margin-top: 18px;
    font-size: 0.96rem;
    line-height: 1.75;
    color: #5e564b;
  }

  .rsv-form-note a {
    color: #111111;
    font-weight: 700;
    text-decoration: none;
  }

  .rsv-success {
    display: none;
    margin-top: 22px;
    padding: 16px 18px;
    border-radius: 14px;
    background: #f6efe4;
    border: 1px solid rgba(179, 138, 63, 0.28);
    color: #42382d;
    line-height: 1.7;
  }

  .rsv-success.show {
    display: block;
  }

  @media (max-width: 768px) {
    .rsv-booking-section {
      padding: 64px 16px;
    }

    .rsv-form-card {
      padding: 22px 18px;
    }

    .rsv-form-row {
      grid-template-columns: 1fr;
    }

    .rsv-form-group.full-width {
      grid-column: 1;
    }

    .rsv-top-actions {
      justify-content: stretch;
    }

    .rsv-wa-btn,
    .rsv-submit-btn {
      width: 100%;
    }
  }
</style>

<section class="rsv-booking-section">
  <div class="rsv-booking-inner">
    <span class="rsv-eyebrow">Reserve Your Dates</span>
    <h1>Booking Enquiry Form</h1>

    <p class="rsv-booking-intro">
      Hello! Thank you so much for your interest in booking with us. Please share your details so we can check availability for RS Cinema Villa in Moinabad, Hyderabad. Once your dates are confirmed, you can make the advance payment and send the screenshot to 9206845678 on WhatsApp to complete your booking confirmation.
    </p>

    <span class="rsv-divider"></span>

    <div class="rsv-form-card">
      <div class="rsv-top-actions">
        <a
          href="https://wa.me/919206845678?text=Hello%20RS%20Cinema%20Villa%2C%20I%20would%20like%20to%20enquire%20about%20booking."
          target="_blank"
          rel="noopener noreferrer"
          class="rsv-wa-btn"
        >
          Chat on WhatsApp
        </a>
      </div>

      <form id="rsvBookingForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
        <input type="hidden" name="_subject" value="New Booking Enquiry - RS Cinema Villa">
        <input type="hidden" name="_captcha" value="false">

        <div class="rsv-form-row">
          <div class="rsv-form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" name="First Name" required>
          </div>

          <div class="rsv-form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="Email" required>
          </div>

          <div class="rsv-form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="Phone Number" required>
          </div>

          <div class="rsv-form-group">
            <label for="guests">Number of Guests</label>
            <input type="number" id="guests" name="Number of Guests" min="1" required>
          </div>

          <div class="rsv-form-group">
            <label for="checkin">Check-in Date</label>
            <input type="date" id="checkin" name="Check-in Date" required>
          </div>

          <div class="rsv-form-group">
            <label for="checkout">Check-out Date</label>
            <input type="date" id="checkout" name="Check-out Date" required>
          </div>

          <div class="rsv-form-group full-width">
            <label for="specialRequest">Special Request</label>
            <textarea id="specialRequest" name="Special Request" placeholder="Tell us about your stay, celebration, event, or any special requirement"></textarea>
          </div>

          <div class="rsv-form-group full-width">
            <label class="rsv-checkbox">
              <input type="checkbox" name="Booking Consent" required>
              <span>
                I understand that booking is confirmed only after availability confirmation and advance payment.
              </span>
            </label>
          </div>
        </div>

        <button type="submit" class="rsv-submit-btn">Submit Enquiry</button>

        <p class="rsv-form-note">
          After we confirm availability, please make the advance payment and send the screenshot to
          <a href="https://wa.me/919206845678" target="_blank" rel="noopener noreferrer">9206845678</a>
          on WhatsApp for final booking confirmation.
        </p>

        <div class="rsv-success" id="rsvSuccess">
          Thank you for your enquiry. Our team will review your requested dates and contact you shortly to confirm availability for RS Cinema Villa. Your booking will be confirmed only after availability confirmation and advance payment.
        </div>
      </form>
    </div>
  </div>
</section>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("rsvBookingForm");
  const successBox = document.getElementById("rsvSuccess");
  const checkin = document.getElementById("checkin");
  const checkout = document.getElementById("checkout");

  if (!form) return;

  const today = new Date().toISOString().split("T")[0];
  checkin.min = today;
  checkout.min = today;

  checkin.addEventListener("change", function () {
    checkout.min = checkin.value || today;
    
