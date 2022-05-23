import sqlite3
import PySimpleGUI as sg
from datetime import timedelta, date
import random
import re
import datetime
now=datetime.datetime.now()
# DB Connect

con = sqlite3.connect('database.db')
print(con)
cur = con.cursor()

class project_ui:
    def __init__(self):
        self.layout = None
        self.window = None
        self.login_user_name = 0
        self.login_user_type = 0
        self.sup_id = 0
        self.ship_id = 0
        self.cust_id = 0
        self.total_price = 0
        self.order_id = 0


    def window_welcome(self):

        self.layout = [[sg.Text('Welcome to the Online Shopping System. Please enter your information.')],
                       [sg.Button('New Customer')],
                       [sg.Button('New Supplier')],
                       [sg.Button('New Shipment Company')],
                       [sg.Button('Login Screen')]]
        return sg.Window('Login Window', self.layout)

    def window_login(self):
        self.layout = [[sg.Text('Please enter your information to login your account')],
                       [sg.Text('User_name:', size=(10, 1)), sg.Input(size=(10, 1), key='user_name')],
                       [sg.Text('Password:', size=(10, 1)), sg.Input(size=(10, 1), key='password')],
                       [sg.Button('Login'), sg.Button('Back to Main')]]
        return sg.Window('Login Window', self.layout)

    def window_sup(self):
        self.layout = [
            [sg.Button('Add a new product!')],
            [sg.Button('Delete a product')],
            [sg.Button('Update a product')],
            [sg.Button('List your orders')],
            [sg.Button("Start a Discount Campaign")],
            [sg.Button('Logout')]]

        return sg.Window('Supplier Window', self.layout)

    def window_ship(self):
        self.layout=[
            [sg.Button('Show all shipments!')],
            [sg.Button('Logout')]
        ]

        return sg.Window('Shipment Company Window', self.layout)

    def window_cust(self):
        self.layout=[]
        cur.execute('SELECT CAT_NAME from category')
        cats=cur.fetchall()
        cat_list=[]
        for el in cats:
            cat_list.append(el[0])
        self.layout = [
            [sg.Button('List the products'),sg.Listbox(values=cat_list, size=(20, 5), key='cat', select_mode='extended')],
            [sg.Button('Old Orders')],
            [sg.Button('Logout')]]

        return sg.Window('Customer Window', self.layout)

    def window_create_supplier(self):
        self.layout = [[sg.Text('user_name:', size=(12, 1)), sg.Input(key='user_name', size=(10, 1))],
                       [sg.Text('name:', size=(12, 1)), sg.Input(key='name', size=(10, 1))],
                       [sg.Text('surname:', size=(12, 1)), sg.Input(key='surname', size=(10, 1))],
                       [sg.Text('phone_number:', size=(12, 1)), sg.Input(key='pno', size=(10, 1))],
                       [sg.Text('password:', size=(12, 1)), sg.Input(key='pword', size=(10, 1))],
                       [sg.Text('e_mail:', size=(12, 1)), sg.Input(key='mail', size=(10, 1))],
                       [sg.Text('shop_name:', size=(12, 1)), sg.Input(key='shop_name', size=(10, 1))],
                       [sg.Text('url:', size=(12, 1)), sg.Input(key='url', size=(10, 1))],
                       [sg.Text('work_address:', size=(12, 1)), sg.Input(key='work_address', size=(10, 1))],

                       [sg.Button('Enrol'), sg.Button('Back to Main')]]
        # print(layout)
        # cur.execute("params")
        return sg.Window('Enrol Window', self.layout)
    def window_create_customer(self):
        self.layout = [[sg.Text('user_name:', size=(12, 1)), sg.Input(key='user_name', size=(10, 1))],
                       [sg.Text('name:', size=(12, 1)), sg.Input(key='name', size=(10, 1))],
                       [sg.Text('surname:', size=(12, 1)), sg.Input(key='surname', size=(10, 1))],
                       [sg.Text('phone_number:', size=(12, 1)), sg.Input(key='pno', size=(10, 1))],
                       [sg.Text('password:', size=(12, 1)), sg.Input(key='pword', size=(10, 1))],
                       [sg.Text('e_mail:', size=(12, 1)), sg.Input(key='mail', size=(10, 1))],
                       [sg.Listbox(['Cash', 'EFT', 'Online', 'Credit Card'], size=(20, 5), key='pay')],
                       # [sg.Text('default_payment_method:', size=(12, 1)), sg.Input(key='default_payment_method', size=(10, 1))],
                       [sg.Text('address:', size=(12, 1)), sg.Input(key='address', size=(10, 1))],
                       [sg.Button('Enrol'), sg.Button('Back to Main')]]
        # print(layout)
        # cur.execute("params")
        return sg.Window('Enrol Window', self.layout)
    def window_create_shipment_comp(self):
        self.layout = [[sg.Text('user_name:', size=(12, 1)), sg.Input(key='user_name', size=(10, 1))],
                       [sg.Text('name:', size=(12, 1)), sg.Input(key='name', size=(10, 1))],
                       [sg.Text('surname:', size=(12, 1)), sg.Input(key='surname', size=(10, 1))],
                       [sg.Text('phone_number:', size=(12, 1)), sg.Input(key='pno', size=(10, 1))],
                       [sg.Text('password:', size=(12, 1)), sg.Input(key='pword', size=(10, 1))],
                       [sg.Text('e_mail:', size=(12, 1)), sg.Input(key='mail', size=(10, 1))],
                       [sg.Text('number_truck:', size=(12, 1)), sg.Input(key='num_truck', size=(10, 1))],
                       [sg.Button('Enrol'), sg.Button('Back to Main')]]
        # print(layout)
        # cur.execute("params")
        return sg.Window('Enrol Window', self.layout)
    def insert_shipment_comp(self, values):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        user_list = []
        u_name = values['user_name']
        p_name = values['name']
        p_surname = values['surname']
        password = values['pword']
        phone_number = values['pno']
        try:
            abcdd=int(phone_number)
            int_flag=1
        except:
            int_flag=0
        e_mail = values['mail']
        num_trucks = values['num_truck']
        try:
            sadss=int(num_trucks)
            t_flag=1
        except:
            t_flag=0
        cur.execute('SELECT user_name FROM user')
        a = list(cur.fetchall())
        print(a)
        for i in range(0, len(a)):
            user_list.append((a[i][0]))
        if u_name in user_list:
            sg.popup('User Name already taken')
        else:
            if u_name == '' or p_name == '' or p_surname == '' or password == '' or phone_number == '' or e_mail == '' or num_trucks=='':
                sg.popup('All areas must be filled!')
            elif not (re.fullmatch(regex, e_mail)):
                sg.popup('Invalid Email')
            elif len(phone_number) != 10 or not int_flag:
                sg.popup('Wrong Tel no!')
            elif not t_flag:
                sg.popup('Number of Trucks should be integer')
            else:
                cur.execute('SELECT MAX(shipment_id) FROM shipment_company')
                row = cur.fetchone()
                id = int(row[0]) + 1
                cur.execute('INSERT INTO User VALUES (?,?,?,?,?,?)',
                            (u_name, p_name, p_surname, phone_number, password, e_mail))
                cur.execute('INSERT INTO shipment_company VALUES (?,?,?)', (id, int(num_trucks), u_name))
                con.commit()
                self.window.close()
                self.window = self.window_welcome()

    def insert_customer(self, values):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


        user_list = []
        u_name = values['user_name']
        p_name = values['name']
        p_surname = values['surname']
        password = values['pword']
        phone_number = values['pno']
        try:
            abcdd=int(phone_number)
            int_flag=1
        except:
            int_flag=0
        e_mail = values['mail']
        default_payment_method = values['pay'][0]
        address = values['address']
        cur.execute('SELECT user_name FROM user')
        a = list(cur.fetchall())
        print(a)
        for i in range(0, len(a)):
            user_list.append((a[i][0]))
        if u_name in user_list:
            sg.popup('User Name already taken')
        else:
            if u_name == '' or p_name == '' or p_surname == '' or password == '' or phone_number == '' or e_mail == '' or address=='':
                sg.popup('All areas must be filled!')
            elif not (re.fullmatch(regex, e_mail)):
                sg.popup('Invalid Email')
            elif len(phone_number) != 10 or not int_flag:
                sg.popup('Wrong Tel no!')
            else:
                cur.execute('SELECT MAX(customer_id) FROM customer')
                row = cur.fetchone()
                id = int(row[0]) + 1
                cur.execute('INSERT INTO User VALUES (?,?,?,?,?,?)',
                            (u_name, p_name, p_surname, phone_number, password, e_mail))
                cur.execute('INSERT INTO customer VALUES (?,?,?,?,?)', (id, address, default_payment_method, 1, u_name))
                con.commit()
                self.window.close()
                self.window = self.window_welcome()

    def insert_supplier(self, values):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        user_list = []
        u_name = values['user_name']
        p_name = values['name']
        p_surname = values['surname']
        password = values['pword']
        phone_number = values['pno']
        try:
            abcdd=int(phone_number)
            int_flag=1
        except:
            int_flag=0
        e_mail = values['mail']
        shop_name = values['shop_name']
        url = values['url']
        work_address = values['work_address']
        cur.execute('SELECT user_name FROM user')
        a = list(cur.fetchall())
        print(a)
        for i in range(0, len(a)):
            user_list.append((a[i][0]))
        if u_name in user_list:
            sg.popup('User Name already taken')
        else:
            if u_name == '' or p_name == '' or p_surname == '' or password == '' or phone_number == '' or e_mail == '' or shop_name=='' or url=='' or work_address=='':
                sg.popup('All areas must be filled!')
            elif not (re.fullmatch(regex, e_mail)):
                sg.popup('Invalid Email')
            elif len(phone_number) != 10 or not int_flag:
                sg.popup('Wrong Tel no!')
            else:
                cur.execute('SELECT MAX(sup_id) FROM supplier')
                row = cur.fetchone()
                id = int(row[0]) + 1
                cur.execute('INSERT INTO User VALUES (?,?,?,?,?,?)',
                            (u_name, p_name, p_surname, phone_number, password, e_mail))
                cur.execute('INSERT INTO supplier VALUES (?,?,?,?,?)', (id, url, shop_name, work_address, u_name))
                con.commit()
                self.window.close()
                self.window = self.window_welcome()

    def window_add_product(self):
        cat = []
        for row in cur.execute('SELECT DISTINCT CAT_NAME FROM category'):
            cat.append(row)
        self.layout = [[sg.Text('description:', size=(12, 1)), sg.Input(key='description', size=(10, 1))],
                       [sg.Text('price:', size=(12, 1)), sg.Input(key='price', size=(10, 1))],
                       [sg.Text('stock count:', size=(12, 1)), sg.Input(key='stock_count', size=(10, 1))],
                       [sg.Text('supplier id:' + str(self.sup_id))],
                       [sg.Listbox(cat, size=(20, 5), key='cat')],
                       [sg.Button('Add')], [sg.Button('Back to Supplier Menu')]]

        return sg.Window('Add Window_', self.layout)

    def window_delete_product(self):
        products = []

        for product in cur.execute('SELECT product_id, description FROM products_supplies WHERE sup_id = ?',
                                   (self.sup_id,)):
            products.append(product)

        if len(products) == 0:
            sg.popup("There is no product for this user")
            return self.window_sup()
        self.layout = [[sg.Listbox(products, size=(40, 10), key='pid')],
                       [sg.Button('Delete'), sg.Button('Back to Supplier Menu')]]

        return sg.Window('Delete Product', self.layout)

    def insert_product(self, values):

        cur.execute('SELECT MAX(product_id) FROM products_supplies')
        row = int(cur.fetchone()[0])

        product_id = row + 1
        description = values['description']
        price = values['price']
        stock_count = values['stock_count']
        cat_name = values['cat']
        print(cat_name)
        cur.execute('SELECT description FROM products_supplies WHERE description=?', (description,))
        products = cur.fetchone()
        print(products)
        if products is not None:
            sg.popup('Already Added Product!')
        else:
            if len(cat_name) != 0:
                cat_id = ''.join(cat_name[0])
                cat_id = (cur.execute('SELECT CAT_DID FROM category WHERE CAT_NAME=?', (cat_id,)))
                cat_id = cur.fetchone()
                cat_id = cat_id[0]
                print(cat_id)
            else:
                cat_id = ''

            if (product_id == '' or description == '' or price == '' or stock_count == '' or cat_id == ''):
                sg.popup("There is missing information, try again!")
            elif not price.isnumeric() or not price.isnumeric():
                sg.popup("Price or Stock must be numeric!")


            else:
                cur.execute('INSERT INTO products_supplies VALUES (?,?,?,?,?)',
                            (product_id, description, price, stock_count, self.sup_id))
                cur.execute('INSERT INTO has2 VALUES (?,?)', (product_id, cat_id))
                con.commit()
                sg.popup("Added Successfully")
                self.window.close()
                self.window = self.window_sup()

    def window_list_products(self, values):
        try:
            filtered_cats=values['cat']
            self.yedek_val=values
        except:
            values=self.yedek_val
            filtered_cats = values['cat']
        if len (filtered_cats)==0:
            cur.execute('''SELECT products_supplies.description,  products_supplies.price,supplier.shop_name,
            CAT_NAME,products_supplies.product_id FROM category, products_supplies, has2,supplier WHERE 
            products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id
            AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 ''')
            list_pro = cur.fetchall()
            Lo=[]
            cur.execute('''SELECT products_supplies.description, supplier.shop_name,CAT_NAME,products_supplies.price, products_supplies.price*(100 - discount."%")/100 as discounted_percentage, discount."%", products_supplies.product_id
                            FROM category, products_supplies, has2,supplier, has1,discount 
                            WHERE products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 AND 
                            products_supplies.product_id=has1.product_id AND has1.discount_id = discount.discount_id AND discount.start<? and ?<discount.end''', (str(datetime.datetime.now()), str(datetime.datetime.now())))
            self.discounted_products = cur.fetchall()
            self.dpid=[]
            for i in range(len(self.discounted_products)):
                self.dpid.append(self.discounted_products[i][-1])
            print(self.discounted_products)
            for elem in self.discounted_products:
                Lo.append(elem[0])
                print(elem)
            self.layout = []
            self.layout.append(
                [sg.Text("Product", size=(15, 1)), sg.Text("Price", size=(15, 1)), sg.Text("Shop Name", size=(15, 1)),
                 sg.Text("Category", size=(15, 1))])
            for i in range(0, len(list_pro)):
                if list_pro[i][0] not in Lo:
                    print(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)), sg.Text(list_pro[i][1], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                else:
                    print(list_pro[i][0])
                    k=Lo.index(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)), sg.Text(self.discounted_products[k][4], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                cur.execute('SELECT stock_count FROM products_supplies WHERE product_id= ? ', (list_pro[i][4],))
                self.layout.append(temp)

            self.layout.append([sg.Button('Back'), sg.Button('Payment Stage'), sg.Button("See the Discounted Products")])
        elif len(filtered_cats)==1:
            additional_sql_code=f"AND CAT_NAME='{filtered_cats[0]}'"
            cur.execute('''SELECT products_supplies.description,  products_supplies.price,supplier.shop_name,
            CAT_NAME,products_supplies.product_id FROM category, products_supplies, has2,supplier WHERE 
            products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id
            AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 '''+additional_sql_code)
            list_pro = cur.fetchall()
            Lo = []
            cur.execute('''SELECT products_supplies.description, supplier.shop_name,CAT_NAME,products_supplies.price, products_supplies.price*(100 - discount."%")/100 as discounted_percentage, discount."%", products_supplies.product_id
                            FROM category, products_supplies, has2,supplier, has1,discount 
                            WHERE products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 AND 
                            products_supplies.product_id=has1.product_id AND has1.discount_id = discount.discount_id AND discount.start<? and ?<discount.end '''+additional_sql_code,
                        (str(datetime.datetime.now()), str(datetime.datetime.now())))
            self.discounted_products = cur.fetchall()
            self.dpid = []
            for i in range(len(self.discounted_products)):
                self.dpid.append(self.discounted_products[i][-1])
            print(self.discounted_products)
            for elem in self.discounted_products:
                Lo.append(elem[0])
                print(elem)
            self.layout = []
            self.layout.append(
                [sg.Text("Product", size=(15, 1)), sg.Text("Price", size=(15, 1)), sg.Text("Shop Name", size=(15, 1)),
                 sg.Text("Category", size=(15, 1))])
            for i in range(0, len(list_pro)):
                if list_pro[i][0] not in Lo:
                    print(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)), sg.Text(list_pro[i][1], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                else:
                    print(list_pro[i][0])
                    k = Lo.index(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)),
                            sg.Text(self.discounted_products[k][4], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                cur.execute('SELECT stock_count FROM products_supplies WHERE product_id= ? ', (list_pro[i][4],))
                self.layout.append(temp)

            self.layout.append(
                [sg.Button('Back'), sg.Button('Payment Stage'), sg.Button("See the Discounted Products")])
        elif len(filtered_cats)>1:
            additional_sql_code=f"AND (CAT_NAME='{filtered_cats[0]}'"
            for i in range(1, len(filtered_cats)):
                additional_sql_code += f" OR CAT_NAME='{filtered_cats[i]}'"
            additional_sql_code+=')'
            cur.execute('''SELECT products_supplies.description,  products_supplies.price,supplier.shop_name,
            CAT_NAME,products_supplies.product_id FROM category, products_supplies, has2,supplier WHERE 
            products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id
            AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 '''+additional_sql_code)
            list_pro = cur.fetchall()
            Lo = []
            cur.execute('''SELECT products_supplies.description, supplier.shop_name,CAT_NAME,products_supplies.price, products_supplies.price*(100 - discount."%")/100 as discounted_percentage, discount."%", products_supplies.product_id
                            FROM category, products_supplies, has2,supplier, has1,discount 
                            WHERE products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 AND 
                            products_supplies.product_id=has1.product_id AND has1.discount_id = discount.discount_id AND discount.start<? and ?<discount.end '''+additional_sql_code,
                        (str(datetime.datetime.now()), str(datetime.datetime.now())))
            self.discounted_products = cur.fetchall()
            self.dpid = []
            for i in range(len(self.discounted_products)):
                self.dpid.append(self.discounted_products[i][-1])
            print(self.discounted_products)
            for elem in self.discounted_products:
                Lo.append(elem[0])
                print(elem)
            self.layout = []
            self.layout.append(
                [sg.Text("Product", size=(15, 1)), sg.Text("Price", size=(15, 1)), sg.Text("Shop Name", size=(15, 1)),
                 sg.Text("Category", size=(15, 1))])
            for i in range(0, len(list_pro)):
                if list_pro[i][0] not in Lo:
                    print(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)), sg.Text(list_pro[i][1], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                else:
                    print(list_pro[i][0])
                    k = Lo.index(list_pro[i][0])
                    temp = [sg.Text(list_pro[i][0], size=(15, 1)),
                            sg.Text(self.discounted_products[k][4], size=(15, 1)),
                            sg.Text(list_pro[i][2], size=(15, 1)), sg.Text(list_pro[i][3], size=(15, 1)),
                            sg.Button("Add Product", key=(('Add', list_pro[i][4]))),
                            sg.Button("Evaluations of Product", key=(('Yorum', list_pro[i][4])))]
                cur.execute('SELECT stock_count FROM products_supplies WHERE product_id= ? ', (list_pro[i][4],))
                self.layout.append(temp)

            self.layout.append(
                [sg.Button('Back'), sg.Button('Payment Stage'), sg.Button("See the Discounted Products")])

        return sg.Window('List Products', self.layout)

    def button_login(self, values):
        uname = values['user_name']
        upass = values['password']
        if uname == '':
            sg.popup('ID cannot be empty')
        elif upass == '':
            sg.popup('Password cannot be empty')
        else:
            # first check if this is a valid user
            cur.execute('SELECT user_name, name, surname FROM user WHERE user_name = ? AND password = ?',
                        (uname, upass))
            row = cur.fetchone()
            if row is None:
                sg.popup('ID or password is wrong!')
            else:
                self.login_user_name = row[0]
                self.name_of_user = row[1]
                print(uname)
                cur.execute('SELECT user_name FROM customer WHERE user_name = ?', (uname,))
                row_customer = cur.fetchone()
                cur.execute('SELECT user_name FROM supplier WHERE user_name = ?', (uname,))
                row_supplier = cur.fetchone()
                cur.execute('SELECT user_name FROM shipment_company WHERE user_name = ?', (uname,))
                row_shipment = cur.fetchone()
                if row_shipment is not None:
                    self.login_user_type = 'Shipment'
                    sg.popup('Welcome, ' + self.name_of_user + ' ( Shipment Company)')
                    self.window.close()
                    cur.execute('SELECT shipment_id FROM shipment_company WHERE user_name=?', (uname,))
                    self.ship_id = int(cur.fetchone()[0])
                    self.window = self.window_ship()
                elif row_supplier is not None:
                    self.login_user_type = 'Supplier'
                    sg.popup('Welcome, ' + self.name_of_user + ' ( Supplier)')
                    self.window.close()
                    cur.execute('SELECT sup_id FROM supplier WHERE user_name=?', (uname,))
                    self.sup_id = int(cur.fetchone()[0])

                    self.window = self.window_sup()

                elif row_customer is not None:
                    self.login_user_type = 'Customer'
                    sg.popup('Welcome, ' + self.name_of_user + ' (Customer)')
                    self.window.close()
                    cur.execute('SELECT customer_id FROM customer WHERE user_name=?', (uname,))
                    self.cust_id = int(cur.fetchone()[0])

                    # self.cust_id = int(''.join(filter(str.isdigit, self.cust_id)))
                    self.window = self.window_cust()
                else:
                    sg.popup('DB Error')

    def update_product(self):
        products = []

        for product in cur.execute('SELECT product_id, description FROM products_supplies WHERE sup_id = ?',
                                   (self.sup_id,)):
            products.append(product)

        if len(products) == 0:
            sg.popup("There is no product for this user")
            return self.window_sup()
        self.layout = [[sg.Listbox(products, size=(20, 5), key='pid')],
                       [sg.Button('Select to Update')], [sg.Button('Back to Supplier Menu')]]

        return sg.Window('Update Product', self.layout)

    def update_details(self, values):
        details = []
        details = cur.execute('SELECT description,price,stock_count FROM products_supplies WHERE product_id = ?',
                              (values["pid"][0][0],))
        details = cur.fetchone()
        self.layout = [[sg.Text("Details:  " + details[0]), sg.Input(key='new_description', size=(10, 1))],
                       [sg.Text("Price:  " + str(details[1])), sg.Input(key='new_price', size=(10, 1))],
                       [sg.Text("stock_count:  " + str(details[2])), sg.Input(key='new_stock', size=(10, 1))],
                       [sg.Button('OK'), sg.Button('Back to Supplier Menu')]]
        return sg.Window('Update Detail', self.layout)

    def window_pay(self, cart_list, adres, payment_method):


        if len(cart_list)!=0:
            self.layout = []
            self.total_price = 0
            for el in cart_list:
                if el not in self.dpid:
                    cur.execute('SELECT price FROM products_supplies WHERE product_id = ?', (el,))
                else:
                    cur.execute('''SELECT products_supplies.price*(100 - discount."%")/100 as discounted_percentage
                                FROM category, products_supplies, has2,supplier, has1,discount 
                                WHERE products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 AND 
                                products_supplies.product_id=has1.product_id AND has1.discount_id = discount.discount_id AND products_supplies.product_id = ?  AND discount.start<? and ?<discount.end''', (el, str(datetime.datetime.now()), str(datetime.datetime.now())))
                pro_price = cur.fetchone()
                print('xty'+ str(pro_price))
                self.total_price += (pro_price[0])
                print('xxty'+ str(self.total_price))
                pro_name = cur.execute('SELECT description FROM products_supplies WHERE product_id = ?', (el,))
                pro_name = cur.fetchone()
                temp = [sg.Text((pro_name[0]), size=(15, 1)), sg.Text((pro_price[0]), size=(15, 1))]
                self.layout.append(temp)
            temp = [sg.Text('Total:' + str(self.total_price))]
            self.layout.append(temp)
            temp = [sg.Text('Payment Method:' + str(payment_method)), sg.Button('Update Payment Method')]
            self.layout.append(temp)
            temp = [sg.Text('Address:' + str(adres)), sg.Button('Update Address')]
            self.layout.append(temp)
            cur.execute('select user_name from shipment_company')
            shipment_comps=cur.fetchall()
            L1=[]
            for el in shipment_comps:
                L1.append(el[0])
            print(L1)
            temp = [sg.Text("Shipment Company: "), sg.Listbox(L1, size=(20, 5), key='shipment')]
            self.layout.append(temp)
            temp = [sg.Button('Pay!'), sg.Button('Back to Product List')]
            self.layout.append(temp)
            return sg.Window('Cart', self.layout)
        else:
            sg.popup('Please add a product to your cart!')
            return self.window_list_products(values)


    def window_address(self):
        self.layout = [[sg.Text("New Address:  "), sg.Input(key='new_address', size=(10, 1))],
                       [sg.Button('Confirm Address')]]
        return sg.Window('Update Address', self.layout)

    def window_new_payment_method(self):
        payment_types = ['Cash', 'Credit Card', 'EFT', 'Online']
        self.layout = [[sg.Listbox(payment_types, size=(20, 5), key='pay')], [sg.Button('Confirm Payment Type')]]
        return sg.Window('Update Payment Method', self.layout)

    def create_order(self, adres, payment_method, cart_list, shipment):
        cur.execute('SELECT MAX(order_id) FROM order_delivery')
        max_order = cur.fetchone()
        print(max_order)
        order_num = int(max_order[0]) + 1
        shipcompid = []
        scomp=shipment[0]
        cur.execute(f"SELECT shipment_id FROM shipment_company where user_name='{scomp}'")
        shipment_id = cur.fetchone()
        shipcompany = shipment_id[0]

        todaysDate = date.today().strftime('%d-%m-%Y')
        EndDate = date.today() + timedelta(days=3)
        estimated_delivery_date = EndDate.strftime('%d-%m-%Y')
        cur.execute('INSERT INTO order_delivery VALUES (?,?,?,?,?,?,?,?)', (
            order_num, todaysDate, adres, payment_method, estimated_delivery_date, shipcompany, self.cust_id,
            self.total_price))
        con.commit()
        unique_pro = set(cart_list)
        countvspro = dict((i, cart_list.count(i)) for i in cart_list)
        for el in unique_pro:
            count = countvspro[el]
            cur.execute('INSERT INTO include VALUES (?,?,?) ', (el, order_num, count))
            con.commit()

    def oldorders(self, cust_id):

        self.layout = []
        cur.execute(
            '''SELECT product_id FROM order_delivery, include WHERE order_delivery.order_id=include.order_id AND customer_id=? ''',
            (cust_id,))
        cur.execute('SELECT total_price, date,order_id FROM order_delivery WHERE customer_id=?', (cust_id,))
        order_ids = cur.fetchall()
        if not order_ids:
            self.layout.append([[sg.Text('No Past Order!')]])
        else:
            u = []
            for el in order_ids:
                el = {'Order_id': str(el[2]), 'Date': str(el[1]), 'Total Price ': str(el[0])}
                u.append(el)
            self.layout.append([sg.Listbox(u, size=(50, 5), key='order_id')])
            det_but = [sg.Button('Order Details')]
            self.layout.append(det_but)
        ev_order = [sg.Button('Evaluate Order-Shipment')]
        self.layout.append(ev_order)
        back_but = [sg.Button('Back')]
        self.layout.append(back_but)
        return sg.Window('Add Window', self.layout)

    def see_details(self, order_id1):
        products = []
        self.layout = []
        for row in cur.execute(
                'SELECT description, products_supplies.product_id FROM products_supplies,include WHERE '
                'include.product_id=products_supplies.product_id AND order_id=?',
                (order_id1,)):
            products.append(row)
        self.layout.append([sg.Listbox(products, size=(50, 5), key='product')])
        ev_p = [sg.Button('Evaluate Product')]
        self.layout.append(ev_p)
        back_but = [sg.Button('Back')]
        self.layout.append(back_but)
        return sg.Window('Order Detail', self.layout)

    def evaluate_shipment(self):
        list_of_points = [1, 2, 3, 4, 5]
        self.layout = [[sg.Text("Comments:  "), sg.Input(key='com', size=(20, 2))],
                       [sg.Text("Points(1-5):  "), sg.Listbox(list_of_points, size=(20, 5), key='points')],
                       [sg.Button('Approve'), sg.Button('Back')]]

        return sg.Window('Shipment Evaluation', self.layout)
    def window_show_shipment(self):
        self.layout=[[sg.Text('user_name'), sg.Text('order date'), sg.Text('Delivered?')]]
        sid=self.ship_id

        now=datetime.datetime.now()
        cur.execute(f"select u.user_name, o.date from order_delivery o, user u, customer c where o.shipment_id={sid} and c.customer_id=o.customer_id and u.user_name=c.user_name and o.estimated_delivery_date>'{now}'")
        delivered=cur.fetchall()
        cur.execute(f"select u.user_name, o.date from order_delivery o, user u, customer c where o.shipment_id={sid} and c.customer_id=o.customer_id and u.user_name=c.user_name and o.estimated_delivery_date<'{now}'")
        not_delivered=cur.fetchall()
        L_del=[]
        L_not_del=[]
        for el in delivered:
            L_del.append((el[0], el[1]))
        for el in not_delivered:
            L_not_del.append((el[0], el[1]))
        for i in range(len(L_del)):
            self.layout.append([sg.Text(L_del[i][0]), sg.Text(str(L_del[i][1])), sg.Text('Not Delivered!')])
        for i in range(len(L_not_del)):
            self.layout.append([sg.Text(L_not_del[i][0]), sg.Text(str(L_not_del[i][1])), sg.Text('Delivered!')])
        return sg.Window('Shipments', self.layout)
    def evaluate_product(self):
        list_of_points = [1, 2, 3, 4, 5]
        self.layout = [[sg.Text("Comments:  "), sg.Input(key='com', size=(20, 2))],
                       [sg.Text("Points(1-5):  "), sg.Listbox(list_of_points, size=(20, 5), key='points')],
                       [sg.Button('Evaluate'), sg.Button('Back')]]

        return sg.Window('Product Evaluation', self.layout)

    def print_ev(self, product_ev):
        self.layout = []
        self.layout.append([sg.Text("Star", size=(3, 1)), sg.Text("Comment", size=(15, 1))])
        if product_ev == []:
            self.layout.append([sg.Text("No Past Evaluations!", size=(15, 1))])
        else:
            self.layout = []
            i = 0
            for el in product_ev:
                self.layout.append([sg.Text("Comment: " + str(i + 1))])
                self.layout.append([sg.Text("Stars: " + el[0])])
                self.layout.append([sg.Text("Comment:" + el[1])])
                i += 1
        back_but = [sg.Button('Back to Product List')]
        self.layout.append(back_but)
        return sg.Window('Product Comments', self.layout)

    def sup_view_order(self):

        orders = []

        for order in cur.execute('''SELECT products_supplies.product_id, order_delivery.order_id, date, address, payment_type, estimated_delivery_date
                       FROM products_supplies, include, order_delivery 
                       WHERE products_supplies.product_id = include.product_id
                       AND include.order_id = order_delivery.order_id AND sup_id = ?''', (self.sup_id,)):
            orders.append(order)
        if len(orders) == 0:
            sg.popup("There are no orders for this supplier")
            return self.window_sup()

        self.layout = [[sg.Listbox(orders, size=(60, 15), key='pid')],
                       [sg.Button('Billing Information')], [sg.Button('Back to Supplier Menu')]]

        return sg.Window('Product Order', self.layout)

    def order_billling_info(self):
        order_info = []

        cur.execute('''SELECT shipment_company.number_truck, 
                       order_delivery.address, date, payment_type, order_delivery.shipment_id, estimated_delivery_date
                       FROM shipment_company, order_delivery, products_supplies, include 
                       WHERE shipment_company.shipment_id=order_delivery.shipment_id AND products_supplies.product_id = include.product_id
                       AND include.order_id = order_delivery.order_id AND sup_id = ?''', (self.sup_id,))
        row = cur.fetchone()
        order_info.append(row)
        if len(order_info) == 0:
            sg.popup("There are no orders for this supplier")
            return self.window_sup()

        self.layout = [[sg.Listbox(order_info, size=(60, 15), key='pid')],
                       [sg.Button('Back to Supplier Menu')], [sg.Button('List your orders')]]

        return sg.Window('Order Billing Information', self.layout)

    def discount_campaign(self):
        product_info = []

        cur.execute('''select p.product_id, p.description
                        from supplier s, products_supplies p
                        where p.sup_id = s.sup_id and s.sup_id = ?''', (self.sup_id,))
        products = cur.fetchall()
        if (len(products) == 0):
            sg.popup("There are no products of supplier")
            return self.window_sup()

        for row in products:
            product_info.append(row)

        self.layout = [[sg.Text("Select the product to discount")],
                       [sg.Listbox(product_info, size=(60, 15), key='pid', select_mode="multiple")],
                       [sg.Text("Enter Starting date (dd.mm.yyyy) :")], [sg.Input(key="Starting Date", size=(10, 1))],
                       [sg.Text("Enter Ending date (dd.mm.yyyy) :")], [sg.Input(key="Ending Date", size=(10, 1))],
                       [sg.Text("Enter Discount (percentage) :")], [sg.Input(key="Discount Percentage", size=(10, 1))],
                       [sg.Button("Apply Discount")], [sg.Button("Back to Supplier Menu")]]
        return sg.Window("Disount Campaign", self.layout)

    def discount_validation(self, values):
        Ids = values.get("pid")
        num_of_choices = len(Ids)
        starting_date = values["Starting Date"]
        ending_date = values["Ending Date"]
        discount_percentage = values["Discount Percentage"]

        try:
            start_date = datetime.datetime.strptime(starting_date, "%d.%m.%Y")
        except:
            sg.Popup("Invalid starting date")
            return self.discount_campaign()

        try:
            end_date = datetime.datetime.strptime(ending_date, "%d.%m.%Y")
        except:
            sg.Popup("Invalid ending date date")
            return self.discount_campaign()

        if (start_date > end_date):
            sg.Popup("Starting date cannot be later than ending date")
            return self.discount_campaign()

        try:
            percentage = int(discount_percentage)
        except:
            sg.Popup("Please enter a valid percentage ratio")
            return self.discount_campaign()

        if not (0 <= percentage <= 100):
            sg.Popup("Percentage should be between 0 and 100")
            return self.discount_campaign()

        for i in range(num_of_choices):
            product_id = Ids[i][0]

            cur.execute('''select product_id
                       from has1
                       where sup_id = ?''', (self.sup_id,))

            discounted_ids = cur.fetchall()
            for row in discounted_ids:
                if (str(row[0]) == str(product_id)):
                    ppup = sg.Window("Window",
                                     [[sg.Text("There is already a discount campaign assigned to that product." +
                                               " Do you want to replace it ?")], [sg.Button("Yes"), sg.Button("No")]])
                    events, values = ppup.read()
                    if (events == "No"):
                        ppup.close()
                        return self.discount_campaign()
                    else:
                        ppup.close()
                        cur.execute('''DELETE FROM has1
                                    where product_id = ?''', (int(product_id),))
                        break

            cur.execute('''select discount_id from discount''')
            lst = cur.fetchall()
            discount_ids = []
            for k in range(len(lst)):
                discount_ids.append(lst[k][0])
            discount_ids = list(map(int, discount_ids))
            max_discount_id = max(discount_ids)
            max_discount_id = max_discount_id + 1
            cur.execute('''INSERT INTO discount VALUES (?,?,?,?)''',
                        (max_discount_id, percentage, start_date, end_date))
            con.commit()
            cur.execute('''INSERT INTO has1 VALUES (?,?,?)''', (int(product_id), max_discount_id, self.sup_id))
            con.commit()
        sg.Popup("Discount(s) Applied Successfully")
        return self.discount_campaign()

    def Discount_prices(self):

        cur.execute('''SELECT products_supplies.description, supplier.shop_name,CAT_NAME,products_supplies.price, products_supplies.price*(100 - discount."%")/100 as discounted_percentage, discount."%", products_supplies.product_id
                        FROM category, products_supplies, has2,supplier, has1,discount 
                        WHERE products_supplies.product_id=has2.product_id  AND supplier.sup_id=products_supplies.sup_id AND has2.CAT_DID=category.CAT_DID AND products_supplies.stock_count >0 AND 
                        products_supplies.product_id=has1.product_id AND has1.discount_id = discount.discount_id AND discount.start<? and ?<discount.end''', (str(datetime.datetime.now()), str(datetime.datetime.now())))
        self.discounted_products = cur.fetchall()
        self.dpid=[]
        for i in range(len(self.discounted_products)):
            self.dpid.append(self.discounted_products[i][-1])
        print(self.discounted_products)
        self.layout = []
        self.layout.append(
            [sg.Text("Product", size=(15, 1)), sg.Text("Company", size=(15, 1)), sg.Text("Category", size=(15, 1)),
             sg.Text("Price", size=(15, 1)), sg.Text("Discounted_price", size=(15, 1)),
             sg.Text("Percentage", size=(15, 1))])
        for row in self.discounted_products:
            self.layout.append(
                [sg.Text(row[0], size=(15, 1)), sg.Text(row[1], size=(15, 1)), sg.Text(row[2], size=(15, 1)),
                 sg.Text(row[3], size=(15, 1)), sg.Text(row[4], size=(15, 1)), sg.Text(row[5], size=(15, 1))])
        self.layout.append([sg.Button("Back to Product list")])
        return (sg.Window("Discounted_prices", self.layout))


Xyz = project_ui()
Xyz.window = Xyz.window_welcome()
cart_list = []
shop_active = 0
while True:
    event, values = Xyz.window.read()
    print('a', event)
    print('b', values)
    print('c', shop_active)

    if shop_active == 1 and event != 'Back' and event != 'Back to Product List':

        if event == 'Payment Stage':
            shop_active = 0
            payment_method = cur.execute('SELECT default_payment_method FROM customer WHERE customer_id = ?',
                                         (Xyz.cust_id,))
            payment_method = cur.fetchone()
            payment_method = ''.join(payment_method[0])
            adres = cur.execute('SELECT address  FROM customer WHERE customer_id = ?', (Xyz.cust_id,))
            adres = cur.fetchone()
            adres = ''.join(adres[0])
            Xyz.window.close()
            Xyz.window = Xyz.window_pay(cart_list, adres, payment_method)
            if len(cart_list) == 0:
                shop_active = 1

        elif event == "Back to Product list":
            Xyz.window.close()
            Xyz.window = Xyz.window_list_products(values)


        elif event == "See the Discounted Products":
            Xyz.window.close()
            Xyz.window = Xyz.Discount_prices()




        elif event != 'Payment Stage' and event != "Back to Product list" and event != "See the Discounted Products":
            event = [event]
            d = dict(event)
            key_event = list(d.keys())[0]
            if key_event == 'Add':
                product_id = d['Add']
                cur.execute('SELECT stock_count FROM products_supplies WHERE product_id= ? ', (product_id,))
                stock_count = cur.fetchone()
                if stock_count[0] == 0:
                    sg.popup('No stock!')
                else:
                    stock_count = stock_count[0] - 1
                    print(stock_count)
                    cur.execute('UPDATE products_supplies SET stock_count= ? WHERE product_id= ? ',
                                (stock_count, product_id))
                    cart_list.append(d['Add'])
                    con.commit()
            elif key_event == 'Yorum':
                product_id = d['Yorum']
                Xyz.window.close()
                product_ev = []
                for row in cur.execute('SELECT prod_star,prod_comment FROM evaluate_product WHERE product_id= ? ',
                                       (product_id,)):
                    product_ev.append(row)
                Xyz.window = Xyz.print_ev(product_ev)

    if event == 'Back to Product List':
        Xyz.window.close()
        Xyz.window = Xyz.window_list_products(values)
        shop_active=1

    if event == 'Back to Main':
        Xyz.window.close()
        Xyz.window = Xyz.window_welcome()
    if event == 'Update Address':
        Xyz.window.close()
        Xyz.window = Xyz.window_address()
    if event == 'Update Payment Method':
        Xyz.window.close()
        Xyz.window = Xyz.window_new_payment_method()
        print(values)

    if event == 'Confirm Payment Type':
        Xyz.window.close()
        payment_method = values['pay'][0]
        Xyz.window = Xyz.window_pay(cart_list, adres, payment_method)

    if event == 'Confirm Address':
        Xyz.window.close()
        adres = values['new_address']
        Xyz.window = Xyz.window_pay(cart_list, adres, payment_method)

    if event == 'Back to Supplier Menu':
        Xyz.window.close()
        Xyz.window = Xyz.window_sup()

    if event == 'Pay!':
        Xyz.window.close()
        shipment=values['shipment']
        Xyz.create_order(adres, payment_method, cart_list, shipment)
        sg.popup('Order Created!')
        Xyz.window = Xyz.window_cust()

    if event == 'Add':
        Xyz.insert_product(values)

    if event == 'Login Screen':
        Xyz.window.close()
        Xyz.window = Xyz.window_login()
    if event == 'New Supplier':
        new_user = 'supplier'
        Xyz.window.close()
        Xyz.window = Xyz.window_create_supplier()
    if event == 'New Customer':
        new_user = 'customer'
        Xyz.window.close()
        Xyz.window = Xyz.window_create_customer()
    if event == 'New Shipment Company':
        new_user = 'Shipment'
        Xyz.window.close()
        Xyz.window = Xyz.window_create_shipment_comp()
    if event == 'Enrol':
        if new_user == 'supplier':
            Xyz.insert_supplier(values)
        if new_user == 'customer':
            Xyz.insert_customer(values)
        if new_user == 'Shipment':
            Xyz.insert_shipment_comp(values)
    if event == 'Login':
        print(values)
        Xyz.button_login(values)

    if event == 'Old Orders':
        Xyz.window.close()
        print("values", values)
        Xyz.window = Xyz.oldorders(Xyz.cust_id)
    if event == 'Order Details':
        try:
            order_id1 = values['order_id'][0]['Order_id']
            Xyz.window.close()
            Xyz.window = Xyz.see_details(order_id1)
        except:
            sg.popup('Please select an order!')

    if event == 'Back' and Xyz.login_user_type == 'Customer':
        Xyz.window.close()
        Xyz.window = Xyz.window_cust()
        shop_active = 0
    if event== 'Show all shipments!':
        Xyz.window.close()
        Xyz.window = Xyz.window_show_shipment()
    if event == 'Add a new product!':
        Xyz.window.close()
        Xyz.window = Xyz.window_add_product()

    if event == 'Delete a product':
        Xyz.window.close()
        Xyz.window = Xyz.window_delete_product()

    if event == 'Main Page':
        Xyz.window.close()
        Xyz.window = Xyz.window_welcome()

    if event == 'List the products':
        Xyz.window.close()
        Xyz.window = Xyz.window_list_products(values)
        shop_active = 1

    if event == 'Delete':
        Xyz.window.close()
        cur.execute('DELETE FROM products_supplies WHERE product_id = ?', (values["pid"][0][0],))
        cur.execute('DELETE FROM has2 WHERE product_id = ?', (values["pid"][0][0],))
        con.commit()
        sg.popup("The product is successfully deleted")

        Xyz.window = Xyz.window_sup()
    if event == 'Update a product':
        Xyz.window.close()
        Xyz.window = Xyz.update_product()
    if event == 'Select to Update':
        Xyz.window.close()
        Xyz.window = Xyz.update_details(values)
        p_id = values["pid"][0][0]
        print(p_id)
    if event == 'OK':
        Xyz.window.close()
        print(values)
        details = ["description", "price", "stock_count"]
        i = -1
        for el_details in ["new_description", "new_price", "new_stock"]:
            i = i + 1
            if values[el_details] != '':
                cur.execute('UPDATE products_supplies SET ' + details[i] + '=? WHERE product_id=?', (values[
                                                                                                         el_details],
                                                                                                     p_id))
                con.commit()
        sg.popup("The product is successfully updated")
        Xyz.window = Xyz.window_sup()
    if event == 'Logout':
        Xyz.window.close()
        sg.popup('Bye')
        Xyz.login_user_name = 0
        Xyz.login_user_type = 0
        Xyz.sup_id = 0
        cart_list = []
        Xyz.window = Xyz.window_welcome()
        Xyz.cust_id = 0

    if event == 'Evaluate Order-Shipment':
        Xyz.order_id = values.get("order_id")[0].get("Order_id")
        Xyz.window.close()
        Xyz.window = Xyz.evaluate_shipment()

    if event == 'Evaluate Product':
        Xyz.product_id = values['product'][0][1]
        Xyz.window.close()
        Xyz.window = Xyz.evaluate_product()

    if event == 'Approve':
        print("Values----", values)

        try:

            cur.execute("INSERT INTO evaluate_delivery VALUES (?,?,?,?)",
                        (values.get("points")[0], values.get("com"), Xyz.cust_id, Xyz.order_id))
            con.commit()
        except:
            sg.popup('Already Evaluated!')
            con.rollback()

        Xyz.window.close()
        Xyz.window = Xyz.window_cust()

    if event == 'Evaluate':
        print("Values----", values)
        cur.execute("SELECT sup_id FROM products_supplies WHERE product_id=?", (Xyz.product_id,))
        sup_id = cur.fetchone()[0]
        try:
            cur.execute("INSERT INTO evaluate_product VALUES (?,?,?,?,?)",
                        (Xyz.product_id, Xyz.cust_id, sup_id, values.get("points")[0], values.get("com")))
            con.commit()
        except:
            sg.popup('Already Evaluated')
            con.rollback()

        Xyz.window.close()
        Xyz.window = Xyz.window_cust()

    if event == 'List your orders':
        Xyz.window.close()
        Xyz.window = Xyz.sup_view_order()

    if event == 'Billing Information':
        Xyz.window.close()
        Xyz.window = Xyz.order_billling_info()

    if event == "Start a Discount Campaign":
        Xyz.window.close()
        Xyz.window = Xyz.discount_campaign()

    if event == "Apply Discount":
        Xyz.discount_validation(values)
        print(values)

    elif event == sg.WIN_CLOSED:
        break

Xyz.window.close()
