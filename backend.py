import sqlite3


class Backend(object):
    def __init__(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, title TEXT, director TEXT, year INTEGER, lead TEXT)")
        db.commit()
        db.close()

    def add(self, title="", director="", year=2000, lead=""):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("INSERT INTO movie VALUES (NULL, ?, ?, ?, ?)", (title, director, year, lead))
        db.commit()
        db.close()

    def view_all(self):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("SELECT * FROM movie")
        rows = cur.fetchall()
        db.close()
        return rows

    def delete(self, id):
        db = sqlite3.connect("movies.db")
        cur = db.cursor()
        cur.execute("DELETE FROM movie WHERE id=?", (id,))
        db.commit()
        db.close()


# we do some tests here
if __name__ == "__main__":
    print("This is my backend part")
    bk = Backend()
    bk.add(title="Indiana Jones", director="George Lucas", lead="Harrison Ford", year=1977)
    # bk.delete(2)
    print(bk.view_all())


