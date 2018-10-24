from flask_wtf import Form
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])  # make sure it conforms to date
    timespent = StringField('Time Spent', validators=[DataRequired()])  # make sure it is a number
    content = TextAreaField('Things Learned', validators=[DataRequired()])
    resources = TextAreaField('Resources')
