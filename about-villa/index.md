---
layout: default
title: About Villa
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
  transition: color 0.2s;
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
  background: url('/RSCinemaVilla/images/RScinemavilla3.JPG') center/cover no-repeat;
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
.section-title {
  font-size: 1.7rem;
  color: #d4af37;
  margin-bottom: 24px;
  letter-spacing: 1px;
}

.intro-block {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 10px;
  padding: 36px 40px;
  margin-bottom: 40px;
}
.intro-block p {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #c8b89a;
  margin-bottom: 16px;
}
.intro-block .phone {
  font-size: 1.2rem;
  color: #d4af37;
  font-weight: bold;
}

.features-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-bottom: 50px;
}
.feature-card {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.25);
  border-radius: 10px;
  padding: 32px 36px;
}
.feature-card h3 {
  font-size: 1.4rem;
  color: #d4af37;
  margin-bottom: 20px;
}
.feature-card ul {
  list-style: none;
  padding: 0;
}
.feature-card ul li {
  color: #c8b89a;
  font-size: 1rem;
  line-height: 1.7;
  padding: 6px 0;
  border-bottom: 1px solid rgba(212,175,55,0.1);
}
.feature-card ul li:last-child { border-bottom: none; }

.cta-section {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 12px;
  padding: 50px 40px;
  text-align: center;
  margin-bottom: 40px;
}
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
  letter-spacing: 0.5px;
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
    <a href="/RSCinemaVilla/about-villa/" class="active">About Villa</a>
    <a href="/RSCinemaVilla/pricing/">Pricing</a>
    <a href="/RSCinemaVilla/reviews/">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <p>Luxury Private Villa for Events, Parties &amp; Movie Shoots</p>
  </div>
</section>

<div class="section">
  <div class="intro-block">
    <p>RS Cinema Villa is a <strong>premium luxury private villa</strong> nestled in the peaceful greenery of <strong>Moinabad, Hyderabad</strong> &mdash; designed for those who seek comfort, exclusivity, and unforgettable experiences.</p>
    <p>Whether you are planning a birthday celebration, family gathering, pre-wedding shoot, corporate event, or a movie shoot &mdash; RS Cinema Villa offers the perfect backdrop and world-class amenities to make your occasion truly special.</p>
    <p class="phone">&#128222; Phone / WhatsApp: <a href="tel:+919206845678" style="color:#d4af37;">+91 92068 45678</a></p>
  </div>

  <div class="features-grid">
    <div class="feature-card">
      <h3>&#127969; Our Space</h3>
      <ul>
        <li>&#127968; 5 spacious AC bedrooms with premium linens</li>
        <li>&#127946; Private swimming pool &mdash; your personal oasis</li>
        <li>&#127807; Manicured lawns &mdash; perfect for outdoor celebrations</li>
        <li>&#127859; Fully-equipped modern kitchen</li>
        <li>&#9832; Hot tub for relaxing evenings</li>
        <li>&#128225; High-speed Wi-Fi throughout</li>
        <li>&#128274; 24-hour front desk support</li>
        <li>&#127916; Private cinema &amp; entertainment room</li>
      </ul>
    </div>

    <div class="feature-card">
      <h3>&#127881; What We Offer</h3>
      <ul>
        <li>&#127882; Full event management &amp; hosting support</li>
        <li>&#127916; Cinema room with projector &amp; surround sound</li>
        <li>&#127800; Custom d&eacute;cor &amp; theming for all occasions</li>
        <li>&#127381; Professional photography-ready spaces</li>
      </ul>
      <br>
      <h3>&#10024; What Makes Us Special</h3>
      <ul>
        <li>&#127775; Complete privacy &mdash; exclusively yours for your event</li>
        <li>&#127968; Premium interiors with luxury finishes throughout</li>
        <li>&#127807; Serene natural surroundings in Moinabad</li>
        <li>&#128081; Dedicated support team for a seamless experience</li>
      </ul>
    </div>
  </div>

  <div class="cta-section">
    <p>Ready to experience luxury at its finest? Book RS Cinema Villa for your next celebration!</p>
    <div class="cta-buttons">
      <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
      <a href="https://wa.me/919206845678" class="btn btn-green" target="_blank">&#128172; WhatsApp Us</a>
      <a href="https://www.airbnb.co.in/rooms/1506244066053865421" class="btn btn-airbnb" target="_blank">&#127968; View on Airbnb</a>
      <a href="https://www.instagram.com/rs_cinema_villa" class="btn btn-outline" target="_blank">&#128247; Follow us @rs_cinema_villa</a>
    </div>
  </div>
</div>

<div class="footer-tagline">More than a villa &mdash; it&rsquo;s an experience you&rsquo;ll never forget.</div>
