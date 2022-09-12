from flask import Flask, render_template, request, redirect
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
    return render_template('product.html', product=product, category_list=category_list)

@app.route('/admin/add_product', methods=['GET'])
def add_product():
    category_list = list(set([p['category'].capitalize() for p in products.ProductsDB().get_visible_products()]))
    return render_template('add_product.html', category_list=category_list)

@app.route('/admin/add_product_form')
def add_product_form():
    args = request.args
    p_id = args['id']
    name = args['name']
    description = args['description']
    price = args['price']
    sale_price = args['sale_price']
    on_sale = 'on_sale' in request.args.keys()
    category = args['category']
    extra = args['extra']
    visible = 'visible' in request.args.keys()
    products.ProductsDB().insert_product(p_id, name, description, price, sale_price, int(on_sale), category, extra, int(visible))
    #print(visible)
    category_list = list(set([p['category'].capitalize() for p in products.ProductsDB().get_visible_products()]))
    #return render_template('add_product.html', category_list=category_list)
    return redirect(f'/product/{p_id}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
