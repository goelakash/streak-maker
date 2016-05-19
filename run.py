#!/usr/bin/env python3

from builtins import str
import datetime
import pexpect
import time

commit_message = "Last commit on " + str(datetime.date.today())
commits = open("commits.txt","r")
line  = commits.readline()
line = line[:-1]

credentials = open("credentials","r")
username = credentials.readline()       # Github username
username = username[:-1]
password = credentials.readline()       # Github password
password = password[:-1]

if line != commit_message:
    commits = open("commits.txt","w")
    commits.write(commit_message)
    commits.close()

pexpect.run("git add .")
pexpect.run("git commit -m '"+commit_message)
pexpect.run('git push https://'+username+':'+password+'@github.com/'+username+'/streak-maker.git')
# ch = pexpect.spawn("git push origin master")
# time.sleep(2)
# ch.expect('U*',async=True)
# ch.sendline(username)
# time.sleep(2)
# ch.expect('P*',async=True)
# ch.sendline(password)
