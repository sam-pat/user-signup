#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)




form = """
<form method= 'post'>
    <h2>Signup</h2>
    <br>
        <label>Username <input name='username' type='text' value='' required></label><div style="color:red">%(user_error)s</div>
        <br>
        <label>Password <input name='password' type='password'  required></label><div style="color:red">%(password_error)s</div>
        <br>
        <label>Verify Password <input name='verify' type='password' required></label><div style="color:red">%(verify_error)s</div>
        <br>
        <label>Email (optinal) <input name='email' type='email' value=''/></label><div style="color:red">%(email_error)s</div>
        <br>
        <br>
        <input type='submit'>
</form>
"""







class MainHandler(webapp2.RequestHandler):



    def write_form(self, user_error = "" , password_error = "",  verify_error = "", email_error = "" ):
        self.response.out.write(form % { "user_error" : user_error , "password_error": password_error,
        "verify_error": verify_error , "email_error" : email_error})


    def get(self):
        self.write_form()

    def post(self):
        user = self.request.get("username")
        post_message = "Welcome, " + user + "!"

        prevalided_username = self.request.get("username")
        prevalided_password = self.request.get("password")
        prevalided_email = self.request.get("email")


        password = self.request.get("verify")



        valided_username = valid_username(prevalided_username)
        valided_password = valid_password(prevalided_password)
        valided_email = valid_email(prevalided_email)

        user_error1 =""
        password_error1=""
        email_error1=""
        verify_error1=""

        valid_form = True
        if not (valided_username ):
            user_error1 = "That's not a valid username"
            valid_form = False
        if not (valided_password):
            password_error1 = "That's not a valid password"
            valid_form = False
        elif not (prevalided_password == password):
            verify_error1 = "Passwords don't match"
            valid_form = False
        if not (valid_email):
            email_error1 = "That's not a valid email"
            valid_form = False

        if not valid_form:

            self.write_form(user_error= user_error1, password_error=password_error1,
                            verify_error = verify_error1 ,email_error = email_error1  )
        #else:
            #do the welcome

        # if not (valided_username ):
        #     self.write_form( user_error = "That's not a valid username")
        # elif not (valided_password):
        #     self.write_form( password_error = "That's not a valid password")
        # elif not (verify_password == password):
        #     self.write_form( verify_error = "Passwords don't match")
        # elif not (valid_email):
        #     self.write_form (email_error = "That's not a valid email")

        #if not  (valided_username and valided_password and valided_email and verify != verify_password):
        #    self.write_form( user_error = "That's not a valid username" , password_error = "That's not a valid password" , verify_error = "Passwords don't match" , email_error = "That's not a valid email")

        else:
            self.response.write(post_message)


#, password_error = "That's not a valid password" , verify_error = "Passwords don't match" , email_error = "That's not a valid email")
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
