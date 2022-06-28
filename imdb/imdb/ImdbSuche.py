import argparse
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument('-k','--keyword', type=str)
parser.add_argument('-d','--path', type=str,)
args=parser.parse_args()

kw = args.keyword
path = args.path

print("MOVIES")
__SQL__ = " SELECT title, year,genre FROM movie WHERE title LIKE '%kw%' GROUP BY title, genre ORDER BY title ASCD"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

__SQL__ = "SELECT genre FROM movie , genre WHERE movie_mid = genre.movie_id title LIKE '%kw%'"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

__SQL__ = "SELECT genre FROM movie , genre WHERE movie_mid = genre.movie_id AND title LIKE '%kw%'"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

__SQL__ = "SELECT name FROM movie,genre WHERE movie_mid = genre.movie_id AND title LIKE '%kw%'"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

print("ACTORS")
__SQL__ = "SELECT actors.name FROM (select name, movie_id from actor union select name, movie_id FROM actress) AS actors WHERE actors.name LIKE '%kw%';"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

__SQL__ = "SELECT title FROM movie, (select name, movie_id from actor union select name, movie_id FROM actress) AS actors WHERE mid = actors.movie_id AND actors.name LIKE '%kw%';"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

__SQL__ = "select b.name, count(b.name) from (select mid from movie, (select name, movie_id from actor union select name, movie_id from actress) as actors where mid = actors.movie_id and actors.name like "%Krug%") as a, (select name, movie_id from actor union select name, movie_id from actress) as b where a.mid = b.movie_id and b.name not like "%Krug%" group by b.name having count(b.name) order by count(b.name) desc, b.name limit 5;"
conn = sqlite3.connect(args.path)
cur = conn.cursor()
cur.execute(__SQL__)
print(cur.fetchall())

