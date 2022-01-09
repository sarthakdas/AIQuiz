from app import *
from models import *

db.create_all()

# p = User(title="hello third", body="content 3")
# p.tags.append(Tag.query.first())

# us = User.query.filter_by(email='mahan').first()
# print(us)
# a = Scorecard(correct=8, total=10)

# a.tag = Tag.query.filter_by(title='ratio').first()
# us.scorecard.append(a)

# t = Tag.query.filter_by(title='ratio').first()

# scoreCardRow = Scorecard.query.filter_by(user=us, tag=t).first()
# scoreCardRow.correct = 5
# scoreCardRow.total = 8
# user = user_datastore.create_user( email="admin@text.com", password="admin")
# role = user_datastore.create_role(name="admin")
# Scorecard.__table__.drop(db.engine)
# # user_datastore
# db.session.add(us)
db.session.commit()

# user_datastore.add_role_to_user(us,u)

# db.session.commit()
