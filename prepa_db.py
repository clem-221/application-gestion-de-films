import json, sqlite3


with open("app/static/data/movies_cleaned.json", "r") as f:
	movies = json.load(f)


connection = sqlite3.connect('app/movies.db')


with open('app/static/data/schema_movies.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for m in movies:
	cur.execute("INSERT INTO movies (title, year, genres, href, extract, cover) VALUES (?, ?, ?, ?, ?, ?)",
            (m["title"], m["year"], ",".join(m["genres"]), m["href"], m["extract"], m["thumbnail"])
            )

connection.commit()
connection.close()


