from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired

# Case Form
class CaseForm(FlaskForm):
    case_type = SelectField('Case Type', choices=[('FOIA', 'FOIA'), ('Other', 'Other')], validators=[DataRequired()])
    status = SelectField('Status', choices=[('Open', 'Open'), ('Closed', 'Closed')], validators=[DataRequired()])
    request_received_year = IntegerField('Request Received Year', validators=[DataRequired()])
    request_received_month = SelectField('Request Received Month', choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], validators=[DataRequired()])
    request_closed_year = IntegerField('Request Closed Year', validators=[DataRequired()])
    request_closed_month = SelectField('Request Closed Month', choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], validators=[DataRequired()])

# Complaint Form
class ComplaintForm(FlaskForm):
    reason_grouped = SelectField('Reason Grouped', choices=[('Reason 1', 'Reason 1'), ('Reason 2', 'Reason 2'), ('Reason 3', 'Reason 3')], validators=[DataRequired()])

# Dashboard Form
class DashboardForm(FlaskForm):
    active_days = StringField('Active Days')
    closed_on_time = StringField('Closed on Time')
    case_active_grouped = StringField('Case Active Grouped')

# Filter Form
class FilterForm(FlaskForm):
    criteria = StringField('Criteria')
