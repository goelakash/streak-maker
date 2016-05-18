#!/usr/bin/env python

from builtins import str
import datetime
import os
import pexpect

commit_message = "Last commit on " + str(datetime.datetime.now().time())
commits = open("commits.txt","r")
line  = commits.readline()

credentials = open("credentials","r")
username = credentials.readline()
password = credentials.readline()

if line != commit_message:

    commits = open("commits.txt","w")
    commits.write(commit_message)
    commits.close()

    os.system("git add .")
    os.system("git commit -m '"+commit_message+"'")
    child = pexpect.spawn("git push origin master")
    child.expect("Username*",async=True)
    child.sendline(username)
    child.expect("Password*",async=True)
    child.sendline(password)
