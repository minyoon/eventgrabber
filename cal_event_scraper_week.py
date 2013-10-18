# Used FeedParse5.1.3
# Collects daily event at UC Berkeley
import feedparser
import sqlite3
import glob
import os
import csv # writes out csv file

d = feedparser.parse('http://events.berkeley.edu/index.php/rss/sn/pubaff/type/week.html?recur=yes')
fpath = 'weekevent' # Name of the DB and CSV File

for f in glob.glob(fpath+'*'):
    os.remove(f) # remove existing files

conn = sqlite3.connect(fpath+'.sqlite3'); # open sqlite3
csvwriter = csv.writer(open('./'+fpath+'.csv', 'w')) # open csv

c = conn.cursor()

# Set up for the csv and sqlite3 files
c.execute('''CREATE TABLE week (\n title text,\n date text,\n link text,\n desc text)''')
csvwriter.writerow(['title', 'date', 'link', 'desc'])

title_dict = dict()

for e in d.entries:
    link_split = e.link.split('&date=')
    date = link_split[1]
    c.execute("INSERT INTO week VALUES (?,?,?,?)", (e.title, date, e.link,e.description,))
    csvwriter.writerow([e.title.encode('ascii', 'ignore'), date, e.link.encode('ascii', 'ignore'), e.description.encode('ascii', 'ignore')])

conn.commit()
conn.close()
