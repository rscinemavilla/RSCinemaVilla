---
layout: default
title: Pricing
---
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Georgia', serif; background: #0a0a0a; color: #f0e6d3; }

.site-header {
  background: rgba(0,0,0,0.92);
  padding: 18px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 1px solid rgba(212,175,55,0.3);
}
.site-header .brand {
  font-size: 1.5rem;
  font-weight: bold;
  color: #d4af37;
  text-decoration: none;
  letter-spacing: 1px;
}
.site-nav a {
  color: #f0e6d3;
  text-decoration: none;
  margin-left: 22px;
  font-size: 0.92rem;
  letter-spacing: 0.5px;
}
.site-nav a:hover { color: #d4af37; }
.site-nav a.active {
  color: #d4af37;
  border-bottom: 3px solid #d4af37;
  padding-bottom: 2px;
}

.hero {
  position: relative;
  height: 420px;
  background: url('/RSCinemaVilla/images/RScinemavilla5.JPG') center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.62);
}
.hero-box {
  position: relative;
  z-index: 2;
  border: 2px solid rgba(255,255,255,0.5);
  padding: 36px 56px;
  backdrop-filter: blur(2px);
}
.hero-box h1 {
  font-size: 3rem;
  color: #fff;
  letter-spacing: 3px;
  margin-bottom: 14px;
  text-transform: uppercase;
}
.hero-box p {
  font-size: 1.2rem;
  color: #f0e6d3;
  font-style: italic;
}

.section { padding: 60px 40px; max-width: 1100px; margin: 0 auto; }

.intro-block {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 10px;
  padding: 36px 40px;
  margin-bottom: 40px;
  text-align: center;
}
.intro-block p { font-size: 1.1rem; line-height: 1.8; color: #c8b89a; margin-bottom: 14px; }
.intro-block .phone { font-size: 1.2rem; color: #d4af37; font-weight: bold; }

.pricing-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-bottom: 40px;
}
.pricing-card {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.25);
  border-radius: 10px;
  padding: 32px 36px;
}
.pricing-card h3 {
  font-size: 1.4rem;
  color: #d4af37;
  margin-bottom: 20px;
}
.pricing-card ul {
  list-style: none;
  padding: 0;
}
.pricing-card ul li {
  color: #c8b89a;
  font-size: 1rem;
  line-height: 1.7;
  padding: 8px 0;
  border-bottom: 1px solid rgba(212,175,55,0.1);
}
.pricing-card ul li:last-child { border-bottom: none; }

.highlight-box {
  background: linear-gradient(135deg, #2a1f05, #1a1200);
  border: 2px solid #d4af37;
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  margin-bottom: 40px;
}
.highlight-box h2 { font-size: 1.6rem; color: #d4af37; margin-bottom: 14px; }
.highlight-box .price { font-size: 2rem; color: #fff; font-weight: bold; margin-bottom: 10px; }
.highlight-box p { color: #c8b89a; font-size: 1rem; line-height: 1.6; }

.cta-section {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 12px;
  padding: 50px 40px;
  text-align: center;
  margin-bottom: 40px;
}
.cta-section h2 { font-size: 1.6rem; color: #d4af37; margin-bottom: 14px; }
.cta-section p { color: #c8b89a; margin-bottom: 30px; font-size: 1.05rem; }
.cta-buttons { display: flex; gap: 16px; justify-content: center; flex-wrap: wrap; }
.btn {
  display: inline-block;
  padding: 14px 32px;
  border-radius: 6px;
  text-decoration: none;
  font-size: 1rem;
  font-weight: bold;
  transition: all 0.2s;
}
.btn-gold { background: #d4af37; color: #0a0a0a; }
.btn-gold:hover { background: #e6c84a; transform: translateY(-2px); }
.btn-outline { border: 2px solid #d4af37; color: #d4af37; background: transparent; }
.btn-outline:hover { background: rgba(212,175,55,0.1); transform: translateY(-2px); }
.btn-green { background: #25D366; color: #fff; }
.btn-green:hover { background: #1ebe57; transform: translateY(-2px); }
.btn-airbnb { background: #FF5A5F; color: #fff; }
.btn-airbnb:hover { background: #e04f54; transform: translateY(-2px); }

.footer-tagline {
  text-align: center;
  padding: 30px;
  color: #8a7a5a;
  font-style: italic;
  font-size: 1.05rem;
  border-top: 1px solid rgba(212,175,55,0.15);
}
</style>

<header class="site-header">
  <a href="/RSCinemaVilla/" class="brand">RS Cinema Villa</a>
  <nav class="site-nav">
    <a href="/RSCinemaVilla/">Home</a>
    <a href="/RSCinemaVilla/gallery/">Gallery</a>
    <a href="/RSCinemaVilla/about-villa/">About Villa</a>
    <a href="/RSCinemaVilla/pricing/" class="active">Pricing</a>
    <a href="/RSCinemaVilla/reviews/">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <p>Pricing</p>
  </div>
</section>

<div class="section">
  <div class="intro-block">
    <p>RS Cinema Villa offers <strong>flexible pricing</strong> based on your event type, duration, and guest count. Contact us for a custom quote tailored to your needs.</p>
    <p class="phone">&#128222; Phone / WhatsApp: <a href="tel:+919206845678" style="color:#d4af37;">+91 92068 45678</a></p>
  </div>

  <div class="pricing-grid">
    <div class="pricing-card">
      <h3>&#128336; Booking Options</h3>
      <ul>
        <li>&#127912; <strong>Day Use</strong> &mdash; Morning to Evening</li>
        <li>&#127769; <strong>Night Use</strong> &mdash; Evening to Morning</li>
        <li>&#127968; <strong>Full Day &amp; Night</strong> &mdash; 24-hour exclusive access</li>
        <li>&#128197; <strong>Multi-day Bookings</strong> &mdash; available on request</li>
      </ul>
    </div>

    <div class="pricing-card">
      <h3>&#127881; Events We Host</h3>
      <ul>
        <li>&#127874; Birthday Parties &amp; Celebrations</li>
        <li>&#128141; Engagements &amp; Pre-wedding Functions</li>
        <li>&#127968; Family Getaways &amp; Reunions</li>
        <li>&#127867; Private Parties &amp; Corporate Events</li>
        <li>&#127916; Movie Shoots &amp; Photo Sessions</li>
      </ul>
    </div>

    <div class="pricing-card">
      <h3>&#128203; What&rsquo;s Included</h3>
      <ul>
        <li>&#127946; Private swimming pool access</li>
        <li>&#127968; All 5 AC bedrooms</li>
        <li>&#127807; Manicured lawn &amp; outdoor areas</li>
        <li>&#127859; Fully-equipped kitchen</li>
        <li>&#127916; Cinema &amp; entertainment room</li>
        <li>&#128225; High-speed Wi-Fi</li>
        <li>&#128274; 24-hour support &amp; security</li>
      </ul>
    </div>

    <div class="pricing-card">
      <h3>&#128233; Get a Custom Quote</h3>
      <ul>
        <li>&#128222; Call or WhatsApp us for instant pricing</li>
        <li>&#127881; Custom packages for all event types</li>
        <li>&#128197; Flexible dates &amp; duration options</li>
        <li>&#128081; Dedicated support throughout your booking</li>
      </ul>
    </div>
  </div>

  <div class="highlight-box">
    <h2>&#128176; Starting From</h2>
    <div class="price">&#8377;20,000 per day</div>
    <p>Pricing varies by date, duration, and event type. Contact us for the best rates!</p>
  </div>

  <div class="cta-section">
    <h2>Ready to Book?</h2>
    <p>Contact us today for a custom quote and to check availability for your dates.</p>
    <div class="cta-buttons">
      <a href="https://wa.me/919206845678?text=Hi%2C%20I%20would%20like%20to%20know%20the%20pricing%20for%20RS%20Cinema%20Villa" class="btn btn-green" target="_blank">&#128172; WhatsApp Us for Pricing</a>
      <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
      <a href="https://www.airbnb.com/rooms/rscinemavilla" class="btn btn-airbnb" target="_blank">&#127968; View on Airbnb</a>
      <a href="https://www.instagram.com/rs_cinema_villa" class="btn btn-outline" target="_blank">&#128247; Follow us @rs_cinema_villa</a>
    </div>
  </div>
</div>

<div class="footer-tagline">The best moments in life are the ones worth planning for.</div>
