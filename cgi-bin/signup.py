#!/usr/bin/env python
print "Content-Type: text/html"
print """
<html>
<body>
<h2>Sign up</h2>
<form method="POST" action="control.py" enctype="multipart/form-data">
<input type='text' name='account' placeholder='account' required></input>
<p></p>
<input type='password' name='pwd' placeholder='***' required></input>
<p></p>
<input type='text' name='firstName' placeholder='First Name' required></input>
<p></p>
<input type='text' name='lastName' placeholder='Last Name' required></input>
<p></p>
<input type="hidden" name="page" value="signup" />
<input type="submit" value="Sign Up" />
</form>
<a href='home.py'>Sign in</a>
</body>
</html>
"""