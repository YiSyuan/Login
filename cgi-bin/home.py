#!/usr/bin/env python
print "Content-Type: text/html"
print """
<html>
<body>
<h2>Hello User</h2>
<form method="POST" action="control.py">
<input type='text' name="account" placeholder='account' required></input>
<p></p>
<input type='password' name="pwd" placeholder='***' required></input>
<p></p>
<input type="hidden" name="page" value="signin" />
<input type="submit" value="Sign in" />
</form>
<a href='signup.py'>No account?</a>
</body>
</html>
"""