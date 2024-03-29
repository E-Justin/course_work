import psycopg2

conn = psycopg2.connect(
    """
    dbname=week3 user=postgres host=localhost port=5432
    """
)

# sets a property to autocommit any changes made to the db
conn.set_session(autocommit=True)

# open a cursor to perform database operations
cur = conn.cursor()

cur.execute(
    """
    DROP TABLE IF EXISTS veggies
    """
)

cur.execute(
    """
    CREATE TABLE veggies(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        color TEXT NOT NULL
    )
    """
)

cur.execute(
    """
    INSERT INTO veggies VALUES
    (1, 'carrot', 'orange'),
    (2, 'onion', 'yellow'),
    (3, 'zuchini', 'green'),
    (4, 'squash', 'yellow'),
    (5, 'pepper', 'red'),
    (6, 'onion', 'red')

    """
)

# execute a query
cur.execute(
    """
    SELECT * FROM veggies
    """
)

# retrieve query results
records = cur.fetchall()

# print(records)

cur.execute(
    """
    SELECT color, name FROM veggies
    ORDER BY name, color
    """
)

# returns previous query as a list of tuples
veggie_records = cur.fetchall()

for veg in veggie_records:
    print(veg[0], veg[1])

print('')

for i, veg in enumerate(veggie_records):
    print(str(i+1) + ".", veg[0].capitalize(), veg[1].capitalize())
