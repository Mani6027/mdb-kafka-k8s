import datetime
from urllib.parse import quote_plus
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import text

engine = create_engine("mysql+mysqlconnector://externaldata:%s@db4free.net:3306/ormtestt?autocommit=true" % quote_plus("external@123"))
conn = engine.connect()


# ---------------------------ORM--------------------------------------
metadata = MetaData()
table = Table('orm1', metadata, autoload_with=engine)

cl = table.columns
for cal in cl:
    print(cl)

query = table.select().limit(10)
result = conn.execute(query)
query = table.insert().values(rollno=3, name='Jack', age=30, date=datetime.datetime.now())
# conn.execute(query)
for row in result:
    print(row)

# ---------------------------Raw query--------------------------------------
# res= conn.execute(statement=text("Select * from orm1")) #raw query

# for row in res:
#     print(row)

conn.close()



# with engine.connect() as conn:
#     query = table.select()
#     result = conn.execute(query)
#
#     for row in result:
#         print(row)
