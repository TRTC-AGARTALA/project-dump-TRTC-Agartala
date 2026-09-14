from flask import Flask, render_template, request, redirect, url_for, session, flash
from pathlib import Path
import json, uuid

app = Flask(__name__)
app.secret_key = "replace-this-with-a-random-secret-key"

BASE = Path(__file__).parent
PRODUCTS_FILE = BASE / "data" / "products.json"
ORDERS_FILE = BASE / "data" / "orders.json"

def load_json(path, default):
    if not path.exists():
        path.write_text(json.dumps(default, indent=2), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))

def save_json(path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")

def cart_items():
    products = load_json(PRODUCTS_FILE, [])
    cart = session.get("cart", {})
    items, total = [], 0
    for pid, qty in cart.items():
        product = next((p for p in products if str(p["id"]) == str(pid)), None)
        if product:
            qty = int(qty)
            subtotal = product["price"] * qty
            items.append({"product": product, "qty": qty, "subtotal": subtotal})
            total += subtotal
    return items, total

@app.context_processor
def inject_cart():
    items, total = cart_items()
    return {"cart_count": sum(x["qty"] for x in items), "cart_total": total}

@app.route("/")
def home():
    products = load_json(PRODUCTS_FILE, [])
    category = request.args.get("category", "")
    q = request.args.get("q", "").strip().lower()
    if category:
        products = [p for p in products if p["category"].lower() == category.lower()]
    if q:
        products = [p for p in products if q in p["name"].lower() or q in p["category"].lower()]
    categories = sorted(set(p["category"] for p in load_json(PRODUCTS_FILE, [])))
    return render_template("index.html", products=products, categories=categories,
                           selected_category=category, q=request.args.get("q",""))

@app.route("/product/<int:product_id>")
def product(product_id):
    products = load_json(PRODUCTS_FILE, [])
    p = next((x for x in products if x["id"] == product_id), None)
    if not p:
        return "Product not found", 404
    return render_template("product.html", product=p)

@app.post("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    products = load_json(PRODUCTS_FILE, [])
    if not any(p["id"] == product_id for p in products):
        return "Product not found", 404
    cart = session.setdefault("cart", {})
    key = str(product_id)
    cart[key] = int(cart.get(key, 0)) + 1
    session.modified = True
    flash("Product added to cart.", "success")
    return redirect(request.referrer or url_for("home"))

@app.route("/cart")
def cart():
    items, total = cart_items()
    return render_template("cart.html", items=items, total=total)

@app.post("/cart/update")
def update_cart():
    cart = session.get("cart", {})
    for key, value in request.form.items():
        if key.startswith("qty_"):
            pid = key[4:]
            try:
                qty = max(0, min(99, int(value)))
            except ValueError:
                qty = 1
            if qty == 0:
                cart.pop(pid, None)
            else:
                cart[pid] = qty
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.post("/cart/remove/<int:product_id>")
def remove_cart(product_id):
    cart = session.get("cart", {})
    cart.pop(str(product_id), None)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    items, total = cart_items()
    if not items:
        return redirect(url_for("home"))
    if request.method == "POST":
        name = request.form.get("name","").strip()
        phone = request.form.get("phone","").strip()
        address = request.form.get("address","").strip()
        if not name or not phone or not address:
            flash("Please fill in all delivery details.", "error")
            return render_template("checkout.html", items=items, total=total)
        orders = load_json(ORDERS_FILE, [])
        order_id = "QC-" + uuid.uuid4().hex[:8].upper()
        orders.append({
            "order_id": order_id,
            "customer": {"name": name, "phone": phone, "address": address},
            "items": [{"id": x["product"]["id"], "name": x["product"]["name"],
                       "qty": x["qty"], "price": x["product"]["price"]} for x in items],
            "total": total,
            "payment": "Cash on Delivery",
            "status": "Order placed"
        })
        save_json(ORDERS_FILE, orders)
        session["cart"] = {}
        return render_template("success.html", order_id=order_id, total=total, name=name)
    return render_template("checkout.html", items=items, total=total)

if __name__ == "__main__":
    app.run(debug=True)
