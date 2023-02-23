from flask_learning import db



class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    # One to One
    # education = db.relationship('Education', backref='person', uselist=False)

    # One to Many
    hobbies = db.relationship('Hobby', backref='person', lazy='dynamic')

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person {self.name} is {self.age} years old"

    def report_hobbies(self):
        print("Here are my hobbies...")
        
        for h in self.hobbies:
            print(h.hobby)

# class Education(db.Model):
#     __tablename__ = 'education'
#     id = db.Column(db.Integer, primary_key=True)
#     qualification = db.Column(db.Text)
#     person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

#     def __init__(self, qualification, person_id) -> None:
#         super().__init__()
#         self.qualification = qualification
#         self.person_id = person_id

class Hobby(db.Model):
    __tablename__ = 'hobby'

    id = db.Column(db.Integer, primary_key=True)
    hobby = db.Column(db.Text)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, hobby, person_id) -> None:
        super().__init__()
        self.hobby = hobby
        self.person_id = person_id
