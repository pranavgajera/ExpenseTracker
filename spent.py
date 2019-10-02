import sqlite3 as db
def init():

    connection = db.connect("spent.db")
    cur = connection.cursor()
    delete = "drop table expenses"
    cur.execute(delete)
    sql = '''
    create table if not exists expenses(
        amount string,
        category string,
        message string,
        date string
        )        
    '''
    cur.execute(sql)
    connection.commit()

init()

def log(amount: int, category: str, message: str):
    """
    :rtype: object
    """
    from datetime import datetime
    date = str(datetime.now())
    connection = db.connect("spent.db")
    print(connection)
    cur = connection.cursor()
    sql = '''
    insert into expenses(
        amount, category, message, date) values (
        {},
       "{}",
       "{}",
       "{}"
        )      
        '''.format(amount, category, message,date)
    cur.execute(sql)
    connection.commit()

log(35, "food", "restaurant")
log(150, "transport", "Uber ride to airport")

def view(category=None):
    connection = db.connect("spent.db")
    cur = connection.cursor()
    if category:
        sql = '''
        select * from expenses where category= '{}'        
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses 
      '''.format(category)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    totalamount = cur.fetchall()[0]
    return totalamount, results
print(view('transport'))

