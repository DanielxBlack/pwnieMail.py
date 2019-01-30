# pwnieMail.py
Python Script that checks email against haveibeenpwnd and returns results in a table.

It requires the following two libraries to work correctly:
 - https://github.com/berend/haveibeenpwnd
 - http://zetcode.com/python/prettytable/

# About the project
It's really nothing special, to be honest. I'm learning Python and building simple tools is part of that journey.


# How it works
pwnieMail is designed for python 3.
Run it with the following command:
> python3 pwnieMail.py

It will prompt you for a file. You must enter the full path to the text file, for instance:
> /home/userName/documents/emails.txt

This will run each email on the list against the Have I Been Pwned database and return a table with known breaches. Each email address on the list will return its own table, unless there are no listed breaches.

Remember, just because your email doesn't show up on the list doesn't mean it hasn't been pwned. It may be part of an unknown databreach.
