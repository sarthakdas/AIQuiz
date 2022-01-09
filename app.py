from flask import Flask
from flask import redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy

from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security
from flask_security import current_user

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from models import *

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))

class StudentMixin:
    def is_accessible(self):
        return current_user.has_role('student')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass

class HomeAdminView(AdminMixin, AdminIndexView):
    pass

class BaseModelView(ModelView):
    def on_model_change(self, form, model,is_created):
        if is_created:
            try:
                model.generate_slug()
            except:
                pass
        return super().on_model_change(form,model,is_created)

class PostAdminView(AdminMixin, BaseModelView):
    form_columns= ['title', 'body', 'answer','tags']

class TagAdminView(AdminMixin, BaseModelView):
    form_columns= ['title', 'posts']

class UserAdminView(AdminMixin, BaseModelView):
    form_columns= ['email', 'password', 'roles']

admin = Admin(app, 'FlaskApp', url="/", index_view=HomeAdminView(name="home"))

admin.add_view(PostAdminView(Post, db.session))
admin.add_view(TagAdminView(Tag, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(Scorecard, db.session))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)