from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>

<html>

<head>
<title>FAREED BABA</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:Arial,sans-serif;
}

body{
background:#111;
color:white;
}

/* NAVBAR */
.navbar{
background:rgba(0,0,0,0.9);
padding:10px 40px;
display:flex;
justify-content:space-between;
align-items:center;
border-bottom:2px solid gold;
position:sticky;
top:0;
z-index:1000;
}

.logo{
height:70px;
width:auto;
}

.nav-links{
display:flex;
gap:25px;
}

.nav-links a{
color:white;
text-decoration:none;
font-size:18px;
font-weight:bold;
}

.nav-links a:hover{
color:gold;
}
/* HERO BANNER */

.hero{
background:#111;
padding: 15px 20px;
text-align:center;
border-bottom:2px solid gold;
}

.hero h1{
font-size:80px;
color:gold;
margin-bottom:15px;
}

.hero p{
font-size:28px;
color:white;
margin-bottom:30px;
}

.hero-buttons .btn{
margin:10px;
}
/* SECTIONS */

.section{
padding:60px 30px;
text-align:center;
}

.section h2{
color:gold;
font-size:40px;
margin-bottom:10px;
}

.section-sub{
color:#ddd;
margin-bottom:35px;
font-style:italic;
}

/* PRODUCT CARDS */

.card{
display:inline-block;
width:300px;
background:white;
color:black;
margin:15px;
border-radius:15px;
overflow:hidden;
transition:0.4s;
box-shadow:0 0 15px rgba(255,215,0,0.2);
}

.card:hover{
transform:translateY(-10px);
}

.card img{
width:100%;
height:260px;
object-fit:cover;
}

.card h3{
margin-top:15px;
}

.price{
color:darkgoldenrod;
font-weight:bold;
font-size:22px;
margin:10px;
}

.btn{
display:inline-block;
margin-bottom:20px;
padding:12px 20px;
background:gold;
color:black;
text-decoration:none;
border-radius:25px;
font-weight:bold;
}

.btn:hover{
background:black;
color:gold;
border:1px solid gold;
}
.back-home-container{
    text-align:center;
    margin:50px 0;
}

.back-btn{
    display:inline-block;
    padding:15px 35px;
    background:gold;
    color:black;
    text-decoration:none;
    border-radius:30px;
    font-weight:bold;
    font-size:18px;
    transition:0.3s;
}

.back-btn:hover{
    background:white;
    color:black;
}

/* WHY US */

.why{
background:#1a1a1a;
padding:60px 20px;
text-align:center;
}

.why h2{
color:gold;
margin-bottom:30px;
}

.feature{
display:inline-block;
background:#222;
padding:20px;
margin:10px;
border-radius:10px;
width:220px;
}

/* FOOTER */

.footer{
background:black;
padding:30px;
text-align:center;
border-top:2px solid gold;
}

.footer h3{
color:gold;
margin-bottom:10px;
}

</style>
</head>

<body>

<div class="navbar">

<img src="/static/images/logo.png" class="logo">

<div class="nav-links">
<a href="/">Home</a>
<a href="/mens_sunglasses">Men</a>
<a href="#women">Women</a>
<a href="#kids">Kids</a>
<a href="#contact">Contact</a>
</div>

</div>

<div class="hero">
    <h1>FAREED BABA</h1>
    <p>Premium Sunglasses • Wallets • Bags • Accessories</p>

    <div class="hero-buttons">
       <a href="#mens" class="btn">Shop for Men</a>

<a href="#women" class="btn">Shop for Women</a>
<a href="#kids" class="btn">Shop for Kids</a>
    </div>
</div>
</div>
<div class="section">


<div class="section" id="mens">
<h2>Men's Collection</h2>

<p class="section-sub">
Elegance is an attitude.
</p>

<div class="card">
<img src="/static/images/sg01_Midnight_Commander.jpeg">
<h3>Sunglasses</h3>
<p>Explore our signature sunglasses collection.</p>
<a class="btn" href="/mens_sunglasses">
View Collection
</a>
</div>

<div class="card">
<img src="/static/images/wallet1.jpg">
<h3>Wallets</h3>
<p>Premium wallets for everyday luxury.</p>
<a class="btn" href="/mens_wallets">
View Collection
</a>
</div>

</div>

</div>
<div class="section" id="mens_wallets">


<div class="section" id="women">
<h2>Women's Collection</h2>
<p class="section-sub">Grace in every detail.</p>

<div class="card">
<img src="/static/images/women_bag.jpg">
<h3>Designer Handbag</h3>
<p class="price">₹Coming Soon</p>

</div>
<div class="card">
<img src="/static/images/bag1.jpg">
<h3>Luxury Handbag</h3>
<p class="price">Coming Soon</p>
</div>

<div class="card">
<img src="/static/images/women_abaya.jpg">
<h3>Premium Abaya</h3>
<p class="price">Coming Soon</p>

</div>

</div>

<div class="section" id="kids">

<h2>Kids Collection</h2>
<p class="section-sub">Little Styles, Big Smiles.</p>

<div class="card">
<img src="/static/images/kids_cap.jpg">
<h3>Kids Cap</h3>
<p class="price">Coming Soon</p>
</div>

<div class="card">
<img src="/static/images/cap1.jpg">
<h3>Kids Fashion Cap</h3>
<p class="price">Coming Soon</p>
</div>

<div class="card">
<img src="/static/images/kids_glasses.jpg">
<h3>Kids Sunglasses</h3>
<p class="price">Coming Soon</p>
</div>

</div>

<div class="why">

<h2>Why Choose Fareed Baba?</h2>

<div class="feature">✔ Premium Quality</div>
<div class="feature">✔ Affordable Luxury</div>
<div class="feature">✔ Latest Fashion Trends</div>
<div class="feature">✔ Fast Delivery</div>

</div>

<div class="footer">

<h3>FAREED BABA</h3>

<p>Luxury Within Reach • Style That Speaks</p>

<p>WhatsApp: +91 9936739281</p>

</div>

</body>
</html>
"""

@app.route("/mens_sunglasses")
def mens_sunglasses():
   return """
<html>

<head>
<title>Men's Sunglasses</title>

<style>

body{
background:#111;
color:white;
font-family:Arial;
text-align:center;
}

h1{
color:gold;
margin-top:30px;
}

.card{
display:inline-block;
width:300px;
background:white;
color:black;
margin:15px;
border-radius:15px;
overflow:hidden;
}

.card img{
width:100%;
height:280px;
object-fit:cover;
}

.price{
color:darkgoldenrod;
font-size:22px;
font-weight:bold;
}

.btn{
display:inline-block;
margin:15px;
padding:10px 20px;
background:gold;
color:black;
text-decoration:none;
border-radius:20px;
font-weight:bold;
}

</style>

</head>

<body>

<h1>FAREED BABA Signature Sunglasses Collection</h1>


<div class="card">

<img src="/static/images/sg01_Midnight_Commander.jpeg">

<h3>Midnight Commander</h3>

<p>FB-SG-01</p>

<p class="price">₹499</p>

<a class="btn"
href="https://wa.me/919936739281?text=Hi,%20I%20would%20like%20to%20order%20FB-SG-01%20Midnight%20Commander">
Order Now
</a>

</div>
<div class="card">
<img src="/static/images/sg02_Shadow_Edge.jpeg">
<h3>Shadow Edge</h3>
<p class="price">₹499</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-02 Shadow Edge">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg03_Arctic_Blue_Mirror.jpeg">
<h3>Arctic Blue Mirror</h3>
<p class="price">₹549</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-03 Arctic Blue Mirror">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg04_Ivory_Luxe.jpeg">
<h3>Ivory Luxe</h3>
<p class="price">₹549</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-04 Ivory Luxe">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg05_Golden_Aviator_Elite.jpeg">
<h3>Golden Aviator Elite</h3>
<p class="price">₹599</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-05 Golden Aviator Elite">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg06_Crimson_Pilot.jpeg">
<h3>Crimson Pilot</h3>
<p class="price">₹599</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-06 Crimson Pilot">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg07_Royal_Amber.jpeg">
<h3>Royal Amber</h3>
<p class="price">₹649</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-07 Royal Amber">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg08_Stealth_Carbon.jpeg">
<h3>Stealth Carbon</h3>
<p class="price">₹649</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-08 Stealth Carbon">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg09_Titan_Hexa.jpeg">
<h3>Titan Hexa</h3>
<p class="price">₹699</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-09 Titan Hexa">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg10_Urban_Graphite.jpeg">
<h3>Urban Graphite</h3>
<p class="price">₹699</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-10 Urban Graphite">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg11_Black_Phantom.jpeg">
<h3>Black Phantom</h3>
<p class="price">₹749</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-11 Black Phantom">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg12_Desert_Gold_Aviator.jpeg">
<h3>Desert Gold Aviator</h3>
<p class="price">₹799</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-12 Desert Gold Aviator">Order Now</a>
</div>

<div class="card">
<img src="/static/images/sg13_Titanium_Octane.jpeg">
<h3>Titanium Octane</h3>
<p class="price">₹899</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-13 Titanium Octane">Order Now</a>
</div>

<div class="back-home-container">
    <a href="/" class="back-btn">← Back to Home</a>
</div>

</body>
</html>
"""
@app.route("/mens_wallets")
def mens_wallets():
    return """
    <html>
    <body style="background:#111;color:white;text-align:center;">
    <h1 style="color:gold;">Men's Wallet Collection</h1>
    <p>Coming Soon!!!.</p>
    <a href="/" style="color:gold;">Back Home</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
