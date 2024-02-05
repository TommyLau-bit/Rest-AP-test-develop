# Import necessary modules
from flask import current_app as app, jsonify, request
from .models import User, Case, Complaint, Dashboard, Filter
from .schemas import UserSchema, CaseSchema, ComplaintSchema, DashboardSchema, FilterSchema
from . import db  # Import the SQLAlchemy instance


# Initialize Marshmallow Schemas
user_schema = UserSchema()
users_schema = UserSchema(many=True)
case_schema = CaseSchema()
cases_schema = CaseSchema(many=True)
complaint_schema = ComplaintSchema()
complaints_schema = ComplaintSchema(many=True)
dashboard_schema = DashboardSchema()
dashboards_schema = DashboardSchema(many=True)
filter_schema = FilterSchema()
filters_schema = FilterSchema(many=True)

# User Routes
@app.route("/users", methods=["GET"])
def get_users():
    """Returns a list of users and their details in JSON."""
    all_users = User.query.all()  # Query all users
    result = users_schema.dump(all_users)  # Serialize the data
    return jsonify(result)  # Return JSON response

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = db.session.get(User, user_id) 
    if user:
        return jsonify(user_schema.dump(user))
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    user_json = request.get_json()
    user = user_schema.load(user_json)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": f"User added with id= {user.id}"}), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User deleted with id= {user_id}"})
    else:
        return jsonify({"message": "User not found"}), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = db.session.get(User, user_id)
    if user:
        user_json = request.get_json()
        user_update = user_schema.load(user_json, instance=user, partial=True)
        db.session.add(user_update)
        db.session.commit()
        return jsonify(user_schema.dump(user_update))
    else:
        return jsonify({"message": "User not found"}), 404

# Case routes   
@app.route("/cases", methods=["GET"])
def get_cases():
    """Returns a list of cases and their details in JSON."""
    all_cases = Case.query.all()  # Query all cases
    result = cases_schema.dump(all_cases)  # Serialize the data
    return jsonify(result)  # Return JSON response

@app.route("/cases/<int:case_id>", methods=["GET"])
def get_case(case_id):
    """Returns the case with the given ID in JSON."""
    case = db.session.get(Case, case_id)
    if case:
        return jsonify(case_schema.dump(case))
    else:
        return jsonify({"message": "Case not found"}), 404

@app.route('/cases', methods=['POST'])
def add_case():
    case_json = request.get_json()
    case = case_schema.load(case_json)
    
    # Include the new columns from the request JSON
    case.status = case_json['status']
    case.request_received_year = case_json['request_received_year']
    case.request_received_month = case_json['request_received_month']
    case.request_closed_year = case_json['request_closed_year']
    case.request_closed_month = case_json['request_closed_month']
    
    db.session.add(case)
    db.session.commit()
    return jsonify({"message": f"Case added with id= {case.id}"}), 201

@app.route('/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    """Deletes a case."""
    case = db.session.get(Case, case_id)
    if case:
        db.session.delete(case)
        db.session.commit()
        return jsonify({"message": f"Case deleted with id= {case_id}"})
    else:
        return jsonify({"message": "Case not found"}), 404

@app.route("/cases/<int:case_id>", methods=["PUT"])
def update_case(case_id):
    """Updates a case."""
    case = db.session.get(Case, case_id)
    if case:
        case_json = request.get_json()
        case_update = case_schema.load(case_json, instance=case, partial=True)
        db.session.add(case_update)
        db.session.commit()
        return jsonify(case_schema.dump(case_update))
    else:
        return jsonify({"message": "Case not found"}), 404

# Complaint routes
@app.route("/complaints", methods=["GET"])
def get_complaints():
    """Returns a list of complaints and their details in JSON."""
    all_complaints = Complaint.query.all()  # Query all complaints
    result = complaints_schema.dump(all_complaints)  # Serialize the data
    return jsonify(result)  # Return JSON response

@app.route("/complaints/<int:complaint_id>", methods=["GET"])
def get_complaint(complaint_id):
    """Returns the complaint with the given ID in JSON."""
    complaint = db.session.get(Complaint, complaint_id)
    if complaint:
        return jsonify(complaint_schema.dump(complaint))
    else:
        return jsonify({"message": "Complaint not found"}), 404

@app.route('/complaints', methods=['POST'])
def add_complaint():
    """Adds a new complaint."""
    complaint_json = request.get_json()
    
    # Create a new Complaint object and set its attributes
    complaint = Complaint(
        reason_grouped=complaint_json['reason_grouped'],
        user_id=complaint_json['user_id'],
        # Include other new columns here
    )
    
    db.session.add(complaint)
    db.session.commit()
    
    return jsonify({"message": f"Complaint added with id= {complaint.id}"}), 201

@app.route('/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint(complaint_id):
    """Deletes a complaint."""
    complaint = db.session.get(Complaint, complaint_id)
    if complaint:
        db.session.delete(complaint)
        db.session.commit()
        return jsonify({"message": f"Complaint deleted with id= {complaint_id}"})
    else:
        return jsonify({"message": "Complaint not found"}), 404

@app.route("/complaints/<int:complaint_id>", methods=["PUT"])
def update_complaint(complaint_id):
    """Updates a complaint."""
    complaint = db.session.get(Complaint, complaint_id)
    if complaint:
        complaint_json = request.get_json()
        complaint_update = complaint_schema.load(complaint_json, instance=complaint, partial=True)
        db.session.add(complaint_update)
        db.session.commit()
        return jsonify(complaint_schema.dump(complaint_update))
    else:
        return jsonify({"message": "Complaint not found"}), 404

# Dashboard routes 
@app.route("/dashboards", methods=["GET"])
def get_dashboards():
    """Returns a list of dashboards and their details in JSON."""
    all_dashboards = Dashboard.query.all()  # Query all dashboards
    result = dashboards_schema.dump(all_dashboards)  # Serialize the data
    return jsonify(result)  # Return JSON response

@app.route("/dashboards/<int:dashboard_id>", methods=["GET"])
def get_dashboard(dashboard_id):
    """Returns the dashboard with the given ID in JSON."""
    dashboard = db.session.get(Dashboard, dashboard_id)
    if dashboard:
        return jsonify(dashboard_schema.dump(dashboard))
    else:
        return jsonify({"message": "Dashboard not found"}), 404

@app.route('/dashboards', methods=['POST'])
def add_dashboard():
    dashboard_json = request.get_json()
    dashboard = dashboard_schema.load(dashboard_json)
    
    # Include the new columns from the request JSON
    dashboard.active_days = dashboard_json['active_days']
    dashboard.closed_on_time = dashboard_json['closed_on_time']
    dashboard.case_active_grouped = dashboard_json['case_active_grouped']
    
    db.session.add(dashboard)
    db.session.commit()
    return jsonify({"message": f"Dashboard added with id= {dashboard.id}"}), 201


@app.route('/dashboards/<int:dashboard_id>', methods=['DELETE'])
def delete_dashboard(dashboard_id):
    """Deletes a dashboard."""
    dashboard = db.session.get(Dashboard, dashboard_id)
    if dashboard:
        db.session.delete(dashboard)
        db.session.commit()
        return jsonify({"message": f"Dashboard deleted with id= {dashboard_id}"})
    else:
        return jsonify({"message": "Dashboard not found"}), 404

@app.route("/dashboards/<int:dashboard_id>", methods=["PUT"])
def update_dashboard(dashboard_id):
    """Updates a dashboard."""
    dashboard = db.session.get(Dashboard, dashboard_id)
    if dashboard:
        dashboard_json = request.get_json()
        
        # Update the new columns from the request JSON
        dashboard.active_days = dashboard_json['active_days']
        dashboard.closed_on_time = dashboard_json['closed_on_time']
        dashboard.case_active_grouped = dashboard_json['case_active_grouped']
        dashboard_update = dashboard_schema.load(dashboard_json, instance=dashboard, partial=True)
        db.session.add(dashboard_update)
        db.session.commit()
        return jsonify(dashboard_schema.dump(dashboard_update))
    else:
        return jsonify({"message": "Dashboard not found"}), 404
    
# filter routes 
@app.route("/filters", methods=["GET"])
def get_filters():
    """Returns a list of filters and their details in JSON."""
    all_filters = Filter.query.all()  # Query all filters
    result = filters_schema.dump(all_filters)  # Serialize the data
    return jsonify(result)  # Return JSON response

@app.route("/filters/<int:filter_id>", methods=["GET"])
def get_filter(filter_id):
    """Returns the filter with the given ID in JSON."""
    filter_ = db.session.get(Filter, filter_id)
    if filter_:
        return jsonify(filter_schema.dump(filter_))
    else:
        return jsonify({"message": "Filter not found"}), 404

@app.route('/filters', methods=['POST'])
def add_filter():
    """Adds a new filter."""
    filter_json = request.get_json()
    filter_ = filter_schema.load(filter_json)
    db.session.add(filter_)
    db.session.commit()
    return jsonify({"message": f"Filter added with id= {filter_.id}"}), 201


@app.route('/filters/<int:filter_id>', methods=['DELETE'])
def delete_filter(filter_id):
    """Deletes a filter."""
    filter_ = db.session.get(Filter, filter_id)
    if filter_:
        db.session.delete(filter_)
        db.session.commit()
        return jsonify({"message": f"Filter deleted with id= {filter_id}"})
    else:
        return jsonify({"message": "Filter not found"}), 404

@app.route("/filters/<int:filter_id>", methods=["PUT"])
def update_filter(filter_id):
    """Updates a filter."""
    filter_ = db.session.get(Filter, filter_id)
    if filter_:
        filter_json = request.get_json()
        filter_update = filter_schema.load(filter_json, instance=filter_, partial=True)
        db.session.add(filter_update)
        db.session.commit()
        return jsonify(filter_schema.dump(filter_update))
    else:
        return jsonify({"message": "Filter not found"}), 404
    
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

 
@app.route('/')
def hello():
    return f"Hello!"