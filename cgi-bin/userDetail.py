#!/usr/bin/env python
print "Content-Type: text/html"

from control import getUser

def main():
    account, first_name, last_name = getUser()
    print """
    <html>
    <body>
    """
    print "<h2>Wellcome %s</h2>" % account
    print "<p>Your first name is %s</p>" % first_name
    print "<p>Your last name is %s</p>" % last_name
    print """
    <form method="POST" action="control.py">
    <input type="hidden" name="page" value="signout" />
    <input type="submit" value="Sign out" />
    </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    main()
