from wtforms import Form, StringField, TextAreaField, FileField, validators

class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    image = FileField('Image')
    tags = StringField('Tags (seperate using comma)')
