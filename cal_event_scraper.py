# Used FeedParse5.1.3
# Collects daily event at UC Berkeley
import feedparser
import sqlite3

d = feedparser.parse('http://events.berkeley.edu/index.php/rss/sn/pubaff/type/day/tab/all_events.html')

conn = sqlite3.connect('todayEvent.sqlite3');
c = conn.cursor()

c.execute('''CREATE TABLE today (\n\ttitle text,\n\t link text,\n\t desc text)''')

for e in d.entries:
    c.execute("INSERT INTO today VALUES (?,?,?)", (e.title,e.link,e.description,))

conn.commit()
conn.close()


