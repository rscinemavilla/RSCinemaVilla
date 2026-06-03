---
layout: default
title: RS Cinema Villa
---
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap');

*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%;background:#faf9f7;color:#1a1a1a}
body{font-family:'Jost',sans-serif;background:#faf9f7;color:#1a1a1a}

/* ── NAV ── */
.site-header{position:sticky;top:0;z-index:1000;background:rgba(250,249,247,0.97);backdrop-filter:blur(12px);display:flex;align-items:center;justify-content:space-between;padding:0 40px;height:64px;border-bottom:1px solid rgba(0,0,0,0.08)}
.brand{color:#1a1a1a;font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600;letter-spacing:1px;text-decoration:none}
.site-nav{display:flex;gap:4px}
.site-nav a{color:#555;text-decoration:none;padding:0 14px;height:64px;line-height:64px;font-size:13px;font-weight:400;letter-spacing:0.5px;transition:color 0.2s}
.site-nav a:hover{color:#1a1a1a}
.site-nav a.active{color:#1a1a1a;font-weight:500;border-bottom:2px solid #c9a96e}
.nav-book-btn{background:#1a1a1a;color:#fff!important;padding:10px 22px!important;height:auto!important;line-height:normal!important;border-radius:3px;font-size:13px!important;letter-spacing:1px!important;transition:background 0.2s!important}
.nav-book-btn:hover{background:#333!important}

/* ── HERO ── */
.hero{position:relative;width:100%;height:92vh;min-height:600px;background:url('/RSCinemaVilla/images/RScinemavilla1.JPG') center/cover no-repeat;display:flex;align-items:flex-end;justify-content:flex-start;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,0.72) 0%,rgba(0,0,0,0.15) 60%,rgba(0,0,0,0.1) 100%)}
.hero-content{position:relative;padding:0 64px 72px;max-width:780px}
.hero-eyebrow{display:inline-block;color:#c9a96e;font-size:12px;font-weight:500;letter-spacing:3px;text-transform:uppercase;margin-bottom:20px;border-bottom:1px solid #c9a96e;padding-bottom:8px}
.hero-content h1{font-family:'Cormorant Garamond',serif;font-size:clamp(3rem,6vw,5.5rem);font-weight:300;color:#fff;line-height:1.05;margin-bottom:20px;letter-spacing:1px}
.hero-content h1 em{font-style:italic;color:#e8d5b0}
.hero-content p{font-size:1.05rem;color:rgba(255,255,255,0.82);font-weight:300;line-height:1.7;max-width:520px;margin-bottom:36px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.btn-hero-primary{background:#c9a96e;color:#fff;padding:14px 32px;font-size:13px;font-weight:500;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:2px;transition:background 0.2s}
.btn-hero-primary:hover{background:#b8914f}
.btn-hero-outline{border:1px solid rgba(255,255,255,0.6);color:#fff;padding:13px 28px;font-size:13px;letter-spacing:1px;text-decoration:none;border-radius:2px;transition:all 0.2s}
.btn-hero-outline:hover{background:rgba(255,255,255,0.12)}
.hero-scroll{position:absolute;bottom:32px;right:40px;color:rgba(255,255,255,0.5);font-size:11px;letter-spacing:2px;text-transform:uppercase;display:flex;align-items:center;gap:8px}
.hero-scroll::after{content:'';width:40px;height:1px;background:rgba(255,255,255,0.4)}

/* ── STATS BAR ── */
.stats-bar{background:#fff;border-bottom:1px solid rgba(0,0,0,0.07);padding:24px 64px;display:flex;justify-content:center;gap:64px;flex-wrap:wrap}
.stat-item{text-align:center}
.stat-number{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:400;color:#1a1a1a;line-height:1}
.stat-label{font-size:11px;color:#888;letter-spacing:1.5px;text-transform:uppercase;margin-top:4px}

/* ── SECTION SHARED ── */
.section-pad{padding:96px 64px;max-width:1200px;margin:0 auto}
.section-eyebrow{font-size:11px;font-weight:500;letter-spacing:3px;text-transform:uppercase;color:#c9a96e;margin-bottom:16px}
.section-title{font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,3.2rem);font-weight:300;color:#1a1a1a;line-height:1.15;margin-bottom:24px}
.section-title em{font-style:italic}
.section-body{font-size:1rem;color:#555;line-height:1.85;font-weight:300}
.divider{width:48px;height:1px;background:#c9a96e;margin:24px 0}

/* ── INTRO SPLIT ── */
.intro-split{display:grid;grid-template-columns:1fr 1fr;gap:0;background:#fff;border:1px solid rgba(0,0,0,0.07)}
.intro-img-col img{width:100%;height:100%;object-fit:cover;display:block;min-height:500px}
.intro-text-col{padding:72px 56px;display:flex;flex-direction:column;justify-content:center}
.phone-badge{display:inline-flex;align-items:center;gap:10px;background:#f0ebe1;padding:14px 20px;border-radius:2px;margin-top:28px;text-decoration:none;transition:background 0.2s}
.phone-badge:hover{background:#e8dfd2}
.phone-badge span{font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#1a1a1a;font-weight:600}
.phone-badge small{font-size:11px;color:#888;letter-spacing:1px;text-transform:uppercase;display:block}

/* ── PERFECT FOR (OCCASIONS) ── */
.occasions-section{background:#faf9f7;padding:96px 64px}
.occasions-inner{max-width:1200px;margin:0 auto}
.occasions-header{text-align:center;margin-bottom:64px}
.occasions-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px}
.occasion-card{background:#fff;padding:48px 36px;position:relative;overflow:hidden;transition:transform 0.3s}
.occasion-card:hover{transform:translateY(-4px)}
.occasion-card::before{content:'';position:absolute;top:0;left:0;width:3px;height:0;background:#c9a96e;transition:height 0.3s}
.occasion-card:hover::before{height:100%}
.occasion-icon{font-size:2rem;margin-bottom:20px;display:block}
.occasion-title{font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:400;color:#1a1a1a;margin-bottom:12px}
.occasion-desc{font-size:0.9rem;color:#777;line-height:1.7;font-weight:300}

/* ── FEATURE SHOWCASE ── */
.feature-showcase{background:#1a1a1a;padding:96px 64px}
.feature-showcase-inner{max-width:1200px;margin:0 auto}
.feature-showcase .section-eyebrow{color:#c9a96e}
.feature-showcase .section-title{color:#fff}
.feature-showcase .section-body{color:rgba(255,255,255,0.65)}
.feature-showcase .divider{background:#c9a96e}
.features-split{display:grid;grid-template-columns:1fr 1fr;gap:48px;margin-top:56px}
.feature-list{list-style:none}
.feature-list li{display:flex;gap:16px;padding:20px 0;border-bottom:1px solid rgba(255,255,255,0.08);align-items:flex-start}
.feature-list li:last-child{border-bottom:none}
.feat-icon{font-size:1.3rem;flex-shrink:0;margin-top:2px}
.feat-text strong{display:block;color:#fff;font-size:0.95rem;font-weight:500;margin-bottom:4px}
.feat-text span{color:rgba(255,255,255,0.55);font-size:0.85rem;font-weight:300}

/* ── WHY CHOOSE US ── */
.why-section{background:#fff;padding:96px 64px}
.why-section-inner{max-width:1200px;margin:0 auto}
.why-grid{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center;margin-top:56px}
.why-img img{width:100%;height:480px;object-fit:cover;display:block}
.why-points{display:flex;flex-direction:column;gap:32px}
.why-point{display:flex;gap:20px;align-items:flex-start}
.why-num{font-family:'Cormorant Garamond',serif;font-size:3rem;font-weight:300;color:#f0ebe1;line-height:1;flex-shrink:0;width:48px}
.why-point-text strong{display:block;color:#1a1a1a;font-size:1rem;font-weight:500;margin-bottom:6px}
.why-point-text p{color:#777;font-size:0.9rem;line-height:1.65;font-weight:300}

/* ── TESTIMONIAL ── */
.testimonial-section{background:#f0ebe1;padding:96px 64px}
.testimonial-inner{max-width:900px;margin:0 auto;text-align:center}
.testimonial-stars{color:#c9a96e;font-size:1.1rem;letter-spacing:4px;margin-bottom:32px}
.testimonial-quote{font-family:'Cormorant Garamond',serif;font-size:clamp(1.4rem,3vw,2rem);font-weight:300;color:#1a1a1a;line-height:1.6;font-style:italic;margin-bottom:32px}
.testimonial-author{font-size:12px;letter-spacing:2px;text-transform:uppercase;color:#888}
.rating-badge{display:inline-flex;align-items:center;gap:12px;background:#fff;padding:16px 28px;border-radius:2px;margin-top:48px}
.rating-badge .score{font-family:'Cormorant Garamond',serif;font-size:2.5rem;font-weight:400;color:#1a1a1a}
.rating-badge .label{text-align:left}
.rating-badge .label strong{display:block;font-size:0.9rem;color:#1a1a1a}
.rating-badge .label small{font-size:11px;color:#888;letter-spacing:1px}

/* ── CTA BAND ── */
.cta-band{background:#1a1a1a;padding:80px 64px;text-align:center}
.cta-band .section-eyebrow{color:#c9a96e}
.cta-band h2{font-family:'Cormorant Garamond',serif;font-size:clamp(2rem,4vw,3rem);font-weight:300;color:#fff;margin:16px 0 12px}
.cta-band p{color:rgba(255,255,255,0.6);font-size:1rem;font-weight:300;margin-bottom:40px}
.cta-band-phone{font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:400;color:#c9a96e;margin-bottom:40px;display:block}
.cta-band-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn-cta-gold{background:#c9a96e;color:#fff;padding:15px 36px;font-size:13px;font-weight:500;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-radius:2px;transition:background 0.2s}
.btn-cta-gold:hover{background:#b8914f}
.btn-cta-wa{background:#25D366;color:#fff;padding:15px 36px;font-size:13px;font-weight:500;letter-spacing:1px;text-decoration:none;border-radius:2px;transition:background 0.2s}
.btn-cta-wa:hover{background:#1ebe57}
.btn-cta-outline{border:1px solid rgba(255,255,255,0.3);color:#fff;padding:14px 28px;font-size:13px;letter-spacing:1px;text-decoration:none;border-radius:2px;transition:all 0.2s}
.btn-cta-outline:hover{border-color:rgba(255,255,255,0.7)}

/* ── FOOTER ── */
.site-footer{background:#111;padding:40px 64px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.footer-brand{font-family:'Cormorant Garamond',serif;color:#c9a96e;font-size:18px;letter-spacing:1px}
.footer-tagline{color:rgba(255,255,255,0.35);font-size:12px;letter-spacing:1.5px;text-transform:uppercase;font-style:italic}
.footer-links a{color:rgba(255,255,255,0.4);font-size:12px;margin-left:20px;text-decoration:none;letter-spacing:0.5px;transition:color 0.2s}
.footer-links a:hover{color:#c9a96e}

@media(max-width:900px){
.site-header{padding:0 20px}
.hero-content{padding:0 24px 48px}
.section-pad,.occasions-section,.feature-showcase,.why-section,.testimonial-section,.cta-band{padding:64px 24px}
.stats-bar{padding:20px 24px;gap:32px}
.intro-split{grid-template-columns:1fr}
.intro-img-col img{min-height:280px}
.intro-text-col{padding:48px 32px}
.occasions-grid{grid-template-columns:1fr 1fr}
.features-split{grid-template-columns:1fr}
.why-grid{grid-template-columns:1fr}
.site-footer{padding:32px 24px;flex-direction:column;text-align:center}
.footer-links a{margin:0 10px}
.nav-book-btn{display:none}
}
@media(max-width:600px){
.occasions-grid{grid-template-columns:1fr}
.hero{height:80vh}
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
    <a href="/RSCinemaVilla/booking-enquiry-form/" class="nav-book-btn">Enquire Now</a>
    <a href="https://wa.me/919206845678" class="nav-book-btn" target="_blank">WhatsApp/a>
  </nav>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-content">
    <span class="hero-eyebrow">Moinabad &middot; Hyderabad</span>
    <h1>Luxury Private Villa for Celebrations & Events</h1>
    <p>Hyderabad&rsquo;s most exclusive private villa &mdash; with a cinema room, private pool, and lush open lawns. Entirely yours. Completely private. Utterly unforgettable.</p>
    <div class="hero-cta">
      <a href="https://wa.me/919206845678" class="btn-hero-primary" target="_blank">WhatsApp to Book</a>
      <a href="/RSCinemaVilla/about-villa/" class="btn-hero-outline">Explore the Villa</a>
    </div>
  </div>
  <span class="hero-scroll">Scroll to discover</span>
</section>

<!-- STATS BAR -->
<div class="stats-bar">
  <div class="stat-item"><div class="stat-number">5.0</div><div class="stat-label">Google Rating</div></div>
  <div class="stat-item"><div class="stat-number">5</div><div class="stat-label">AC Bedrooms</div></div>
  <div class="stat-item"><div class="stat-number">24/7</div><div class="stat-label">Dedicated Support</div></div>
  <div class="stat-item"><div class="stat-number">100%</div><div class="stat-label">Private &amp; Exclusive</div></div>
</div>

<!-- INTRO SPLIT -->
<div class="section-pad" style="padding-top:80px;padding-bottom:0">
  <div class="intro-split">
    <div class="intro-img-col">
      <img src="/RSCinemaVilla/images/RScinemavilla1.JPG" alt="RS Cinema Villa exterior with private pool">
    </div>
    <div class="intro-text-col">
      <p class="section-eyebrow">Welcome</p>
      <h2 class="section-title">More than a villa &mdash;<br><em>an experience</em></h2>
      <div class="divider"></div>
      <p class="section-body">RS Cinema Villa is a luxury private villa nestled in the peaceful greenery of Moinabad, Hyderabad &mdash; designed for those who seek complete privacy, world-class comfort, and celebrations that are truly unforgettable.</p>
      <p class="section-body" style="margin-top:16px">Whether it&rsquo;s a birthday, an anniversary, a private party, a family reunion, or a film shoot &mdash; every moment here feels extraordinary. The entire villa is reserved exclusively for you and your guests.</p>
      <a href="tel:+919206845678" class="phone-badge" style="max-width:fit-content">
        <small>Phone / WhatsApp</small>
        <span>+91 9206845678</span>
      </a>
    </div>
  </div>
</div>

<!-- PERFECT FOR / OCCASIONS -->
<section class="occasions-section">
  <div class="occasions-inner">
    <div class="occasions-header">
      <p class="section-eyebrow">Crafted for</p>
      <h2 class="section-title">Your most special<br><em>moments</em></h2>
      <div class="divider" style="margin:24px auto"></div>
    </div>
    <div class="occasions-grid">
      <div class="occasion-card">
        <span class="occasion-icon">&#127874;</span>
        <div class="occasion-title">Birthdays &amp; Celebrations</div>
        <p class="occasion-desc">Mark another year in grand style. Celebrate by the pool, set up your dream d&eacute;cor, and party the night away in complete privacy. RS Cinema Villa is Hyderabad&rsquo;s finest private birthday venue.</p>
      </div>
      <div class="occasion-card">
        <span class="occasion-icon">&#128141;</span>
        <div class="occasion-title">Anniversaries &amp; Romantic Escapes</div>
        <p class="occasion-desc">A private pool, candle-lit lawns, a cinema room for two &mdash; give your partner an anniversary they will talk about forever. The perfect luxury couple staycation near Hyderabad.</p>
      </div>
      <div class="occasion-card">
        <span class="occasion-icon">&#128106;</span>
        <div class="occasion-title">Family Gatherings &amp; Reunions</div>
        <p class="occasion-desc">Five spacious bedrooms, an open lawn, and a fully equipped kitchen. RS Cinema Villa gives your whole family the space and privacy to truly enjoy each other&rsquo;s company.</p>
      </div>
      <div class="occasion-card">
        <span class="occasion-icon">&#127882;</span>
        <div class="occasion-title">Private Parties &amp; Social Events</div>
        <p class="occasion-desc">Host your guests in a setting that impresses. Open lawns, a glittering pool, and premium interiors create the perfect atmosphere for any private party or social gathering in Hyderabad.</p>
      </div>
      <div class="occasion-card">
        <span class="occasion-icon">&#127916;</span>
        <div class="occasion-title">Film Shoots &amp; Photo Sessions</div>
        <p class="occasion-desc">Elegant architecture, diverse backdrops, and complete privacy make RS Cinema Villa a top choice for music videos, short films, fashion shoots, and pre-wedding photography near Hyderabad.</p>
      </div>
      <div class="occasion-card">
        <span class="occasion-icon">&#128188;</span>
        <div class="occasion-title">Corporate Offsites &amp; Events</div>
        <p class="occasion-desc">A premium and productive setting away from the city. Perfect for leadership offsites, team retreats, small corporate meetings, and client entertainment in a private, exclusive environment.</p>
      </div>
    </div>
  </div>
</section>

<!-- AMENITIES FEATURE SHOWCASE -->
<section class="feature-showcase">
  <div class="feature-showcase-inner">
    <p class="section-eyebrow">Amenities &amp; Features</p>
    <h2 class="section-title" style="color:#fff">Every comfort.<br><em style="color:#e8d5b0">Every detail. All yours.</em></h2>
    <div class="divider"></div>
    <p class="section-body" style="max-width:600px">RS Cinema Villa is designed to impress. From the private cinema to the sparkling pool &mdash; every amenity is curated for a premium, exclusive experience.</p>
    <div class="features-split">
      <ul class="feature-list">
        <li><span class="feat-icon">&#127968;</span><div class="feat-text"><strong>5 Spacious AC Bedrooms</strong><span>Plush premium linens, stylish interiors &amp; individual climate control</span></div></li>
        <li><span class="feat-icon">&#127946;</span><div class="feat-text"><strong>Private Swimming Pool</strong><span>Your personal oasis &mdash; exclusively available throughout your stay</span></div></li>
        <li><span class="feat-icon">&#127916;</span><div class="feat-text"><strong>Private Cinema Room</strong><span>Large screen, projector &amp; surround sound for unforgettable movie nights</span></div></li>
        <li><span class="feat-icon">&#9832;</span><div class="feat-text"><strong>Hot Tub / Jacuzzi</strong><span>Unwind and relax after celebrations in a private hot tub</span></div></li>
      </ul>
      <ul class="feature-list">
        <li><span class="feat-icon">&#127807;</span><div class="feat-text"><strong>Manicured Open Lawns</strong><span>Perfect for outdoor events, ceremonies &amp; golden-hour photography</span></div></li>
        <li><span class="feat-icon">&#127859;</span><div class="feat-text"><strong>Fully Equipped Kitchen</strong><span>Modern kitchen stocked for self-catering or private chef arrangements</span></div></li>
        <li><span class="feat-icon">&#128225;</span><div class="feat-text"><strong>High-Speed Wi-Fi</strong><span>Seamless connectivity across the entire property</span></div></li>
        <li><span class="feat-icon">&#128274;</span><div class="feat-text"><strong>24/7 Dedicated Support</strong><span>Our on-site team is always available for a smooth, worry-free stay</span></div></li>
      </ul>
    </div>
  </div>
</section>

<!-- WHY CHOOSE US -->
<section class="why-section">
  <div class="why-section-inner">
    <p class="section-eyebrow">Why RS Cinema Villa</p>
    <div class="why-grid">
      <div class="why-img">
        <img src="/RSCinemaVilla/images/RScinemavilla1.JPG" alt="RS Cinema Villa private pool and lawns">
      </div>
      <div>
        <h2 class="section-title">What sets us <em>apart</em></h2>
        <div class="divider"></div>
        <div class="why-points">
          <div class="why-point"><div class="why-num">01</div><div class="why-point-text"><strong>Complete Privacy</strong><p>The entire villa is yours alone. No shared spaces, no other guests &mdash; just you, your people, and total exclusivity.</p></div></div>
          <div class="why-point"><div class="why-num">02</div><div class="why-point-text"><strong>The Cinema Experience</strong><p>No other villa near Hyderabad offers a private cinema room. Perfect for movie nights, sports screenings, and presentations.</p></div></div>
          <div class="why-point"><div class="why-num">03</div><div class="why-point-text"><strong>Serene Moinabad Setting</strong><p>Peaceful countryside just 30 minutes from Hyderabad city &mdash; a true escape from the hustle, without being far away.</p></div></div>
          <div class="why-point"><div class="why-num">04</div><div class="why-point-text"><strong>Customizable for Every Event</strong><p>From d&eacute;cor setup to music arrangements, our team helps you design the perfect experience for your occasion.</p></div></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIAL -->
<section class="testimonial-section">
  <div class="testimonial-inner">
    <p class="section-eyebrow">What our guests say</p>
    <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
    <p class="testimonial-quote">&ldquo;The villa is stunning, private, and has everything you need for a memorable experience. The perfect choice for a romantic staycation. Highly recommended!&rdquo;</p>
    <p class="testimonial-author">&mdash; Radhika C. &middot; Google Review</p>
    <div class="rating-badge">
      <div class="score">5.0</div>
      <div class="label">
        <strong>&#9733;&#9733;&#9733;&#9733;&#9733; Perfect Rating</strong>
        <small>Based on 11+ Google Reviews</small>
      </div>
    </div>
    <div style="margin-top:36px">
      <a href="/RSCinemaVilla/reviews/" style="font-size:13px;color:#888;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;border-bottom:1px solid #bbb;padding-bottom:3px">Read all guest stories &rarr;</a>
    </div>
  </div>
</section>

<!-- CTA BAND -->
<section class="cta-band">
  <p class="section-eyebrow">Ready to book?</p>
  <h2>Your dream stay<br><em style="color:#e8d5b0;font-style:italic">begins with one call</em></h2>
  <p>Check availability, get a custom quote, and secure your dates &mdash; all in minutes.</p>
  <a href="tel:+919206845678" class="cta-band-phone">+91 9206845678</a>
  <div class="cta-band-btns">
    <a href="https://wa.me/919206845678" class="btn-cta-wa" target="_blank">&#128172; WhatsApp Us Now</a>
    <a href="https://calendly.com/rscinemavilla/booking" class="btn-cta-gold" target="_blank">&#128197; Book Online</a>
    <a href="https://www.airbnb.co.in/rooms/1506244066053865421" class="btn-cta-outline" target="_blank">&#127968; View on Airbnb</a>
  </div>
</section>

<!-- FOOTER -->
<footer class="site-footer">
  <div class="footer-brand">RS Cinema Villa</div>
  <div class="footer-tagline">Yours alone. Entirely private. Utterly unforgettable.</div>
  <div class="footer-links">
    <a href="https://www.instagram.com/rs_cinema_villa/" target="_blank">Instagram</a>
    <a href="mailto:rscinemavilla@gmail.com">Email</a>
    <a href="/RSCinemaVilla/contact/">Contact</a>
  </div>
</footer>
