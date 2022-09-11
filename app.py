from flask import Flask, render_template
from dal import products
app = Flask(__name__)


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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
