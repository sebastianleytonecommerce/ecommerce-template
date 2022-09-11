from flask import Flask, render_template, g
from dal import products

app = Flask(__name__)

config_dict = {"page_name": "Pepito Ventas",
               "telefono": "099151172"
               }


@app.route('/')
def index():
    product_list = products.ProductsDB().get_visible_products()
    category_list = list(set([p['category'].capitalize() for p in products.ProductsDB().get_visible_products()]))
    print(category_list)
    return render_template('index.html', product_list=product_list, category_list=category_list)


@app.route('/<category>')
def products_by_category(category):
    product_list = products.ProductsDB().get_products_by_category(category)
    category_list = list(set([p['category'].capitalize() for p in products.ProductsDB().get_visible_products()]))
    return render_template('index.html', product_list=product_list, category_list=category_list)


@app.route('/product/<product_id>')
def product_by_id(product_id):
    product = products.ProductsDB().get_product_by_id(product_id)
    category_list = list(set([p['category'].capitalize() for p in products.ProductsDB().get_visible_products()]))
    return render_template('index.html', product=product, category_list=category_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
