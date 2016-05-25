#Streak Maker

Simply put, this application creates a single commit everyday to maintain git streak.

To schedule a commit everyday, you can use any basic scheduling utility.
For example, using cron (linux) you can do:

(from the root of the repo)
```
chmod +x run.py
sudo su <your_username>
crontab -e
```

Add the following lines to cron jobs file that pops up:

`0 * * * * cd /path/to/run.py && ./run.py`

This means that the script will run at every hour precisely on the 0th minute. You can adjust this to run on a different time accordingly.
