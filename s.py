import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("""CREATE TABLE users (
    username text,
    id integer,
    rank text,
    balance integer,
    level integer,
    is_banned integer,
    last_claimed_daily integer,
    daily_streak integer
)""")

c.execute("INSERT INTO users VALUES ('BEN SHAPIRO', 1131, 'Admin', 0, 1, 0, 0, 1 )")
c.execute("INSERT INTO users VALUES ('Kevin', 5, 'Admin', 0, 1, 0, 0, 1)")
c.execute("INSERT INTO users VALUE ('Rheanna', 197, 'Admin', 0, 1, 0, 0, 1)")

c.execute("SELECT * FROM users WHERE username='BEN SHAPIRO'")

print(c.fetchone())

conn.commit()

conn.close()

