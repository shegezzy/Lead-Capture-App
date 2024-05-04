from app import db

class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100))
    company = db.Column(db.String(100))

    def __repr__(self):
        return f'<Lead {self.email}>'
