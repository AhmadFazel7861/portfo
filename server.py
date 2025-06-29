from flask import Flask, render_template, request, redirect, url_for
import csv
import logging
from jinja2 import TemplateNotFound
import os

app = Flask(__name__)
print(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/currency-converter.html")
def currencyconverter():
    return render_template("currency-converter.html")


@app.route("/Object-Detection-and-Analysis.html")
def Object():
    return render_template("Object-Detection-and-Analysis.html")


@app.route("/personal-portfo.html")
def personalportfo():
    return render_template("personal-portfo.html")


@app.route("/todo-list.html")
def todolist():
    return render_template("todo-list.html")

