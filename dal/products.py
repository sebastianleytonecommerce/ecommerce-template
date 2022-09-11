import sqlite3
from dal import database_base

DB_NAME = 'products'
COLUMNS_LIST = ['name', 'description', 'price', 'sale_price', 'on_sale', 'category', 'extra', 'visible']


class ProductsDB(database_base.DBConnection):
    def __init__(self):
        super().__init__(DB_NAME)

    def create_products_db(self):
        # name, description, price, sale_price, on_sale, extra, category
        self.create_table(DB_NAME, COLUMNS_LIST)

    def get_all_products(self):
        products = self.query('SELECT * FROM products')
        return products

    def get_visible_products(self):
        products = self.query('SELECT * FROM products where visible = 1')
        return products

    def get_not_visible_products(self):
        products = self.query('SELECT * FROM products where visible = 0')
        return products

    def get_products_by_category(self, category):
        products = self.query(f"SELECT * FROM products where visible = 1 and category = '{category}'")
        return products

    def get_product_by_id(self, product_id):
        product = self.query(f'SELECT * FROM product WHERE id = {product_id}')
        return product[0]

    def insert_product(self, id, name, desc, price, sale_price, on_sale, category, extra, visible):
        sql = f"INSERT INTO {DB_NAME} (id,name, description, price, sale_price, on_sale, category, extra, visible) VALUES ({id}, '{name}', '{desc}', {price}, {sale_price}, {on_sale}, '{category}', '{extra}', {visible})"
        self.execute(sql)

    def insert_products_bulk(self, product_list):
        for p in product_list:
            self.insert_product(p['id'], p['name'], p['description'], p['price'], p['sale_price'], p['on_sale'],
                                p['category'], p['extra'], p['visible'])

    def update_product_name(self, product_id, name):
        sql = f"UPDATE {DB_NAME} set name = '{name}' where id = {product_id}"
        self.execute(sql)

    def update_product_description(self, product_id, description):
        sql = f"UPDATE {DB_NAME} set name = '{description}' where id = {product_id}"
        self.execute(sql)

    def update_product_price(self, product_id, price):
        sql = f"UPDATE {DB_NAME} set name = '{price}' where id = {product_id}"
        self.execute(sql)

    def update_product_sale_price(self, product_id, sale_price):
        sql = f"UPDATE {DB_NAME} set name = {sale_price} where id = {product_id}"
        self.execute(sql)

    def update_product_sale_flag(self, product_id, sale_flag):
        sql = f"UPDATE {DB_NAME} set sale_flag = {sale_flag} where id = {product_id}"
        self.execute(sql)

    def update_product_category(self, product_id, category):
        sql = f"UPDATE {DB_NAME} set name = '{category}' where id = {product_id}"
        self.execute(sql)

    def update_product_extra(self, product_id, extra):
        sql = f"UPDATE {DB_NAME} set name = '{extra}' where id = {product_id}"
        self.execute(sql)

    def update_product_visible(self, product_id, visible):
        sql = f"UPDATE {DB_NAME} set visible = {visible} where id = {product_id}"
        self.execute(sql)


# self.insert_product(p['name'], p['description'], p['price'], p['sale_price'], p['on_sale'], p['category'], p['extra'], p['visible'])
#db = ProductsDB()

#db.create_products_db()
'''
p_list = [
    {'id': 5, 'name': 'Pan con manteca', 'description': 'Rico pan untado con manteca sin sal', 'price': 20.00, 'sale_price': 15.00, 'on_sale': 0, 'category': 'comida', 'extra': '', 'visible':1},
    {'id': 6, 'name': 'Camello verde', 'description': 'Increible camello verde de plastico', 'price': 500.00, 'sale_price': 250.00, 'on_sale': 0, 'category': 'juguete', 'extra': '', 'visible':1},
    {'id': 7, 'name': 'Pan con manteca', 'description': 'Rico pan untado con manteca sin sal', 'price': 20.00, 'sale_price': 15.00, 'on_sale': 1, 'category': 'comida', 'extra': '', 'visible':1},
    {'id': 8, 'name': 'Pan con manteca21', 'description': 'Rico pan untado con manteca sin sal', 'price': 120.00, 'sale_price': 15.00, 'on_sale': 0, 'category': 'comida', 'extra': '', 'visible':1},
    {'id': 9, 'name': 'Pan con manteca 2', 'description': 'Rico pan untado con manteca sin sal', 'price': 200.00, 'sale_price': 115.00, 'on_sale': 1, 'category': 'pauli', 'extra': '', 'visible':1},
    {'id': 10, 'name': 'Pan con manteca 11', 'description': 'Rico pan untado con manteca sin sal', 'price': 120.00, 'sale_price': 15.00, 'on_sale': 1, 'category': 'pauli', 'extra': '', 'visible':1},
    {'id': 11, 'name': 'Pan con manteca 12 ', 'description': 'Rico pan untado con manteca sin sal', 'price': 220.00, 'sale_price': 15.00, 'on_sale': 1, 'category': 'patos', 'extra': '', 'visible':1},
    {'id': 12, 'name': 'Pan con manteca 13', 'description': 'Rico pan untado con manteca sin sal', 'price': 20.00, 'sale_price': 15.00, 'on_sale': 0, 'category': 'patos', 'extra': '', 'visible':1},
]
'''
#db.insert_products_bulk(p_list)
'''
print("--ALL--")
print(db.get_all_products())
print("--VISIBLE--")
print(db.get_visible_products())
print("--NOT VISIBLE--")
print(db.get_not_visible_products())
db.close()
'''
