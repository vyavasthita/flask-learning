from main import db, Person

db.create_all()

dilip = Person('Dilip', 36)
shilpa = Person('Shilpa', 34)

print("Before")
print(dilip.id)
print(shilpa.id)

db.session.add([dilip, shilpa])

db.session.commit()
print("-----------------------------")
print("After")
print(dilip.id)
print(shilpa.id)