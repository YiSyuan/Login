#!/usr/bin/env python
print "Content-Type: text/html"

from control import getUser
import cgi

def main():
    q = cgi.FieldStorage()
    cookie = q["q"].value
    account, first_name, last_name = getUser(cookie)
    print """
    <html>
    <body>
    """
    print "<h2>Wellcome %s</h2>" % account
    print "<p>Your first name is %s</p>" % first_name
    print "<p>Your last name is %s</p>" % last_name
    print "<form method='POST' action='control.py'>"
    print "<input type='hidden' name='cookie' value='%s' />" % cookie
    print """
    <input type="hidden" name="page" value="signout" />
    <input type="submit" value="Sign out" />
    </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    main()
