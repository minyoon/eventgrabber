# Used FeedParse5.1.3
# Collects daily event at UC Berkeley
import feedparser
import sqlite3
import glob
import os
import csv # writes out csv file

d = feedparser.parse('http://events.berkeley.edu/index.php/rss/sn/pubaff/type/day/tab/all_events.html')
fpath = 'todayevent' # Name of the DB and CSV File

for f in glob.glob(fpath+'*'):
    os.remove(f) # remove existing files

conn = sqlite3.connect(fpath+'sqlite3'); # open sqlite3
csvwriter = csv.writer(open('./'+fpath+'.csv', 'w')) # open csv

c = conn.cursor()

# Set up for the csv and sqlite3 files
c.execute('''CREATE TABLE today (\n\ttitle text,\n\t link text,\n\t desc text)''')
csvwriter.writerow(['title', 'link', 'desc'])

for e in d.entries:
    c.execute("INSERT INTO today VALUES (?,?,?)", (e.title,e.link,e.description,))
    csvwriter.writerow([e.title.encode('ascii', 'ignore'), e.link.encode('ascii', 'ignore'), e.description.encode('ascii', 'ignore')])

conn.commit()
conn.close()


