from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CompanyForm(FlaskForm):
    company_a = StringField("Company A", validators=[DataRequired()])
    company_b = StringField("Company B", validators=[DataRequired()])
    submit = SubmitField('Submit Companies')