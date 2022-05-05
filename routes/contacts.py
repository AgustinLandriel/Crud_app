from flask import Blueprint, flash, redirect, render_template, request, url_for, flash
from models.contact import Contact
from utils.db import db

# Creamos nuestro blueprint para organizar mejor los modulos
contacts = Blueprint("contacts", __name__)


@contacts.route("/")
def index():
    contact_list = Contact.query.all()
    return render_template("index.html", contacts=contact_list)


@contacts.route("/new", methods=["POST"])
def add_contact():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    contactoNuevo = Contact(fullname=fullname, email=email, phone=phone)

    db.session.add(contactoNuevo)
    db.session.commit()

    flash("Contact add successfully")

    return redirect(url_for("contacts.index"))


@contacts.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    contact = Contact.query.get(id)
    if request.method == "POST":
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]

        db.session.commit()
        flash("Contact update successfully")
        return redirect(url_for("contacts.index"))

    return render_template("update.html", contact=contact)


@contacts.route("/about")
def about():
    return render_template("about.html")


@contacts.route("/delete/<id>")
def delete(id):
    id = Contact.query.get(id)
    db.session.delete(id)
    db.session.commit()
    flash("Contact delete successfully")
    return redirect(url_for("contacts.index"))
