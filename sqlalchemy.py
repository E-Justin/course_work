from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# connect to postgres db
engine = create_engine('postgresql://postgres@localhost:5432/week3') # argument is url connection
Session = sessionmaker(bind=engine) # allows us to interact with db
Base = declarative_base() # Base class


class Veggie(Base):
    __tablename__ = 'veggies'

    # set autoincrement to use the SERIAL data type
    id = Column(Integer, primary_key = True, autoincrement = True)
    color = Column(String, nullable = False)
    name = Column(String, nullable = False)

    def formatted_name(self):
        return self.color.capitalize() + ' ' + self.name.capitalize()

# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'name': 'carrot', 'color': 'orange'},
    {'name': 'onion', 'color': 'yellow'},
    {'name': 'zuchini', 'color': 'green'},
    {'name': 'squash', 'color': 'yellow'},
    {'name': 'pepper', 'color': 'red'},
    {'name': 'onion', 'color': 'red'},
]

# Turn the seed data into a list of Veggie objects
veggie_objects = []
for item in seed_data:
    v = Veggie(name = item['name'], color = item['color'])
    veggie_objects.append(v)

# create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(veggie_objects)
session.commit()

# create a new session for performing queries
session = Session()

# run a select * query on the veggies table
veggies = session.query(Veggie).all()

for v in veggies:
    print(v.color, v.name)

#         select * from veggies  order by      name,        color
veggies = session.query(Veggie).order_by(Veggie.name, Veggie.color).all()

for i, v in enumerate(veggies):
    print(str(i+1) + '.' + v.formatted_name())
