
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from db import *

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/images"


# Login page
@app.route("/login")
def login():
    return render_template("login.html")


# Authenticate user
@app.route("/auth", methods=["POST"])
def auth():
    username = request.form.get("username")
    password = request.form.get("password")

    result = authenticate_user(username, password)

    if result:
        if result["role"] == "admin":
            return render_template("admindashboard.html")

    return "Invalid credentials"


# Add product
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        try:
            file = request.files.get("image_url")

            if file and file.filename:
                filename = secure_filename(file.filename)

                os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

                file.save(
                    os.path.join(app.config["UPLOAD_FOLDER"], filename)
                )

                id = request.form.get("id")
                product_name = request.form.get("product_name")
                description = request.form.get("description")
                price = request.form.get("price")
                stock = request.form.get("stock")

                image_url = f"static/images/{filename}"

                insert_record_products(
                    id, product_name, description,
                    price, stock, image_url
                )

                return render_template(
                    "admindashboard.html",
                    message="Product uploaded successfully"
                )

            return render_template("admindashboard.html", message="Please select a product image")

        except Exception as e:
            return render_template(
                "admindashboard.html",
                message="Something went wrong: " + str(e)
            )

    return render_template("admindashboard.html")


# View products
@app.route("/ad-products", methods=["GET"])
def view_products():
    products = select_records_products()
    return render_template("admindashboard.html", products=products)


# Edit product page
@app.route("/edit-product", methods=["GET", "POST"])
def edit_product():
    products = select_records_products()

    return render_template(
        "admin_edit.html",
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True)
