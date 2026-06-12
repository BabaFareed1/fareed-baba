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
background:black;
padding:15px 30px;
border-bottom:2px solid gold;
position:sticky;
top:0;
z-index:1000;
}

.brand{
display:flex;
align-items:center;
justify-content:center;
gap:15px;
}

.logo{
height:60px;
width:auto;
}

.navbar h1{
color:gold;
font-size:36px;
}}

/* HERO BANNER */

.hero{
height:100vh;
background:url('/static/images/hero.jpg');
background-size:cover;
background-position:center;
background-repeat:no-repeat;
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

<div class="brand">

<img src="/static/images/logo.png" class="logo">

<h1>FAREED BABA</h1>

</div>

</div>

<div class="hero"></div>

<div class="section">

<div class="section">

<h2>Men's Collection</h2>
<p class="section-sub">Elegance is an attitude.</p>

<a class="btn" href="#mens_sunglasses">
Sunglasses
</a>

<a class="btn" href="#mens_wallets">
Wallets
</a>

</div>
<div class="section" id="mens_sunglasses">

<h2>Men's Sunglasses</h2>
<div class="section">

<h2>FAREED BABA Signature Sunglasses Collection</h2>
<p class="section-sub">Designed for those who lead, not follow.</p>

<div class="card">
<img src="/static/images/sg01_Midnight_Commander.jpeg">
<h3>Midnight Commander</h3>
<p class="price">₹499</p>
<a class="btn" href="https://wa.me/919936739281?text=I want FB-SG-01 Midnight Commander">Order Now</a>
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

</div>


</div>
<div class="section" id="mens_wallets">

<h2>Men's Wallets</h2>

<div class="card">
<img src="/static/images/men_wallet.jpg">
<h3>Leather Wallet</h3>
<p class="price">₹999</p>
<a class="btn"
href="https://wa.me/919936739281?text=I want Leather Wallet">
Order Now
</a>
</div>

</div>

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

<div class="section">

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
