from sqlalchemy import create_engine
from flask import Flask
import flask_excel as excel

# connect to database simple sample using sqlite
engine = create_engine("sqlite://")
conn = engine.connect()

# insert rows to test
conn.execute("create table user (id integer, name  varchar(50))")
conn.execute("insert into user values (1, 'john')")
conn.execute("insert into user values (2, 'linus')")
conn.execute("insert into user values (3, 'egg')")
conn.execute("insert into user values (4, 'spam')")


app = Flask(__name__)
@app.route('/sheet.xlsx')
def sheet():
    # define sql statement
    res = conn.execute('select * from user')
    # build excel from records
    return excel.make_response_from_records(res.fetchall(),"xlsx",file_name="sheet.xlsx")

# running app
app.run(host='0.0.0.0')
