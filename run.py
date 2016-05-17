#!/usr/bin/env python

import time
import os

commit_message = "committed on " + time.asctime()
commits = open("commits.txt","a")
commits.write(commit_message)
commits.close()

os.system("git add commits.txt")
os.system("git commit -m '"+commit_message+"'")
os.system("git push origin master")

