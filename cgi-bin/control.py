#!/usr/bin/env python
import cgi
import psycopg2

def main():
    conn, cur = conndb()
    form = cgi.FieldStorage()
    page = form['page'].value
    if page == 'signin':
        signin(form, conn, cur)
    else:
        signup(form, conn, cur)

def conndb():
    connection = "dbname='postgres' user='postgres' host='localhost' password='postgres'"
    try:
        conn = psycopg2.connect(connection)
    except:
        print "Connect to the database fail"
    cur = conn.cursor()
    return conn, cur

def redirect(url, msg):
    print "Content-Type: text/plain"
    print "Refresh: 2; url=%s" % url
    print
    print msg
    print
    print "Redirecting..."

def signin(form, conn, cur):
    account = form['account'].value
    pwd = form['pwd'].value
    sql = "SELECT * FROM account WHERE user_account = '%s' and user_password = '%s'" % (account, pwd)
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 1:
        msg = "Sign in success."
        redirect('userDetail.py', msg)
    else:
        msg = "No this account, please sign up"
        redirect('signup.py', msg)
    conn.commit()
    cur.close()

def signup(form, conn, cur):
    account = form['account'].value
    pwd = form['pwd'].value
    firstName = form['firstName'].value
    lastName = form['lastName'].value
    sql = "SELECT * FROM account WHERE user_account = '%s'" % account
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 1:
        msg = "Existing account, please sign up again."
        redirect('signup.py', msg)
    else:
        sql = "INSERT INTO account(user_account, user_password, first_name, last_name) values (%s, %s, %s, %s)"
        data = (account, pwd, firstName, lastName)
        cur.execute(sql, data)
        conn.commit()
        cur.close()
        msg = "Sign up success, please sign in."
        redirect('home.py', msg)

main()