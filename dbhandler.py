from app import *
from models import *

db.create_all()

# p = User(title="hello third", body="content 3")
# p.tags.append(Tag.query.first())

# us = User.query.filter_by(email='student@test.com').first()
# print(us)
# a = Scorecard(correct=8, total=10)

# a.tag = Tag.query.filter_by(title='MATHS').first()
# us.scorecard.append(a)

# user = user_datastore.create_user( email="admin@text.com", password="admin")
# role = user_datastore.create_role(name="admin")

# # user_datastore
# db.session.add(us)
# db.session.commit()

# user_datastore.add_role_to_user(user,role)

# db.session.commit()
