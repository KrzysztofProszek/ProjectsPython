import sqlalchemy as db

#Połączenie z naszą bazą sqlite
engine = db.create_engine('sqlite:///CodeBrainers.db')
connection = engine.connect()

# MetaData to obiekt kontenera, który przechowuje razem wiele różnych
# funkcji opisywanej bazy danych (lub wielu baz danych).

metadata = db.MetaData()

#obiekt tabeli
customer = db.Table('Customer',metadata, autoload_with=engine)
order_product = db.Table('Order_product', metadata, autoload_with=engine)
product = db.Table('Product', metadata, autoload_with=engine)
# print("Klucze tabeli:",customer.columns.keys(),'\n')
# print("Reprezentacja tabeli: \n")
# print(repr(customer))

select_customer_query = db.select(customer).where(customer.columns.id == '1')
select_results = connection.execute(select_customer_query)
print('\n', select_results.fetchall())

query = db.select(customer).where( customer.columns.id == '1')
print('\n',connection.execute(query).fetchone())

query = db.select(product).where(product.columns.price.in_([10,50,100]))
print('\n',connection.execute(query).fetchall())

query = db.select(customer).where(db.and_(customer.columns.city == 'Lublin', customer.columns.id !='1'))
print('\n',connection.execute(query).fetchall())

query = db.select(product).order_by(db.desc(product.columns.date))
print('\n',connection.execute(query).fetchall())

query = db.select(db.func.avg(product.columns.price))
print('\n',connection.execute(query).fetchall())

query = db.select(db.func.count(customer.columns.city.distinct()))
print('\n',connection.execute(query).fetchall())

query = db.select(order_product, product)

query = query.select_from(order_product.join(product, product.columns.id == order_product.columns.product_id))
print('\n',connection.execute(query).fetchall())

