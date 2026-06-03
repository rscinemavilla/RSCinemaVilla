---
layout: default
title: Contact & Book Now
permalink: /contact/
---
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap');

*{box-sizing:border-box;margin:0;padding:0}
html,body{min-height:100%;background:#faf9f7;color:#1a1a1a}
body{font-family:'Jost',sans-serif;background:#faf9f7;color:#1a1a1a}

.site-header{position:sticky;top:0;z-index:1000;background:rgba(250,249,247,0.97);backdrop-filter:blur(12px);display:flex;align-items:center;justify-content:space-between;padding:0 40px;height:64px;border-bottom:1px solid rgba(0,0,0,0.08)}
.brand{color:#1a1a1a;font-family:'Cormorant Garamond',serif;font-size:20px;font-weight:600;letter-spacing:1px;text-decoration:none}
.site-nav{display:flex;gap:4px}
.site-nav a{color:#555;text-decoration:none;padding:0 14px;height:64px;line-height:64px;font-size:13px;font-weight:400;letter-spacing:0.5px;transition:color 0.2s}
.site-nav a:hover{color:#1a1a1a}
.site-nav a.active{color:#1a1a1a;font-weight:500;border-bottom:2px solid #c9a96e}
.nav-book-btn{background:#1a1a1a;color:#fff!important;padding:10px 22px!important;height:auto!important;line-height:normal!important;border-radius:3px;font-size:13px!important;letter-spacing:1px!important;transition:background 0.2s!important}
.nav-book-btn:hover{background:#333!important}

.hero{position:relative;width:100%;height:55vh;min-height:380px;background:url('/RSCinemaVilla/images/RScinemavilla2.JPG') center/cover no-repeat;display:flex;align-items:flex-end;justify-content:flex-start;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,0.75) 0%,rgba(0,0,0,0.15) 70%,transparent 100%)}
.hero-content{position:relative;padding:0 64px 56px;max-width:700px}
.hero-eyebrow{display:inline-block;color:#c9a96e;font-size:11px;font-weight:500;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px}
.hero-content h1{font-family:'Cormorant Garamond',serif;font-size:clamp(2.2rem,4.5vw,4rem);font-weight:300;color:#fff;line-height:1.1;margin-bottom:14px}
.hero-content h1 em{font-style:italic;color:#e8d5b0}
.hero-content p{font-size:0.95rem;color:rgba(255,255,255,0.75);font-weight:300;line-height:1.7}

.section-eyebrow{font-size:11px;font-weight:500;letter-spacing:3px;text-transform:uppercase;color:#c9a96e;margin-bottom:14px}
.section-title{font-family:'Cormorant Garamond',serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:300;color:#1a1a1a;line-height:1.2;margin-bottom:20px}
.section-title em{font-style:italic}
.divider{width:48px;height:1px;background:#c9a96e;margin:20px 0 24px}
.body-text{font-size:1rem;color:#555;line-height:1.85;font-weight:300}

/* CONTACT INTRO */
.contact-intro{background:#fff;padding:64px;text-align:center;border-bottom:1px solid rgba(0,0,0,0.07)}
.contact-intro-inner{max-width:700px;margin:0 auto}

/* CONTACT GRID */
.contact-main{background:#faf9f7;padding:96px 64px}
.contact-main-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start}
.contact-details-box{background:#fff;padding:48px;border-top:3px solid #c9a96e}
.contact-details-box h2{font-family:'Cormorant Garamond',serif;font-size:1.8rem;color:#1a1a1a;margin-bottom:32px;font-weight:400}
.contact-item{display:flex;align-items:flex-start;gap:16px;padding:20px 0;border-bottom:1px solid rgba(0,0,0,0.06)}
.contact-item:last-child{border-bottom:none}
.c-icon{font-size:1.2rem;flex-shrink:0;margin-top:3px;color:#c9a96e}
.c-label{font-size:11px;color:#aaa;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:5px}
.c-value{color:#1a1a1a;font-size:1rem;font-weight:400;line-height:1.5}
.c-value a{color:#1a1a1a;text-decoration:none;transition:color 0.2s}
.c-value a:hover{color:#c9a96e}
.c-value .phone-link{font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-weight:600;color:#c9a96e}
.c-value .phone-link:hover{color:#b8914f}
.wa-btn{display:block;background:#25D366;color:#fff;text-align:center;padding:16px;border-radius:2px;text-decoration:none;font-size:14px;font-weight:500;letter-spacing:0.5px;margin-top:28px;transition:background 0.2s}
.wa-btn:hover{background:#1ebe57}

.map-box{border-radius:2px;overflow:hidden;border:1px solid rgba(0,0,0,0.07)}
.map-box iframe{width:100%;height:340px;display:block;border:none}
.map-info{background:#fff;padding:28px 32px}
.map-address{font-size:0.95rem;color:#555;line-height:1.6;margin-bottom:16px}
.map-link{display:inline-flex;align-items:center;gap:8px;color:#c9a96e;font-size:13px;letter-spacing:0.5px;text-decoration:none;font-weight:500;border-bottom:1px solid #c9a96e;padding-bottom:2px;transition:color 0.2s}
.map-link:hover{color:#b8914f;border-bottom-color:#b8914f}

/* HOW TO BOOK */
.book-section{background:#1a1a1a;padding:96px 64px}
.book-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.book-section .section-title{color:#fff}
.book-section .divider{background:#c9a96e}
.book-section .body-text{color:rgba(255,255,255,0.55)}
.book-steps{margin-top:40px;display:flex;flex-direction:column;gap:24px}
.book-step{display:flex;gap:20px;align-items:flex-start;padding:24px;background:rgba(255,255,255,0.04);border-left:3px solid rgba(201,169,110,0.4)}
.step-num{font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:300;color:#c9a96e;line-height:1;flex-shrink:0;width:36px}
.step-text strong{display:block;color:#fff;font-size:0.95rem;font-weight:500;margin-bottom:4px}
.step-text span{color:rgba(255,255,255,0.4);font-size:0.85rem;font-weight:300}
.book-cta{background:rgba(255,255,255,0.04);border:1px solid rgba(201,169,110,0.3);padding:48px 40px;border-radius:2px;text-align:center}
.book-cta p{color:rgba(255,255,255,0.5);font-size:0.9rem;margin-bottom:16px}
.book-phone{font-family:'Cormorant Garamond',serif;font-size:2.2rem;font-weight:400;color:#c9a96e;display:block;text-decoration:none;margin-bottom:28px}
.cta-btns{display:flex;flex-direction:column;gap:12px}
.btn{display:inline-block;padding:14px 32px;font-size:13px;font-weight:500;letter-spacing:1px;text-decoration:none;border-radius:2px;transition:all 0.2s;text-align:center}
.btn-gold{background:#c9a96e;color:#fff}
.btn-gold:hover{background:#b8914f}
.btn-wa{background:#25D366;color:#fff}
.btn-wa:hover{background:#1ebe57}
.btn-airbnb{background:#FF5A5F;color:#fff}
.btn-airbnb:hover{background:#e04f54}

/* LOCATION */
.location-section{background:#fff;padding:96px 64px;border-top:1px solid rgba(0,0,0,0.07)}
.location-inner{max-width:1100px;margin:0 auto}
.nearby-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:56px}
.nearby-item{background:#faf9f7;padding:28px 24px;display:flex;gap:14px;align-items:flex-start}
.nearby-icon{font-size:1.2rem;flex-shrink:0;margin-top:2px}
.nearby-name{font-size:0.95rem;color:#1a1a1a;font-weight:500;margin-bottom:4px}
.nearby-dist{font-size:0.82rem;color:#888;font-weight:300}

/* HOUSE RULES */
.rules-section{background:#f0ebe1;padding:96px 64px}
.rules-inner{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:64px}
.rules-list{margin-top:56px;display:flex;flex-direction:column;gap:2px}
.rule-item{background:#fff;padding:18px 24px;display:flex;gap:14px;align-items:flex-start}
.rule-icon{font-size:1rem;flex-shrink:0;margin-top:2px;color:#c9a96e}
.rule-text{font-size:0.9rem;color:#555;line-height:1.5;font-weight:300}
.rule-text strong{color:#1a1a1a;font-weight:500}

.site-footer{background:#111;padding:40px 64px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.footer-brand{font-family:'Cormorant Garamond',serif;color:#c9a96e;font-size:18px;letter-spacing:1px}
.footer-tagline{color:rgba(255,255,255,0.35);font-size:12px;letter-spacing:1.5px;text-transform:uppercase;font-style:italic}
.footer-links a{color:rgba(255,255,255,0.4);font-size:12px;margin-left:20px;text-decoration:none;letter-spacing:0.5px;transition:color 0.2s}
.footer-links a:hover{color:#c9a96e}

@media(max-width:900px){
.site-header{padding:0 20px}
.hero-content{padding:0 24px 40px}
.contact-intro,.contact-main,.book-section,.location-section,.rules-section{padding:64px 24px}
.contact-main-inner,.book-inner,.rules-inner{grid-template-columns:1fr}
.nearby-grid{grid-template-columns:1fr 1fr}
.site-footer{padding:32px 24px;flex-direction:column;text-align:center}
.footer-links a{margin:0 10px}
.nav-book-btn{display:none}
}
@media(max-width:600px){
.nearby-grid{grid-template-columns:1fr}
.site-nav a{padding:0 8px;font-size:12px}
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
    <a href="/RSCinemaVilla/booking-enquiry-form/" class="nav-book-btn">Booking Enquiry Form</a>
  </nav>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-content">
    <span class="hero-eyebrow">Get in Touch &middot; Book Your Stay</span>
    <h1>Your dream celebration<br>begins with <em>one call</em></h1>
    <p>Reach out to us on WhatsApp or call us directly &mdash; we respond fast, answer all your questions, and help you plan your event from start to finish.</p>
  </div>
</section>

<!-- CONTACT INTRO -->
<div class="contact-intro">
  <div class="contact-intro-inner">
    <p class="section-eyebrow">We&rsquo;re here for you</p>
    <h2 class="section-title">Booking is <em>simple &amp; fast</em></h2>
    <div class="divider" style="margin:20px auto 24px"></div>
    <p class="body-text">For bookings and enquiries, reach us on <strong>Phone or WhatsApp &mdash; we respond quickly!</strong> The fastest way to reach us is via WhatsApp. Send us a message and we&rsquo;ll get back to you within minutes.</p>
  </div>
</div>

<!-- CONTACT DETAILS + MAP -->
<section class="contact-main">
  <div class="contact-main-inner">
    <div class="contact-details-box">
      <h2>&#128222; Get in Touch</h2>
      <div class="contact-item">
        <div class="c-icon">&#128222;</div>
        <div>
          <div class="c-label">Phone / WhatsApp</div>
          <div class="c-value"><a href="tel:+919206845678" class="phone-link">+91 92068 45678</a></div>
        </div>
      </div>
      <div class="contact-item">
        <div class="c-icon">&#127760;</div>
        <div>
          <div class="c-label">Email</div>
          <div class="c-value"><a href="mailto:rscinemavilla@gmail.com">rscinemavilla@gmail.com</a></div>
        </div>
      </div>
      <div class="contact-item">
        <div class="c-icon">&#128247;</div>
        <div>
          <div class="c-label">Instagram</div>
          <div class="c-value"><a href="https://www.instagram.com/rs_cinema_villa" target="_blank">@rs_cinema_villa</a></div>
        </div>
      </div>
      <div class="contact-item">
        <div class="c-icon">&#128336;</div>
        <div>
          <div class="c-label">Available</div>
          <div class="c-value">Open 24/7 &mdash; 7 days a week</div>
        </div>
      </div>
      <a href="/RSCinemaVilla/booking-enquiry-form/" class="nav-book-btn">Booking Enquiry Form</a>
    </div>
    <div>
      <div class="map-box">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3808.0!2d77.8700!3d17.3500!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTfCsDIxJzAwLjAiTiA3N8KwNTInMTIuMCJF!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="RS Cinema Villa Location"></iframe>
        <div class="map-info">
          <p class="map-address">&#128205; RS Cinema Villa, Moinabad, Hyderabad, Telangana &ndash; 501503, India<br><span style="font-size:0.85rem;color:#aaa;margin-top:6px;display:block">Peaceful surroundings, easily accessible from Hyderabad city center</span></p>
          <a href="https://maps.google.com/?q=RS+Cinema+Villa+Moinabad+Hyderabad" class="map-link" target="_blank">&#128205; Get Directions on Google Maps &rarr;</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- HOW TO BOOK -->
<section class="book-section">
  <div class="book-inner">
    <div>
      <p class="section-eyebrow">How to Book</p>
      <h2 class="section-title" style="color:#fff">Simple. Fast. <em style="color:#e8d5b0">Effortless.</em></h2>
      <div class="divider"></div>
      <p class="body-text" style="color:rgba(255,255,255,0.55)">Securing your dates at RS Cinema Villa takes just a few minutes. Dates fill up fast &mdash; especially on weekends and holidays &mdash; so don&rsquo;t wait.</p>
      <div class="book-steps">
        <div class="book-step"><div class="step-num">01</div><div class="step-text"><strong>WhatsApp or Call Us</strong><span>Reach us at +91 92068 45678 to check availability for your dates</span></div></div>
        <div class="book-step"><div class="step-num">02</div><div class="step-text"><strong>Share Your Event Details</strong><span>Tell us the date, number of guests, and type of occasion</span></div></div>
        <div class="book-step"><div class="step-num">03</div><div class="step-text"><strong>Receive Your Custom Quote</strong><span>We&rsquo;ll send you the best package for your needs, quickly</span></div></div>
        <div class="book-step"><div class="step-num">04</div><div class="step-text"><strong>Confirm with Advance Payment</strong><span>Lock in your dates securely with a deposit</span></div></div>
        <div class="book-step"><div class="step-num">05</div><div class="step-text"><strong>Arrive &amp; Celebrate</strong><span>Our team will be ready to welcome you and make your stay unforgettable</span></div></div>
      </div>
    </div>
    <div class="book-cta">
      <p class="section-eyebrow" style="color:#c9a96e">Ready to Book?</p>
      <p>Contact us today. We respond quickly &mdash; 7 days a week.</p>
      <a href="tel:+919206845678" class="book-phone">+91 92068 45678</a>
      <div class="cta-btns">
        <a href="https://wa.me/919206845678" class="btn btn-wa" target="_blank">&#128172; WhatsApp Us</a>
        <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
        <a href="https://www.airbnb.co.in/rooms/1506244066053865421" class="btn btn-airbnb" target="_blank">&#127968; View on Airbnb</a>
      </div>
    </div>
  </div>
</section>

<!-- LOCATION & NEARBY -->
<section class="location-section">
  <div class="location-inner">
    <p class="section-eyebrow">Location &amp; Nearby</p>
    <h2 class="section-title">Find us in <em>Moinabad, Hyderabad</em></h2>
    <div class="divider"></div>
    <p class="body-text">RS Cinema Villa is located in Moinabad &mdash; a peaceful, scenic neighbourhood just 25&ndash;30 minutes from Hyderabad city centre, Gachibowli, and HITEC City. Lush green surroundings, open air, and tranquility &mdash; a welcome escape that&rsquo;s always within reach.</p>
    <div class="nearby-grid">
      <div class="nearby-item"><span class="nearby-icon">&#127963;</span><div><div class="nearby-name">Charminar &amp; Old City</div><div class="nearby-dist">Approx. 45 minutes</div></div></div>
      <div class="nearby-item"><span class="nearby-icon">&#127754;</span><div><div class="nearby-name">Osman Sagar (Gandipet Lake)</div><div class="nearby-dist">Approx. 20 minutes</div></div></div>
      <div class="nearby-item"><span class="nearby-icon">&#127807;</span><div><div class="nearby-name">KBR National Park</div><div class="nearby-dist">Approx. 35 minutes</div></div></div>
      <div class="nearby-item"><span class="nearby-icon">&#127970;</span><div><div class="nearby-name">Gachibowli / HITEC City</div><div class="nearby-dist">Approx. 25&ndash;30 minutes</div></div></div>
      <div class="nearby-item"><span class="nearby-icon">&#9992;</span><div><div class="nearby-name">Rajiv Gandhi International Airport</div><div class="nearby-dist">Approx. 40 minutes</div></div></div>
      <div class="nearby-item"><span class="nearby-icon">&#9968;</span><div><div class="nearby-name">Chevella (Scenic Hill Drives)</div><div class="nearby-dist">Approx. 15 minutes</div></div></div>
    </div>
  </div>
</section>

<!-- HOUSE RULES -->
<section class="rules-section">
  <div class="rules-inner">
    <div>
      <p class="section-eyebrow">House Rules</p>
      <h2 class="section-title">A few <em>important guidelines</em></h2>
      <div class="divider"></div>
      <p class="body-text">To ensure that every guest has the best possible experience, we kindly request all guests to respect the following guidelines. For any questions, WhatsApp us at <a href="https://wa.me/919206845678" style="color:#c9a96e">+91 92068 45678</a>.</p>
    </div>
    <div>
      <div class="rules-list">
        <div class="rule-item"><span class="rule-icon">&#128336;</span><div class="rule-text"><strong>Check-in:</strong> 12:00 Noon onwards (flexible, subject to arrangement)</div></div>
        <div class="rule-item"><span class="rule-icon">&#128336;</span><div class="rule-text"><strong>Check-out:</strong> 11:00 AM (late check-out available on request)</div></div>
        <div class="rule-item"><span class="rule-icon">&#128101;</span><div class="rule-text"><strong>Guest count:</strong> Please inform us in advance of the total number of guests</div></div>
        <div class="rule-item"><span class="rule-icon">&#127867;</span><div class="rule-text"><strong>Alcohol:</strong> Permitted responsibly within the villa premises</div></div>
        <div class="rule-item"><span class="rule-icon">&#128054;</span><div class="rule-text"><strong>Pets:</strong> Please enquire at the time of booking</div></div>
        <div class="rule-item"><span class="rule-icon">&#128683;</span><div class="rule-text"><strong>Smoking:</strong> Permitted in designated outdoor areas only</div></div>
        <div class="rule-item"><span class="rule-icon">&#128263;</span><div class="rule-text"><strong>Noise:</strong> Please be mindful of the neighbourhood, especially late at night</div></div>
        <div class="rule-item"><span class="rule-icon">&#128274;</span><div class="rule-text"><strong>Security deposit</strong> may be collected at check-in and refunded after satisfactory checkout</div></div>
      </div>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="footer-brand">RS Cinema Villa</div>
  <div class="footer-tagline">Your dream celebration is just one call away.</div>
  <div class="footer-links">
    <a href="https://www.instagram.com/rs_cinema_villa/" target="_blank">Instagram</a>
    <a href="mailto:rscinemavilla@gmail.com">Email</a>
    <a href="/RSCinemaVilla/reviews/">Reviews</a>
  </div>
</footer>
