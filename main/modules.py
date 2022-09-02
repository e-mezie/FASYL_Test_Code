from main import db


class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column (db.String (20), unique=False, nullable=False)
    lastname = db.Column (db.String (20), unique=False, nullable=False)
    email_address = db.Column (db.String (120), unique=True, nullable=False)
    reference_code = db.Column (db.String (20), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.firstname}','{self.lastname}', '{self.email_address}','{self.reference_code}'"
