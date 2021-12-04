import crawler01, crawler02
import pandas as pd
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template("hello00.html")

# @app.route("/")
# def hello():
#     return render_template("hello01.html")

# @app.route("/")
# def hello():
#     item = request.args.get('item', '')
#     print(f'item => {item}')
#     return render_template("hello02.html", 
#         item=item
#     )

# @app.route("/")
# def hello():

#     d1 = crawler01.yahoo()
#     d2 = crawler01.momo()
#     d3 = crawler01.pchome()
#     d4 = crawler01.shopee()
    
#     df = pd.concat([d1, d2, d3, d4])

#     return render_template("hello03.html", 
#         d = df.to_dict(orient='records'),
#     )

# @app.route("/")
# def hello():

#     item = request.args.get('item')

#     if not item:
#         return render_template("none.html", 
#         item = '',
#         d = [],
#     )        

#     print(f'item => {item}')

#     d1 = crawler02.yahoo(item)
#     d2 = crawler02.momo(item)
#     d3 = crawler02.pchome(item)
#     # d4 = crawler02.shopee(item)
    
#     df = pd.concat([d1, d2, d3])

#     return render_template("hello04.html", 
#         item = item,
#         d = df.to_dict(orient='records'),
#     )

# =====
# 加上 Thread 非同步執行
# =====

# import threading

# def yahoo(item):
#     print(" yahoo threading start: ", item)
#     print(" ==== yahoo threading done ====")
    
# def momo(item):
#     print(" momo threading start: ", item)
#     print(" ==== shopee threading done ====")

# def pchome(item):
#     print(" pchome threading start: ", item)
#     print(" ==== shopee threading done ====")

# def shopee(item):
#     print(" shopee threading start: ", item)
#     print(" ==== shopee threading done ====")

# @app.route("/search")
# def search():

#     item = request.args.get('item')

#     if not item:
#         return render_template("none.html", 
#         item = '',
#         d = [],
#     )        

#     print(f'item => {item}')
    
#     # d1 = crawler02.yahoo(item)
#     # d2 = crawler02.momo(item)
#     # d3 = crawler02.pchome(item)
#     # d4 = crawler02.shopee(item)
    
#     # df = pd.concat([d1, d2, d3])

#     t1 = threading.Thread(target = yahoo, args = (item,))
#     t1.start()
#     t2 = threading.Thread(target = momo, args = (item,))
#     t2.start()
#     t3 = threading.Thread(target = pchome, args = (item,))
#     t3.start()
#     t4 = threading.Thread(target = shopee, args = (item,))
#     t4.start()
            
#     return 'done'

### =====
### 串接資料庫，把爬蟲資料非同步存入資料庫
### =====


# import threading
# from sqlalchemy import create_engine

# conn = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/sample?auth_plugin=mysql_native_password', echo=False)

# def yahoo(item):
#     print(" yahoo threading start: ", item)
#     d1 = crawler02.yahoo(item)
#     d1['item'] = item
#     d1.to_sql(name='data', con=conn, if_exists='append', index=False)
#     print(" ==== yahoo threading done ====")
    
# def momo(item):
#     print(" momo threading start: ", item)
#     d2 = crawler02.momo(item)
#     d2['item'] = item
#     d2.to_sql(name='data', con=conn, if_exists='append', index=False)
#     print(" ==== momo threading done ====")

# def pchome(item):
#     print(" pchome threading start: ", item)
#     d3 = crawler02.pchome(item)
#     d3['item'] = item
#     d3['優惠'] = ''
#     d3.to_sql(name='data', con=conn, if_exists='append', index=False)
#     print(d3)
#     print(" ==== pchome threading done ====")

# def shopee(item):
#     print(" shopee threading start: ", item)
#     d4 = crawler02.shopee(item)
#     d4['item'] = item
#     d4.to_sql(name='data', con=conn, if_exists='append', index=False)
#     print(" ==== shopee threading done ====")

# @app.route("/search")
# def search():

#     item = request.args.get('item')

#     if not item:
#         return render_template("none.html", 
#         item = '',
#         d = [],
#     )        

#     print(f'item => {item}')

#     t1 = threading.Thread(target = yahoo, args = (item,))
#     t1.start()
#     t2 = threading.Thread(target = momo, args = (item,))
#     t2.start()
#     t3 = threading.Thread(target = pchome, args = (item,))
#     t3.start()
#     t4 = threading.Thread(target = shopee, args = (item,))
#     t4.start()
            
#     return 'done'

## =====
## 建立一個表格，紀錄查詢資料
## =====

# from datetime import datetime
# from sqlalchemy import create_engine

# conn = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/sample?auth_plugin=mysql_native_password', echo=False)

# @app.route("/search")
# def search():

#     item = request.args.get('item')
#     time = datetime.today()

#     if not item:
#         return render_template("none.html", 
#         item = '',
#         d = [],
#     )        

#     print(f'item => {item}')
#     print(f'time => {time}')

#     df = pd.DataFrame({
#         'item': [item],
#         'createdAt': [time],
#         'status': [0]
#     })

#     d = df.to_sql(name='records', con=conn, if_exists='append', index=False)
#     records = pd.read_sql('''SELECT * 
#                             FROM records;
#                         ''', conn)
            
#     return 'done'


### =====
### 查詢記錄整合爬蟲執行
### =====

# import threading
# from datetime import datetime
# from sqlalchemy import create_engine

# conn = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/sample?auth_plugin=mysql_native_password', echo=False)

# def yahoo(item, item_id):
#     print(" yahoo threading start: ", item)
#     d1 = crawler02.yahoo(item)
#     d1['item'] = item_id
#     d1.to_sql(name='data', con=conn, if_exists='append', index=False)
    
#     with conn.connect() as con:
#         rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

#     print(" ==== yahoo threading done ====")
    
# def momo(item, item_id):
#     print(" momo threading start: ", item)
#     d2 = crawler02.momo(item)
#     d2['item'] = item_id
#     d2.to_sql(name='data', con=conn, if_exists='append', index=False)
    
#     with conn.connect() as con:
#         rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

#     print(" ==== momo threading done ====")

# def pchome(item, item_id):
#     print(" pchome threading start: ", item)
#     d3 = crawler02.pchome(item)
#     d3['item'] = item_id
#     d3['優惠'] = ''
#     d3.to_sql(name='data', con=conn, if_exists='append', index=False)
    
#     with conn.connect() as con:
#         rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

#     print(" ==== pchome threading done ====")

# def shopee(item, item_id):
#     print(" shopee threading start: ", item)
#     d4 = crawler02.shopee(item)
#     d4['item'] = item_id
#     d4.to_sql(name='data', con=conn, if_exists='append', index=False)
    
#     with conn.connect() as con:
#         rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

#     print(" ==== shopee threading done ====")

# @app.route("/search")
# def search():

#     item = request.args.get('item')
#     time = datetime.today()

#     if not item:
#         return render_template("none.html", 
#         item = '',
#         d = [],
#     )        

#     print(f'item => {item}')
#     print(f'time => {time}')

#     df = pd.DataFrame({
#         'item': [item],
#         'createdAt': [time],
#         'status': [0]
#     })

#     d = df.to_sql(name='records', con=conn, if_exists='append', index=False)
#     records = pd.read_sql(f'''SELECT * 
#                             FROM records
#                             WHERE item = '{item}';
#                         ''', conn)

#     item_id = records.iloc[-1, 0]

#     t1 = threading.Thread(target = yahoo, args = (item, item_id,))
#     t1.start()
#     t2 = threading.Thread(target = momo, args = (item, item_id,))
#     t2.start()
#     t3 = threading.Thread(target = pchome, args = (item, item_id,))
#     t3.start()
#     t4 = threading.Thread(target = shopee, args = (item, item_id,))
#     t4.start()
            
#     return 'done'

### =====
### 呈現所有紀錄
### 
### 1. 首頁可以看到所有「查詢記錄」
### 2. 首頁可以啟動背景搜尋
### 3. 每一筆記錄都看到爬蟲結果
### =====

import threading
from datetime import datetime
from sqlalchemy import create_engine

conn = create_engine('mysql+mysqlconnector://bedc46389be583:9400dd86@us-cdbr-east-04.cleardb.com/heroku_b85b091d677c406?auth_plugin=mysql_native_password', echo=False)

def yahoo(item, item_id):
    print(" yahoo threading start: ", item)
    d1 = crawler02.yahoo(item)
    d1['item'] = item_id
    d1.to_sql(name='data', con=conn, if_exists='append', index=False)
    
    with conn.connect() as con:
        rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

    print(" ==== yahoo threading done ====")
    
def momo(item, item_id):
    print(" momo threading start: ", item)
    d2 = crawler02.momo(item)
    d2['item'] = item_id
    d2.to_sql(name='data', con=conn, if_exists='append', index=False)
    
    with conn.connect() as con:
        rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

    print(" ==== momo threading done ====")

def pchome(item, item_id):
    print(" pchome threading start: ", item)
    d3 = crawler02.pchome(item)
    d3['item'] = item_id
    d3['優惠'] = ''
    d3.to_sql(name='data', con=conn, if_exists='append', index=False)
    
    with conn.connect() as con:
        rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

    print(" ==== pchome threading done ====")

def shopee(item, item_id):
    print(" shopee threading start: ", item)
    d4 = crawler02.shopee(item)
    d4['item'] = item_id
    d4.to_sql(name='data', con=conn, if_exists='append', index=False)
    
    with conn.connect() as con:
        rs = con.execute(f'UPDATE records SET status=status+1 WHERE id = {item_id};')

    print(" ==== shopee threading done ====")

@app.route("/")
def hello():

    records = pd.read_sql(f'''SELECT * 
                            FROM records;
                        ''', conn)

    return render_template("hello05.html", 
        d = records.to_dict(orient='records'),
    )

@app.route("/show/<item_id>")
def show(item_id):
    print('')
    items = pd.read_sql(f'''SELECT * 
                            FROM records
                            WHERE id = {item_id};
                        ''', conn)

    products = pd.read_sql(f'''SELECT * 
                            FROM data
                            WHERE item = {item_id};
                        ''', conn)

    print(items)
    return render_template("details.html", 
        item = items.iloc[0, 1],
        d = products.to_dict(orient='records'),
    )

@app.route("/search")
def search():

    item = request.args.get('item')
    time = datetime.today()

    if not item:
        return render_template("none.html", 
        item = '',
        d = [],
    )        

    print(f'item => {item}')
    print(f'time => {time}')

    df = pd.DataFrame({
        'item': [item],
        'createdAt': [time],
        'status': [0]
    })

    d = df.to_sql(name='records', con=conn, if_exists='append', index=False)
    records = pd.read_sql(f'''SELECT * 
                            FROM records
                            WHERE item = '{item}';
                        ''', conn)

    if len(df) == 0:
        return render_template("none.html", 
        item = '',
        d = [],
    )        

    item_id = records.iloc[-1, 0]

    t1 = threading.Thread(target = yahoo, args = (item, item_id,))
    t1.start()
    t2 = threading.Thread(target = momo, args = (item, item_id,))
    t2.start()
    t3 = threading.Thread(target = pchome, args = (item, item_id,))
    t3.start()
    t4 = threading.Thread(target = shopee, args = (item, item_id,))
    t4.start()
            
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0')


