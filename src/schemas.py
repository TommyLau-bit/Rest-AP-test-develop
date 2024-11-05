from .models import User, Case, Complaint, Dashboard, Filter
from . import db, ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session
        load_instance = True

class CaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Case
        sqla_session = db.session
        load_instance = True
        include_fk = True

<<<<<<< HEAD
    # Add fields for the new columns added
=======
    # Add fields for the new columns you've added
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
    status = ma.auto_field()
    request_received_year = ma.auto_field()
    request_received_month = ma.auto_field()
    request_closed_year = ma.auto_field()
    request_closed_month = ma.auto_field()

class ComplaintSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Complaint
        sqla_session = db.session
        load_instance = True
        include_fk = True

    # Include the new columns here
    reason_grouped = ma.auto_field()

class DashboardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dashboard
        sqla_session = db.session
        load_instance = True
        include_fk = True

    # Include the new columns here
    active_days = ma.auto_field()
    closed_on_time = ma.auto_field()
    case_active_grouped = ma.auto_field()

class FilterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Filter
        sqla_session = db.session
        load_instance = True
        include_fk = True
