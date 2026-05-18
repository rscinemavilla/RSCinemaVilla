---
layout: default
title: RS Cinema Villa
---

<style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%;background:#000;color:#fff}
body{font-family:Arial,sans-serif;background:#000;color:#fff}

.site-header{position:sticky;top:0;z-index:1000;background:#202124;display:flex;align-items:center;justify-content:space-between;padding:0 24px;height:56px}
.brand{color:#fff;font-size:18px;font-weight:600;text-decoration:none}
.site-nav{display:flex;flex-wrap:wrap}
.site-nav a{color:#e8eaed;text-decoration:none;padding:0 14px;height:56px;line-height:56px;font-size:14px;font-weight:500}
.site-nav a:hover{background:rgba(255,255,255,0.1)}
.site-nav a.active{border-bottom:3px solid #fff;font-weight:700}

.hero{position:relative;width:100%;min-height:400px;background:url('/RSCinemaVilla/images/RScinemavilla1.JPG') center/cover no-repeat;display:flex;align-items:center;justify-content:center}
.hero::before{content:'';position:absolute;inset:0;background:rgba(0,0,0,0.45)}
.hero-box{position:relative;border:2px solid rgba(255,255,255,0.7);padding:40px 60px;text-align:center;color:#fff}
.hero-box h1{font-size:52px;font-weight:700;margin-bottom:12px}
.hero-box h2{font-size:26px;font-weight:400}

.intro-section{display:flex;align-items:flex-start;gap:40px;max-width:1100px;margin:48px auto;padding:0 32px}
.intro-img{width:42%;flex-shrink:0}
.intro-img img{width:100%;height:auto;display:block;border-radius:4px}
.intro-text{flex:1}
.intro-text p{font-size:15px;line-height:1.65;margin-bottom:12px}
.phone-line{font-weight:600}
.phone-line a{color:#4da3ff;text-decoration:underline}
.perfect-title{font-size:15px;font-weight:700;margin-bottom:12px}
.intro-text ul{list-style:none;padding:0;margin-bottom:20px}
.intro-text ul li{font-size:15px;margin-bottom:10px;padding-left:20px;position:relative}
.intro-text ul li::before{content:'\25AA';position:absolute;left:4px;color:#bbb}

.cta-row{display:flex;flex-wrap:wrap;align-items:center;gap:6px;font-size:15px;margin-bottom:16px}
.cta-row a{color:#4da3ff;text-decoration:underline;font-weight:500}
.sep{color:#777}
.follow-row{font-size:15px}
.follow-row a{color:#4da3ff;text-decoration:underline}

.footer-tagline{text-align:center;padding:32px 24px 48px;font-style:italic;color:#bbb;font-size:15px;border-top:1px solid #222;margin-top:24px}

@media(max-width:700px){
  .intro-section{flex-direction:column}
  .intro-img{width:100%}
  .hero-box h1{font-size:32px}
  .hero-box h2{font-size:18px}
  .hero-box{padding:24px 20px}
  .site-nav a{padding:0 8px;font-size:12px}
}
</style>

<header class="site-header">
  <a href="/RSCinemaVilla/" class="brand">RS Cinema Villa</a>
  <nav class="site-nav">
    <a href="/RSCinemaVilla/" class="active">Home</a>
    <a href="/RSCinemaVilla/gallery/">Gallery</a>
    <a href="/RSCinemaVilla/about-villa/">About Villa</a>
    <a href="/RSCinemaVilla/pricing/">Pricing</a>
    <a href="/RSCinemaVilla/reviews/">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <h2>Luxury Private Villa for Celebrations &amp; Events</h2>
  </div>
</section>

<section class="intro-section">
  <div class="intro-img">
    <img src="/RSCinemaVilla/images/RScinemavilla1.JPG" alt="RS Cinema Villa">
  </div>

  <div class="intro-text">
    <p><b>Welcome to RS Cinema Villa</b> &#127916;&#10024; A luxury private villa in the peaceful heart of Moinabad, Hyderabad &mdash; designed for privacy, celebration, and premium experiences.</p>

    <p class="phone-line">Phone / WhatsApp: <a href="https://wa.me/919206845678">+91 92068 45678</a></p>

    <p class="perfect-title">&#127881; <b>Perfect For:</b></p>
    <ul>
      <li>&#127874; Birthdays &amp; Celebrations</li>
      <li>&#128141; Engagements &amp; Pre-wedding Functions</li>
      <li>&#128106; Family Get-togethers &amp; Reunions</li>
      <li>&#127882; Private Parties &amp; Social Events</li>
      <li>&#127916; Movie &amp; Photo Shoots</li>
      <li>&#128188; Corporate Offsites</li>
      <li>&#127912; Customizable D&eacute;cor &amp; Music</li>
    </ul>

    <div class="cta-row">
      <span>&#128197;</span> <a href="https://calendly.com/rscinemavilla/booking">Book Now</a>
      <span class="sep">|</span>
      <span>&#128172;</span> <a href="https://wa.me/919206845678">WhatsApp Us</a>
      <span class="sep">|</span>
      <span>&#127968;</span> <a href="https://www.airbnb.co.in/rooms/1506244066053865421">View on Airbnb</a>
    </div>

    <div class="follow-row">
      &#128247; Follow us: <a href="https://www.instagram.com/rs_cinema_villa/">@rs_cinema_villa</a>
    </div>
  </div>
</section>

<div class="footer-tagline">Where every moment becomes a memory worth keeping.</div>
