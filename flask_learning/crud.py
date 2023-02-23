from main import db, Person

# Create
samskriti = Person('Samskriti', 3)
db.session.add(samskriti)
db.session.commit()

# Read
all_person = Person.query.all()

# Read person by id
person = Person.query.get(1)

# Read by name
dilip = Person.query.filter_by(name='Dilip')
print(dilip.all())

