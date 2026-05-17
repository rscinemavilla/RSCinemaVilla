---
layout: default
title: Contact & Book Now
permalink: /contact/
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
  background: url('/RSCinemaVilla/images/RScinemavilla2.JPG') center/cover no-repeat;
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

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-bottom: 40px;
}

.map-container {
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(212,175,55,0.3);
  height: 340px;
}
.map-container iframe {
  width: 100%;
  height: 100%;
  border: 0;
}

.contact-details {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 10px;
  padding: 36px;
}
.contact-details h2 {
  font-size: 1.5rem;
  color: #d4af37;
  margin-bottom: 24px;
}
.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 20px;
  padding-bottom: 18px;
  border-bottom: 1px solid rgba(212,175,55,0.1);
}
.contact-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
.contact-icon { font-size: 1.3rem; flex-shrink: 0; margin-top: 2px; }
.contact-label { color: #8a7a5a; font-size: 0.82rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
.contact-value {
  color: #f0e6d3;
  font-size: 1rem;
  line-height: 1.5;
}
.contact-value a { color: #d4af37; text-decoration: none; }
.contact-value a:hover { text-decoration: underline; }

.intro-text {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.2);
  border-radius: 10px;
  padding: 28px 36px;
  margin-bottom: 30px;
  text-align: center;
}
.intro-text p { color: #c8b89a; font-size: 1.1rem; line-height: 1.7; }

.location-box {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 10px;
  padding: 32px 36px;
  margin-bottom: 30px;
}
.location-box h3 { font-size: 1.3rem; color: #d4af37; margin-bottom: 16px; }
.location-box p { color: #c8b89a; line-height: 1.7; margin-bottom: 16px; }
.location-box .note { color: #8a7a5a; font-style: italic; font-size: 0.95rem; }

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
.btn-maps { background: #4285F4; color: #fff; }
.btn-maps:hover { background: #3574e2; transform: translateY(-2px); }

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
    <a href="/RSCinemaVilla/pricing/">Pricing</a>
    <a href="/RSCinemaVilla/reviews/">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/" class="active">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <p>Contact Us</p>
  </div>
</section>

<div class="section">
  <div class="intro-text">
    <p>For bookings and enquiries, reach us on <strong>Phone or WhatsApp &mdash; we respond quickly!</strong></p>
  </div>

  <div class="contact-grid">
    <div class="map-container">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3808.0!2d77.8700!3d17.3500!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTfCsDIxJzAwLjAiTiA3N8KwNTInMTIuMCJF!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="RS Cinema Villa Location"></iframe>
    </div>

    <div class="contact-details">
      <h2>&#128222; Get in Touch</h2>

      <div class="contact-item">
        <div class="contact-icon">&#128222;</div>
        <div>
          <div class="contact-label">Phone / WhatsApp</div>
          <div class="contact-value"><a href="tel:+919206845678">+91 92068 45678</a></div>
        </div>
      </div>

      <div class="contact-item">
        <div class="contact-icon">&#127760;</div>
        <div>
          <div class="contact-label">Email</div>
          <div class="contact-value"><a href="mailto:rscinemavilla@gmail.com">rscinemavilla@gmail.com</a></div>
        </div>
      </div>

      <div class="contact-item">
        <div class="contact-icon">&#128247;</div>
        <div>
          <div class="contact-label">Instagram</div>
          <div class="contact-value"><a href="https://www.instagram.com/rs_cinema_villa" target="_blank">@rs_cinema_villa</a></div>
        </div>
      </div>

      <div class="contact-item">
        <div class="contact-icon">&#128336;</div>
        <div>
          <div class="contact-label">Available</div>
          <div class="contact-value">Open 24/7</div>
        </div>
      </div>
    </div>
  </div>

  <div class="location-box">
    <h3>&#128205; Our Location</h3>
    <p>RS Cinema Villa, Moinabad, Hyderabad, Telangana &ndash; 501503, India</p>
    <p class="note">Peaceful surroundings, easily accessible from Hyderabad city center.</p>
    <a href="https://maps.google.com/?q=RS+Cinema+Villa+Moinabad+Hyderabad" class="btn btn-maps" target="_blank">&#128205; Get Directions on Google Maps</a>
  </div>

  <div class="cta-section">
    <h2>&#128197; Book Your Stay</h2>
    <p>Ready to create unforgettable memories? Contact us now to check availability and confirm your booking!</p>
    <div class="cta-buttons">
      <a href="https://wa.me/919206845678" class="btn btn-green" target="_blank">&#128172; WhatsApp Us</a>
      <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
      <a href="https://www.airbnb.com/rooms/rscinemavilla" class="btn btn-airbnb" target="_blank">&#127968; View on Airbnb</a>
    </div>
  </div>
</div>

<div class="footer-tagline">Your dream celebration is just one call away.</div>
