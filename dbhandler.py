from app import * 
from models import *

db.create_all()

# p = User(title="hello third", body="content 3")
# p.tags.append(Tag.query.first())

us = User.query.first()
u = Role.query.first()

user_datastore.create_user(email="student@text.com", password="student")
user_datastore.create_role(name="student")

# user_datastore


user_datastore.add_role_to_user(us,u)
# db.session.add(u)
db.session.commit()