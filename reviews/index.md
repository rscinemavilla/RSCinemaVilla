---
layout: default
title: Reviews & Testimonials
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
  background: url('/RSCinemaVilla/images/RScinemavilla8.JPG') center/cover no-repeat;
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
  text-align: center;
  font-size: 2rem;
  color: #d4af37;
  margin-bottom: 40px;
  letter-spacing: 2px;
}

.google-rating {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 10px;
  padding: 30px 40px;
  text-align: center;
  margin-bottom: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
}
.google-rating .rating-score {
  font-size: 3.5rem;
  font-weight: bold;
  color: #fff;
  line-height: 1;
}
.google-rating .stars { font-size: 1.8rem; color: #f4b942; margin-bottom: 6px; }
.google-rating .count { color: #c8b89a; font-size: 0.95rem; }
.google-rating .g-label { color: #4285F4; font-size: 1.1rem; font-weight: bold; }

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 50px;
}
.review-card {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border: 1px solid rgba(212,175,55,0.2);
  border-radius: 10px;
  padding: 28px 30px;
}
.review-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}
.reviewer-name { font-size: 1.1rem; font-weight: bold; color: #d4af37; }
.review-date { color: #8a7a5a; font-size: 0.85rem; }
.review-stars { color: #f4b942; font-size: 1rem; margin-bottom: 12px; }
.review-text { color: #c8b89a; line-height: 1.7; font-size: 0.95rem; }
.review-verified { color: #4caf50; font-size: 0.8rem; margin-top: 10px; }

.testimonials-section {
  margin-bottom: 50px;
}
.testimonial-card {
  background: linear-gradient(135deg, #1a1a1a, #0d0d0d);
  border-left: 4px solid #d4af37;
  border-radius: 0 10px 10px 0;
  padding: 28px 36px;
  margin-bottom: 20px;
}
.testimonial-stars { color: #f4b942; font-size: 1.1rem; margin-bottom: 12px; }
.testimonial-text { color: #c8b89a; line-height: 1.8; font-size: 1.05rem; font-style: italic; margin-bottom: 14px; }
.testimonial-author { color: #d4af37; font-size: 0.9rem; }

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
.btn-google { background: #4285F4; color: #fff; }
.btn-google:hover { background: #3574e2; transform: translateY(-2px); }
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
    <a href="/RSCinemaVilla/pricing/">Pricing</a>
    <a href="/RSCinemaVilla/reviews/" class="active">Reviews &amp; Testimonials</a>
    <a href="/RSCinemaVilla/contact/">Contact &amp; Book Now</a>
  </nav>
</header>

<section class="hero">
  <div class="hero-box">
    <h1>RS Cinema Villa</h1>
    <p>Reviews &amp; Testimonials</p>
  </div>
</section>

<div class="section">
  <h2 class="section-title">What Our Customers Say</h2>

  <div class="google-rating">
    <div>
      <div class="rating-score">5.0</div>
    </div>
    <div>
      <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="count">Based on 11 Google Reviews</div>
      <div class="g-label">Google Reviews</div>
    </div>
    <div>
      <a href="https://g.page/r/rscinemavilla/review" class="btn btn-google" target="_blank">&#11088; Review us on Google</a>
    </div>
  </div>

  <div class="reviews-grid">
    <div class="review-card">
      <div class="review-header">
        <div class="reviewer-name">Uday Kumar</div>
        <div class="review-date">1 month ago</div>
      </div>
      <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="review-text">"I had a wonderful experience at the farmhouse. The place is peaceful, clean, and beautifully maintained. The amenities were top-notch and the host was very responsive and helpful throughout our stay. Highly recommend!"</div>
      <div class="review-verified">&#10003; Google Review</div>
    </div>

    <div class="review-card">
      <div class="review-header">
        <div class="reviewer-name">Peter Jones</div>
        <div class="review-date">2 months ago</div>
      </div>
      <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="review-text">"Really nice stay. The host and the place were really good. We had fun!"</div>
      <div class="review-verified">&#10003; Google Review</div>
    </div>

    <div class="review-card">
      <div class="review-header">
        <div class="reviewer-name">Radhika Chatpalliwar</div>
        <div class="review-date">3 months ago</div>
      </div>
      <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="review-text">"We recently stayed at RS Cinevilla, Hyderabad to celebrate Valentine&rsquo;s Day, and honestly, it was the perfect choice for a romantic staycation. The villa is stunning, private, and has everything you need for a memorable experience. Highly recommended!"</div>
      <div class="review-verified">&#10003; Google Review</div>
    </div>

    <div class="review-card">
      <div class="review-header">
        <div class="reviewer-name">Bharathi Y</div>
        <div class="review-date">4 months ago</div>
      </div>
      <div class="review-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="review-text">"This is a great property to stay in with spacious rooms and modern amenities. We rented it out for one of our family events. We lived there for 3 days with our whole family and had a wonderful time. The property management team is very responsive and helpful."</div>
      <div class="review-verified">&#10003; Google Review</div>
    </div>
  </div>

  <div class="testimonials-section">
    <div class="testimonial-card">
      <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="testimonial-text">"An absolutely stunning villa &mdash; the pool, the interiors, the privacy. Perfect for our family gathering."</div>
      <div class="testimonial-author">&mdash; Airbnb Guest, Hyderabad</div>
    </div>

    <div class="testimonial-card">
      <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="testimonial-text">"Best birthday celebration venue! Beautiful space and very responsive host."</div>
      <div class="testimonial-author">&mdash; Airbnb Guest</div>
    </div>

    <div class="testimonial-card">
      <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <div class="testimonial-text">"Perfect location for our film shoot. Stunning backdrops and complete privacy."</div>
      <div class="testimonial-author">&mdash; Airbnb Guest</div>
    </div>
  </div>

  <div class="cta-section">
    <h2>Share Your Experience</h2>
    <p>Had a wonderful stay at RS Cinema Villa? We&rsquo;d love to hear from you!</p>
    <div class="cta-buttons">
      <a href="https://g.page/r/rscinemavilla/review" class="btn btn-google" target="_blank">&#11088; Leave us a Google Review</a>
      <a href="https://www.airbnb.com/rooms/rscinemavilla" class="btn btn-airbnb" target="_blank">&#127968; View all Airbnb Reviews</a>
      <a href="https://calendly.com/rscinemavilla" class="btn btn-gold" target="_blank">&#128197; Book Now</a>
      <a href="https://www.instagram.com/rs_cinema_villa" class="btn btn-outline" target="_blank">&#128247; Follow us @rs_cinema_villa</a>
    </div>
  </div>
</div>

<div class="footer-tagline">Happiness shared is happiness doubled &mdash; thank you for celebrating with us.</div>
