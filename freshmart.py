from flask import Flask, render_template_string

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Fresh Tomatoes",
        "category": "Vegetables",
        "price": 40,
        "image": "https://images.unsplash.com/photo-1546094096-0df4bcaaa337?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "name": "Organic Carrots",
        "category": "Vegetables",
        "price": 60,
        "image": "https://images.unsplash.com/photo-1447175008436-054170c2e979?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "name": "Fresh Broccoli",
        "category": "Vegetables",
        "price": 90,
        "image": "https://images.unsplash.com/photo-1584270354949-c26b0d5b4a0c?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "name": "Red Apples",
        "category": "Fruits",
        "price": 160,
        "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 5,
        "name": "Fresh Bananas",
        "category": "Fruits",
        "price": 50,
        "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 6,
        "name": "Sweet Oranges",
        "category": "Fruits",
        "price": 100,
        "image": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 7,
        "name": "Orange Juice",
        "category": "Juices",
        "price": 80,
        "image": "https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 8,
        "name": "Berry Juice",
        "category": "Juices",
        "price": 90,
        "image": "https://images.unsplash.com/photo-1610970881699-44a5587cabec?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 9,
        "name": "Green Detox Juice",
        "category": "Juices",
        "price": 100,
        "image": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=800&q=80"
    },
]

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Fresh Mart | Fresh Food, Healthy Life</title>

<style>

:root {
    --green: #16833c;
    --dark: #103d25;
    --light: #f6fff5;
    --accent: #9bdd4f;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: var(--light);
    color: #20352a;
}

/* NAVBAR */

nav {
    position: sticky;
    top: 0;
    z-index: 100;

    background: white;
    min-height: 76px;

    padding: 0 7%;

    display: flex;
    align-items: center;
    gap: 25px;

    box-shadow: 0 2px 15px rgba(0, 0, 0, .08);
}

.logo {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--green);
    white-space: nowrap;
}

.logo span {
    color: var(--dark);
}

.links {
    display: flex;
    gap: 22px;
    list-style: none;
    margin-left: auto;
}

.links a {
    text-decoration: none;
    color: #33443a;
    font-weight: 600;
}

.links a:hover {
    color: var(--green);
}

.search {
    width: 220px;
    border: 1px solid #ddd;
    border-radius: 25px;

    padding: 11px 16px;
    outline: none;
}

.cart-button {
    border: 0;
    background: var(--green);
    color: white;

    border-radius: 25px;
    padding: 11px 16px;

    cursor: pointer;
    font-weight: bold;
    white-space: nowrap;
}

/* HERO */

.hero {
    min-height: 570px;

    padding: 80px 8%;

    display: flex;
    align-items: center;

    background:
        linear-gradient(
            90deg,
            rgba(7, 46, 22, .88),
            rgba(7, 46, 22, .35)
        ),
        url('https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=1800&q=85');

    background-position: center;
    background-size: cover;
}

.hero-content {
    max-width: 650px;
    color: white;
}

.hero h1 {
    font-size: clamp(3rem, 7vw, 5.2rem);
    line-height: 1;
    margin-bottom: 22px;
}

.hero h1 span {
    color: var(--accent);
}

.hero p {
    font-size: 1.2rem;
    line-height: 1.7;

    margin-bottom: 30px;
    max-width: 560px;
}

.btn {
    display: inline-block;

    border: 0;
    background: var(--green);
    color: white;

    text-decoration: none;

    padding: 15px 28px;
    border-radius: 30px;

    font-size: 1rem;
    font-weight: bold;

    cursor: pointer;
}

.btn:hover {
    background: #0d692e;
}

/* GENERAL */

section {
    padding: 75px 7%;
}

.title {
    text-align: center;
    margin-bottom: 40px;
}

.title h2 {
    font-size: 2.4rem;
    color: var(--dark);
    margin-bottom: 10px;
}

.title p {
    color: #68736c;
}

/* CATEGORIES */

.categories {
    background: #ecf8eb;
}

.category-grid,
.product-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
}

.category {
    height: 300px;

    border-radius: 20px;
    overflow: hidden;
    position: relative;

    cursor: pointer;

    box-shadow: 0 8px 25px rgba(0, 0, 0, .12);
}

.category img {
    width: 100%;
    height: 100%;
    object-fit: cover;

    transition: .4s;
}

.category:hover img {
    transform: scale(1.06);
}

.category div {
    position: absolute;
    inset: 0;

    display: flex;
    align-items: flex-end;

    padding: 25px;

    background: linear-gradient(
        transparent,
        rgba(0, 0, 0, .75)
    );

    color: white;
    font-size: 1.8rem;
    font-weight: bold;
}

/* PRODUCTS */

.product-card {
    background: white;

    border-radius: 18px;
    overflow: hidden;

    box-shadow: 0 8px 25px rgba(0, 0, 0, .08);

    transition: .25s;
}

.product-card:hover {
    transform: translateY(-6px);
}

.product-card img {
    width: 100%;
    height: 220px;

    object-fit: cover;
}

.product-info {
    padding: 20px;
}

.product-info h3 {
    margin-bottom: 10px;
    color: var(--dark);
}

.price {
    font-size: 1.25rem;
    font-weight: bold;

    color: var(--green);

    margin-bottom: 15px;
}

.add-btn {
    width: 100%;

    border: 0;
    border-radius: 25px;

    padding: 12px;

    background: var(--green);
    color: white;

    font-weight: bold;
    cursor: pointer;
}

.add-btn:hover {
    background: #0d692e;
}

/* FEATURES */

.features {
    background: var(--dark);
    color: white;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);

    gap: 20px;
    text-align: center;
}

.feature {
    padding: 20px;
}

.feature h3 {
    color: var(--accent);
    margin-bottom: 10px;
}

/* CART */

.cart-panel {
    display: none;

    position: fixed;
    right: 20px;
    top: 90px;

    width: min(380px, calc(100vw - 40px));
    max-height: 75vh;

    overflow: auto;

    background: white;

    z-index: 200;

    border-radius: 18px;
    padding: 20px;

    box-shadow: 0 15px 45px rgba(0, 0, 0, .25);
}

.cart-panel.show {
    display: block;
}

.cart-item {
    display: flex;
    justify-content: space-between;

    gap: 15px;

    padding: 12px 0;

    border-bottom: 1px solid #eee;
}

.remove {
    border: 0;

    background: #d94b4b;
    color: white;

    padding: 5px 9px;
    border-radius: 8px;

    cursor: pointer;
}

.cart-total {
    font-size: 1.2rem;
    font-weight: bold;

    margin-top: 18px;
}

.empty {
    text-align: center;
    color: #777;
    padding: 35px;
}

/* FOOTER */

footer {
    background: #082617;
    color: #c9d5cc;

    text-align: center;
    padding: 25px;
}

/* RESPONSIVE */

@media (max-width: 900px) {

    .links {
        display: none;
    }

    .search {
        margin-left: auto;
    }

    .category-grid,
    .product-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .feature-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {

    nav {
        padding: 0 4%;
        gap: 10px;
    }

    .logo {
        font-size: 1.35rem;
    }

    .search {
        width: 130px;
    }

    .category-grid,
    .product-grid,
    .feature-grid {
        grid-template-columns: 1fr;
    }

    .hero {
        min-height: 500px;
    }

    .hero h1 {
        font-size: 3.1rem;
    }

    section {
        padding: 60px 5%;
    }
}

</style>
</head>

<body>

<nav>

    <div class="logo">
        🌿 Fresh <span>Mart</span>
    </div>

    <ul class="links">
        <li><a href="#home">Home</a></li>
        <li><a href="#categories">Categories</a></li>
        <li><a href="#shop" onclick="showCategory('all')">Shop</a></li>
    </ul>

    <input
        id="searchInput"
        class="search"
        type="search"
        placeholder="Search products..."
        oninput="searchProducts()"
    >

    <button class="cart-button" onclick="toggleCart()">
        🛒 Cart (<span id="cartCount">0</span>)
    </button>

</nav>


<main>

<section class="hero" id="home">

    <div class="hero-content">

        <h1>
            Fresh & Healthy
            <span>Every Day</span>
        </h1>

        <p>
            Premium vegetables, delicious fruits and refreshing
            natural juices — fresh from nature to your home.
        </p>

        <a
            class="btn"
            href="#shop"
            onclick="showCategory('all')"
        >
            Shop Now →
        </a>

    </div>

</section>


<section class="categories" id="categories">

    <div class="title">
        <h2>Shop by Category</h2>
        <p>Choose fresh, healthy and delicious products.</p>
    </div>

    <div class="category-grid">

        <div
            class="category"
            onclick="showCategory('Vegetables')"
        >
            <img
                src="https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=900&q=80"
                alt="Fresh vegetables"
            >

            <div>🥬 Vegetables</div>
        </div>


        <div
            class="category"
            onclick="showCategory('Fruits')"
        >
            <img
                src="https://images.unsplash.com/photo-1619566636858-adf3ef46400b?auto=format&fit=crop&w=900&q=80"
                alt="Fresh fruits"
            >

            <div>🍎 Fruits</div>
        </div>


        <div
            class="category"
            onclick="showCategory('Juices')"
        >
            <img
                src="https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?auto=format&fit=crop&w=900&q=80"
                alt="Fresh juices"
            >

            <div>🥤 Fresh Juices</div>
        </div>

    </div>

</section>


<section id="shop">

    <div class="title">

        <h2>Fresh Products</h2>

        <p id="shopMessage">
            Everything fresh, just for you.
        </p>

    </div>


    <div class="product-grid">

        {% for product in products %}

        <article
            class="product-card"
            data-name="{{ product.name|lower }}"
            data-category="{{ product.category }}"
        >

            <img
                src="{{ product.image }}"
                alt="{{ product.name }}"
                onerror="this.style.display='none'"
            >

            <div class="product-info">

                <h3>{{ product.name }}</h3>

                <div class="price">
                    ₹{{ product.price }}
                </div>

                <button
                    class="add-btn"
                    onclick='addToCart({{ product|tojson }})'
                >
                    Add to Cart 🛒
                </button>

            </div>

        </article>

        {% endfor %}

    </div>


    <div
        id="noResults"
        class="empty"
        style="display:none"
    >
        No products found.
    </div>

</section>


<section class="features">

    <div class="feature-grid">

        <div class="feature">
            <h3>🌱 100% Fresh</h3>
            <p>Carefully selected quality produce.</p>
        </div>

        <div class="feature">
            <h3>🚚 Fast Delivery</h3>
            <p>Fresh groceries delivered quickly.</p>
        </div>

        <div class="feature">
            <h3>🔒 Secure Payments</h3>
            <p>Simple and secure shopping.</p>
        </div>

        <div class="feature">
            <h3>💚 Healthy Living</h3>
            <p>Better food for a better life.</p>
        </div>

    </div>

</section>

</main>


<aside class="cart-panel" id="cartPanel">

    <h2>Your Cart</h2>

    <div id="cartItems"></div>

    <div class="cart-total">
        Total: ₹<span id="cartTotal">0</span>
    </div>

</aside>


<footer>
    © 2026 Fresh Mart • Fresh Food • Healthy Life
</footer>


<script>

let cart = [];


/* CATEGORY FILTER */

function showCategory(category) {

    document.getElementById("searchInput").value = "";

    document
        .querySelectorAll(".product-card")
        .forEach(function(card) {

            if (
                category === "all" ||
                card.dataset.category === category
            ) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }

        });

    document
        .getElementById("noResults")
        .style.display = "none";

    if (category === "all") {
        document.getElementById("shopMessage").textContent =
            "Everything fresh, just for you.";
    } else {
        document.getElementById("shopMessage").textContent =
            "Showing fresh " + category.toLowerCase() + ".";
    }
}


/* SEARCH */

function searchProducts() {

    const term =
        document
            .getElementById("searchInput")
            .value
            .toLowerCase()
            .trim();

    let visible = 0;

    document
        .querySelectorAll(".product-card")
        .forEach(function(card) {

            const match =
                card.dataset.name.includes(term) ||
                card.dataset.category
                    .toLowerCase()
                    .includes(term);

            if (match) {
                card.style.display = "block";
                visible++;
            } else {
                card.style.display = "none";
            }

        });

    if (visible === 0) {
        document
            .getElementById("noResults")
            .style.display = "block";
    } else {
        document
            .getElementById("noResults")
            .style.display = "none";
    }
}


/* ADD TO CART */

function addToCart(product) {

    const item =
        cart.find(function(p) {
            return p.id === product.id;
        });

    if (item) {
        item.quantity++;
    } else {

        cart.push({
            ...product,
            quantity: 1
        });

    }

    renderCart();
}


/* REMOVE FROM CART */

function removeFromCart(id) {

    cart =
        cart.filter(function(item) {
            return item.id !== id;
        });

    renderCart();
}


/* RENDER CART */

function renderCart() {

    const container =
        document.getElementById("cartItems");

    const count =
        cart.reduce(
            function(sum, item) {
                return sum + item.quantity;
            },
            0
        );

    const total =
        cart.reduce(
            function(sum, item) {
                return sum + item.price * item.quantity;
            },
            0
        );

    document
        .getElementById("cartCount")
        .textContent = count;

    document
        .getElementById("cartTotal")
        .textContent = total;


    if (cart.length === 0) {

        container.innerHTML =
            '<p class="empty">Your cart is empty.</p>';

        return;
    }


    container.innerHTML =
        cart.map(function(item) {

            return `
                <div class="cart-item">

                    <div>

                        <strong>${item.name}</strong>

                        <br>

                        ₹${item.price} × ${item.quantity}

                    </div>

                    <button
                        class="remove"
                        onclick="removeFromCart(${item.id})"
                    >
                        Remove
                    </button>

                </div>
            `;

        }).join("");

}


/* SHOW / HIDE CART */

function toggleCart() {

    document
        .getElementById("cartPanel")
        .classList
        .toggle("show");

}


renderCart();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        products=products
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )