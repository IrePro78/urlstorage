from repositories.urls import save, fetch_categories, fetch_urls
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    print(request.get_json())
    return 'Tutaj zaraz będzie dodawanie!'


@app.route('/categories')
def get_categories():
    categories = fetch_categories()
    return jsonify(categories)


@app.route('/category/<name>')
def get_category(name: str):
    urls = fetch_urls(name)
    print(urls)
    return jsonify(urls)


