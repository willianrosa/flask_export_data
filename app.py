from sqlalchemy import create_engine
from flask import Flask
import flask_excel as excel

engine = create_engine("sqlite://")
conn = engine.connect()

conn.execute("create table user (id integer, name  varchar(50))")
conn.execute("insert into user values (1, 'john')")
conn.execute("insert into user values (2, 'linus')")
conn.execute("insert into user values (3, 'egg')")
conn.execute("insert into user values (4, 'spam')")


app = Flask(__name__)
@app.route('/sheet.xlsx')
def sheet():
   res = conn.execute('select * from user')
   return excel.make_response_from_records(res.fetchall(),"xlsx",file_name="sheet.xlsx")

app.run(host='0.0.0.0')
