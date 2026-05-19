---
layout: default
title: Reviews & Testimonials
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

.hero{position:relative;width:100%;height:55vh;min-height:380px;background:url('/RSCinemaVilla/images/RScinemavilla8.JPG') center/cover no-repeat;display:flex;align-items:flex-end;justify-content:flex-start;overflow:hidden}
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

/* RATING BAND */
.rating-band{background:#1a1a1a;padding:64px;text-align:center}
.rating-band-inner{max-width:700px;margin:0 auto}
.big-score{font-family:'Cormorant Garamond',serif;font-size:7rem;font-weight:300;color:#c9a96e;line-height:1}
.rating-stars{font-size:1.4rem;color:#c9a96e;letter-spacing:4px;margin:8px 0 12px}
.rating-label{font-size:12px;color:rgba(255,255,255,0.4);letter-spacing:2px;text-transform:uppercase;margin-bottom:28px}
.google-link{display:inline-block;background:#4285F4;color:#fff;padding:12px 28px;border-radius:2px;text-decoration:none;font-size:13px;font-weight:500;letter-spacing:0.5px;transition:background 0.2s}
.google-link:hover{background:#3574e2}

/* INTRO */
.reviews-intro{background:#fff;padding:64px;text-align:center;border-bottom:1px solid rgba(0,0,0,0.07)}
.reviews-intro-inner{max-width:700px;margin:0 auto}

/* GOOGLE REVIEWS */
.google-reviews-section{background:#faf9f7;padding:96px 64px}
.google-reviews-inner{max-width:1100px;margin:0 auto}
.reviews-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:2px;margin-top:56px}
.review-card{background:#fff;padding:36px;border-top:3px solid transparent;transition:border-color 0.3s}
.review-card:hover{border-top-color:#c9a96e}
.review-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:16px}
.reviewer-name{font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#1a1a1a;font-weight:400}
.review-date{font-size:11px;color:#aaa;letter-spacing:1px;text-transform:uppercase}
.review-stars{color:#c9a96e;font-size:0.9rem;letter-spacing:2px;margin-bottom:14px}
.review-text{color:#666;line-height:1.75;font-size:0.93rem;font-weight:300;font-style:italic}
.review-verified{font-size:11px;color:#4caf50;margin-top:14px;letter-spacing:0.5px}

/* AIRBNB TESTIMONIALS */
.testimonials-section{background:#fff;padding:96px 64px;border-top:1px solid rgba(0,0,0,0.07)}
.testimonials-inner{max-width:1100px;margin:0 auto}
.testimonials-list{margin-top:56px;display:flex;flex-direction:column;gap:2px}
.testimonial-card{background:#faf9f7;padding:40px 48px;display:grid;grid-template-columns:auto 1fr;gap:32px;align-items:center;border-left:3px solid #c9a96e}
.testimonial-stars{color:#c9a96e;font-size:1rem;letter-spacing:3px;margin-bottom:14px}
.testimonial-text{font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#1a1a1a;line-height:1.6;font-style:italic;margin-bottom:14px}
.testimonial-author{font-size:12px;color:#888;letter-spacing:1.5px;text-transform:uppercase}

/* WHY GUESTS LOVE US */
.why-section{background:#f0ebe1;padding:96px 64px}
.why-inner{max-width:1100px;margin:0 auto}
.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:56px}
.why-card{background:#fff;padding:40px 32px;text-align:center;border-radius:2px}
.why-icon{font-size:2rem;margin-bottom:16px;display:block}
.why-title{font-family:'Cormorant Garamond',serif;font-size:1.2rem;color:#1a1a1a;margin-bottom:10px}
.why-desc{font-size:0.88rem;color:#777;line-height:1.65;font-weight:300}

/* CTA */
.cta-band{background:#1a1a1a;padding:80px 64px;text-align:center}
.cta-band .section-eyebrow{color:#c9a96e}
.cta-band h2{font-family:'Cormorant Garamond',serif;font-size:clamp(1.8rem,3.5vw,2.8rem);font-weight:300;color:#fff;margin:14px 0 10px}
.cta-band p{color:rgba(255,255,255,0.55);font-size:1rem;font-weight:300;margin-bottom:36px}
.cta-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn{display:inline-block;padding:14px 32px;font-size:13px;font-weight:500;letter-spacing:1px;text-decoration:none;border-radius:2px;transition:all 0.2s}
.btn-gold{background:#c9a96e;color:#fff}
.btn-gold:hover{background:#b8914f}
.btn-google{background:#4285F4;color:#fff}
.btn-google:hover{background:#3574e2}
.btn-airbnb{background:#FF5A5F;color:#fff}
.btn-airbnb:hover{background:#e04f54}
.btn-outline{border:1px solid rgba(255,255,255,0.3);color:#fff}
.btn-outline:hover{border-color:rgba(255,255,255,0.7)}

.site-footer{background:#111;padding:40px 64px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.footer-brand{font-family:'Cormorant Garamond',serif;color:#c9a96e;font-size:18px;letter-spacing:1px}
.footer-tagline{color:rgba(255,255,255,0.35);font-size:12px;letter-spacing:1.5px;text-transform:uppercase;font-style:italic}
.footer-links a{color:rgba(255,255,255,0.4);font-size:12px;margin-left:20px;text-decoration:none;letter-spacing:0.5px;transition:color 0.2s}
.footer-links a:hover{color:#c9a96e}

@media(max-width:900px){
.site-header{padding:0 20px}
.hero-content{padding:0 24px 40px}
.rating-band,.reviews-intro,.google-reviews-section,.testimonials-section,.why-section,.cta-band{padding:64px 24px}
.reviews-grid{grid-template-columns:1fr}
.why-grid{grid-template-columns:1fr 1fr}
.testimonial-card{grid-template-columns:1fr}
.site-footer{padding:32px 24px;flex-direction:column;text-align:center}
.footer-links a{margin:0 10px}
.nav-book-btn{display:none}
}
@media(max-width:600px){
.why-grid{grid-template-columns:1fr}
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
    <a href="/RSCinemaVilla/reviews/" class="active">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
    <a href="https://wa.me/919206845678" class="nav-book-btn" target="_blank">Enquire Now</a>
  </nav>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-content">
    <span class="hero-eyebrow">Real Stories &middot; Real Guests</span>
    <h1>Loved by guests across <em>Hyderabad &amp; beyond</em></h1>
    <p>At RS Cinema Villa, every guest is family. We pour our heart into making each stay extraordinary &mdash; and our guests keep saying so.</p>
  </div>
</section>

<!-- RATING BAND -->
<div class="rating-band">
  <div class="rating-band-inner">
    <p class="section-eyebrow" style="color:#c9a96e">Our Google Rating</p>
    <div class="big-score">5.0</div>
    <div class="rating-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
    <div class="rating-label">Based on 11 Google Reviews &middot; Perfect 5-star rating</div>
    <a href="https://g.page/r/rscinemavilla/review" class="google-link" target="_blank">&#11088; Review us on Google</a>
  </div>
</div>

<!-- INTRO -->
<div class="reviews-intro">
  <div class="reviews-intro-inner">
    <p class="section-eyebrow">What Our Customers Say</p>
    <h2 class="section-title">Five stars, <em>every time</em></h2>
    <div class="divider" style="margin:20px auto 24px"></div>
    <p class="body-text">Here&rsquo;s what real guests love most about staying at RS Cinema Villa. Every review is genuine &mdash; from real people who celebrated their most special moments here.</p>
  </div>
</div>

<!-- GOOGLE REVIEWS -->
<section class="google-reviews-section">
  <div class="google-reviews-inner">
    <p class="section-eyebrow">Google Reviews</p>
    <h2 class="section-title">Verified guest <em>experiences</em></h2>
    <div class="divider"></div>
    <div class="reviews-grid">
      <div class="review-card">
        <div class="review-header">
          <div class="reviewer-name">Uday Kumar</div>
          <div class="review-date">1 month ago</div>
        </div>
        <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="review-text">&ldquo;I had a wonderful experience at the farmhouse. The place is peaceful, clean, and beautifully maintained. The amenities were top-notch and the host was very responsive and helpful throughout our stay. Highly recommend!&rdquo;</div>
        <div class="review-verified">&#10003; Verified Google Review</div>
      </div>
      <div class="review-card">
        <div class="review-header">
          <div class="reviewer-name">Peter Jones</div>
          <div class="review-date">2 months ago</div>
        </div>
        <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="review-text">&ldquo;Really nice stay. The host and the place were really good. We had fun!&rdquo;</div>
        <div class="review-verified">&#10003; Verified Google Review</div>
      </div>
      <div class="review-card">
        <div class="review-header">
          <div class="reviewer-name">Radhika Chatpalliwar</div>
          <div class="review-date">3 months ago</div>
        </div>
        <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="review-text">&ldquo;We recently stayed at RS Cinevilla, Hyderabad to celebrate Valentine&rsquo;s Day, and honestly, it was the perfect choice for a romantic staycation. The villa is stunning, private, and has everything you need for a memorable experience. Highly recommended!&rdquo;</div>
        <div class="review-verified">&#10003; Verified Google Review</div>
      </div>
      <div class="review-card">
        <div class="review-header">
          <div class="reviewer-name">Bharathi Y</div>
          <div class="review-date">4 months ago</div>
        </div>
        <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <div class="review-text">&ldquo;This is a great property to stay in with spacious rooms and modern amenities. We rented it out for one of our family events. We lived there for 3 days with our whole family and had a wonderful time. The property management team is very responsive and helpful.&rdquo;</div>
        <div class="review-verified">&#10003; Verified Google Review</div>
      </div>
    </div>
  </div>
</section>

<!-- AIRBNB TESTIMONIALS -->
<section class="testimonials-section">
  <div class="testimonials-inner">
    <p class="section-eyebrow">Airbnb Guest Reviews</p>
    <h2 class="section-title">What our guests are <em>saying</em></h2>
    <div class="divider"></div>
    <div class="testimonials-list">
      <div class="testimonial-card">
        <div></div>
        <div>
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <div class="testimonial-text">&ldquo;An absolutely stunning villa &mdash; the pool, the interiors, the privacy. Perfect for our family gathering.&rdquo;</div>
          <div class="testimonial-author">&mdash; Airbnb Guest, Hyderabad</div>
        </div>
      </div>
      <div class="testimonial-card">
        <div></div>
        <div>
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <div class="testimonial-text">&ldquo;Best birthday celebration venue! Beautiful space and very responsive host.&rdquo;</div>
          <div class="testimonial-author">&mdash; Airbnb Guest</div>
        </div>
      </div>
      <div class="testimonial-card">
        <div></div>
        <div>
          <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
          <div class="testimonial-text">&ldquo;Perfect location for our film shoot. Stunning backdrops and complete privacy.&rdquo;</div>
          <div class="testimonial-author">&mdash; Airbnb Guest</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WHY GUESTS LOVE US -->
<section class="why-section">
  <div class="why-inner">
    <p class="section-eyebrow">Why Guests Come Back</p>
    <h2 class="section-title">What our guests <em>love most</em></h2>
    <div class="divider"></div>
    <div class="why-grid">
      <div class="why-card">
        <span class="why-icon">&#128274;</span>
        <div class="why-title">Perfect Privacy</div>
        <p class="why-desc">Guests love having the entire villa to themselves &mdash; no shared spaces, no other guests, just complete exclusivity.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">&#127946;</span>
        <div class="why-title">Stunning Spaces</div>
        <p class="why-desc">From the glittering pool to the private cinema room &mdash; guests consistently say every corner of the villa is beautiful.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">&#128172;</span>
        <div class="why-title">Responsive Host</div>
        <p class="why-desc">Multiple guests highlight how quickly we respond and how helpful our team is &mdash; before, during, and after the stay.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">&#127874;</span>
        <div class="why-title">Ideal for Celebrations</div>
        <p class="why-desc">Birthday parties, romantic getaways, film shoots &mdash; guests say RS Cinema Villa makes every occasion feel extra special.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">&#127807;</span>
        <div class="why-title">Great Location</div>
        <p class="why-desc">Peaceful, scenic, and surrounded by nature in Moinabad &mdash; yet easily reachable from Hyderabad city in just 30 minutes.</p>
      </div>
      <div class="why-card">
        <span class="why-icon">&#10024;</span>
        <div class="why-title">Clean &amp; Well-Maintained</div>
        <p class="why-desc">Guests consistently praise the property&rsquo;s impeccable cleanliness, maintenance, and attention to detail in every corner.</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-band">
  <p class="section-eyebrow">Share your experience</p>
  <h2>Had a wonderful stay?<br><em style="color:#e8d5b0;font-style:italic">We&rsquo;d love to hear from you!</em></h2>
  <p>Your kind words help other families and couples discover RS Cinema Villa. Share your experience on Google or Airbnb.</p>
  <div class="cta-btns">
    <a href="https://g.page/r/rscinemavilla/review" class="btn btn-google" target="_blank">&#11088; Leave a Google Review</a>
    <a href="https://www.airbnb.co.in/rooms/1506244066053865421" class="btn btn-airbnb" target="_blank">&#127968; View Airbnb Reviews</a>
    <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
    <a href="https://www.instagram.com/rs_cinema_villa" class="btn btn-outline" target="_blank">&#128247; Follow @rs_cinema_villa</a>
  </div>
</section>

<footer class="site-footer">
  <div class="footer-brand">RS Cinema Villa</div>
  <div class="footer-tagline">Happiness shared is happiness doubled &mdash; thank you for celebrating with us.</div>
  <div class="footer-links">
    <a href="https://www.instagram.com/rs_cinema_villa/" target="_blank">Instagram</a>
    <a href="mailto:rscinemavilla@gmail.com">Email</a>
    <a href="/RSCinemaVilla/contact/">Contact</a>
  </div>
</footer>
