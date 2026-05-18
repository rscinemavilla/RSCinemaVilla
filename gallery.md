---
layout: default
title: Gallery
permalink: /gallery/
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
  background: url('/RSCinemaVilla/images/RScinemavilla1.JPG') center/cover no-repeat;
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

.section { padding: 60px 40px; max-width: 1200px; margin: 0 auto; }
.section-title {
  text-align: center;
  font-size: 2rem;
  color: #d4af37;
  margin-bottom: 40px;
  letter-spacing: 2px;
}

.photo-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 60px;
}
.photo-grid img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 6px;
  transition: transform 0.3s, box-shadow 0.3s;
  border: 1px solid rgba(212,175,55,0.2);
}
.photo-grid img:hover {
  transform: scale(1.04);
  box-shadow: 0 8px 32px rgba(212,175,55,0.3);
}

.video-section {
  text-align: center;
  margin-bottom: 60px;
}
.video-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  margin-top: 30px;
}
.video-wrapper {
  position: relative;
  padding-bottom: 56.25%;
  height: 0;
  overflow: hidden;
  border-radius: 10px;
  border: 1px solid rgba(212,175,55,0.3);
}
.video-wrapper iframe {
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 100%;
}

.cta-section {
  background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 12px;
  padding: 50px 40px;
  text-align: center;
  margin-bottom: 40px;
}
.cta-section h2 {
  font-size: 1.7rem;
  color: #d4af37;
  margin-bottom: 14px;
}
.cta-section p {
  color: #c8b89a;
  margin-bottom: 30px;
  font-size: 1.05rem;
}
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
.btn-gold {
  background: #d4af37;
  color: #0a0a0a;
}
.btn-gold:hover { background: #e6c84a; transform: translateY(-2px); }
.btn-outline {
  border: 2px solid #d4af37;
  color: #d4af37;
  background: transparent;
}
.btn-outline:hover { background: rgba(212,175,55,0.1); transform: translateY(-2px); }
.btn-green {
  background: #25D366;
  color: #fff;
}
.btn-green:hover { background: #1ebe57; transform: translateY(-2px); }

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
    <a href="/RSCinemaVilla/gallery/" class="active">Gallery</a>
    <a href="/RSCinemaVilla/about-villa/">About Villa</a>
    <a href="/RSCinemaVilla/pricing/">Pricing</a>
    <a href="/RSCinemaVilla/reviews/">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <p>Step inside RS Cinema Villa &mdash; where every corner is picture perfect.</p>
  </div>
</section>

<div class="section">
  <h2 class="section-title">&#127880; Photo Gallery</h2>

  <div class="photo-grid">
    <img src="/RSCinemaVilla/images/RScinemavilla1.JPG" alt="RS Cinema Villa 1" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla2.JPG" alt="RS Cinema Villa 2" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla3.JPG" alt="RS Cinema Villa 3" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla4.JPG" alt="RS Cinema Villa 4" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla5.JPG" alt="RS Cinema Villa 5" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla6.JPG" alt="RS Cinema Villa 6" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla7.JPG" alt="RS Cinema Villa 7" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla8.JPG" alt="RS Cinema Villa 8" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla9.JPG" alt="RS Cinema Villa 9" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla10.JPG" alt="RS Cinema Villa 10" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla11.JPG" alt="RS Cinema Villa 11" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla12.JPG" alt="RS Cinema Villa 12" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla13.JPG" alt="RS Cinema Villa 13" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla14.JPG" alt="RS Cinema Villa 14" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla15.JPG" alt="RS Cinema Villa 15" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla16.JPG" alt="RS Cinema Villa 16" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla17.JPG" alt="RS Cinema Villa 17" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla18.JPG" alt="RS Cinema Villa 18" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla19.JPG" alt="RS Cinema Villa 19" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla20.JPG" alt="RS Cinema Villa 20" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla21.JPG" alt="RS Cinema Villa 21" loading="lazy">
    <img src="/RSCinemaVilla/images/RScinemavilla22.JPG" alt="RS Cinema Villa 22" loading="lazy">
  </div>

  <div class="video-section">
  <h2 class="section-title">&#127916; Video Tour</h2>
  <div class="video-grid">
    <div class="video-wrapper">
      <iframe
        src="https://www.youtube.com/embed/oNUwoxu3glc?start=1"
        title="RS Cinema Villa Luxury Villa"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>

    <div class="video-wrapper">
      <iframe
        src="https://www.youtube.com/embed/V5tWUCpOVVk"
        title="Perfect Venue for Parties"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>
</div>


  <div class="cta-section">
    <h2>Love what you see?</h2>
    <p>Book RS Cinema Villa for your next celebration!</p>
    <div class="cta-buttons">
      <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
      <a href="https://wa.me/919206845678" class="btn btn-green" target="_blank">&#128172; WhatsApp Us</a>
      <a href="https://www.instagram.com/rs_cinema_villa" class="btn btn-outline" target="_blank">&#128247; Follow us @rs_cinema_villa</a>
    </div>
  </div>
</div>

<div class="footer-tagline">Every photo tells a story &mdash; make yours at RS Cinema Villa.</div>
