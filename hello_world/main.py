# Copyright 2016 Google Inc.
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

import webapp2

form ='''

<form method="post">
   What is your Birthday?<br>
   
   <label> Month
      <input type="text" name="month">
   </label>
   
   <label> Day
      <input type="text" name="day">
   </label>
   
   <label> Year
      <input type="text" name="year">
   </label>

   <div style="color: red">%(error)s</div>

   <br>
   <input type="submit">
</form>

'''

valid_months = [
   "January",
   "February",
   "Mars",
   "April",
   "May",
   "June",
   "July",
   "August",
   "September",
   "October",
   "November",
   "December",
   ];

def valid_day(day_str):
   try:
      day_int = int(day_str);
      if day_int>0 and day_int<=31:
         return day_int;
   except:
      pass;
   return None;

def valid_month(month_str):
   if month_str.capitalize() in valid_months:
      return month_str;
   return None;

def valid_year(year_str):
   try:
      year_int = int(year_str);
      if year_int>1900 and year_int<=2020:
         return year_int;
   except:
      pass;
   return None;

class MainPage(webapp2.RequestHandler):
   def write_form(self, error=""):
      self.response.write(form%{'error':error});
   def get(self):
      # self.response.headers['Content-Type'] = 'text/plain'
      self.write_form()
   def post(self):
      user_month = valid_month( self.request.get("month") );
      user_day   = valid_day  ( self.request.get("day"  ) );
      user_year  = valid_year ( self.request.get("year" ) );
      if not(user_month and user_day and user_year):
         self.write_form("That doesn't look fine to me.");
      else:
         self.write_form("Thanks! Thats a valid Birthday!");

class TestHandler(webapp2.RequestHandler):
   def post(self):
      self.response.write(self.request)
      self.response.headers['Content-Type'] = 'text/plain'

app = webapp2.WSGIApplication([
      ('/', MainPage),
      ('/testform', TestHandler)
   ], debug=True)

