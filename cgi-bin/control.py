#!/usr/bin/env python
import cgi
import psycopg2
import Cookie
import string
import random

def main():
    conn, cur = connDB()
    form = cgi.FieldStorage()
    page = form['page'].value
    if page == 'signin':
        signIn(form, conn, cur)
    elif page == 'signup':
        signUp(form, conn, cur)
    elif page == 'signout':
        cookie = form['cookie'].value
        signOut(form, conn, cur, cookie)

def connDB():
    connection = "dbname='postgres' user='postgres' host='localhost' password='postgres'"
    try:
        conn = psycopg2.connect(connection)
    except:
        print "Connect to the database fail"
    cur = conn.cursor()
    return conn, cur

def getUser(cookie):
    conn, cur = connDB()
    sql = "SELECT user_account, first_name, last_name FROM account JOIN signin ON (account.user_account = signin.account) where signin.ip = '%s'" % (cookie)
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 1:
        cur.close()
        return rows[0][0], rows[0][1], rows[0][2]
    else:
        cur.close()
        msg = "Your not user, please sign up."
        redirect('signup.py', msg)

def numbers(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def redirect(url, msg):
    print "Content-Type: text/plain"
    print "Refresh: 2; url=%s" % url
    print
    print msg
    print
    print "Redirecting..."

def signIn(form, conn, cur):
    account = form['account'].value
    pwd = form['pwd'].value
    number = numbers()
    sql = "SELECT * FROM account a where user_account = '%s' and user_password = '%s' AND NOT EXISTS (SELECT * FROM signin where account = a.user_account)" % (account, pwd)
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) == 1:
        sql = "INSERT INTO signin(account, password, ip) values (%s, %s, %s)"
        data = (account, pwd, number)
        cur.execute(sql, data)
        conn.commit()
        cur.close()
        msg = "Sign in success."
        redirect('userDetail.py?q=' + number, msg)
    else:
        cur.close()
        msg = "Sign in fail, please sign in again or sign up"
        redirect('signup.py', msg)

def signOut(form, conn, cur, cookie):
    sql = "DELETE FROM signin WHERE ip = '%s'" % (cookie)
    cur.execute(sql)
    conn.commit()
    cur.close()
    msg = "Sign out..."
    redirect('home.py', msg)

def signUp(form, conn, cur):
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

if __name__ == "__main__":
    main()