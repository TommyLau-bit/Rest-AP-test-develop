# Import necessary modules
from flask import current_app as app, jsonify, request
from .models import User, Case, Complaint, Dashboard, Filter
from .schemas import UserSchema, CaseSchema, ComplaintSchema, DashboardSchema, FilterSchema
from . import db  # Import the SQLAlchemy instance
<<<<<<< HEAD
from flask import Flask, render_template,  flash, redirect, url_for, request
from flask_login import login_required, current_user 
from .figures import dashboard_chart, complaint_chart, dashboard_active_cases_chart, get_complaint_reasons_distribution, case_closure_time_distribution
from .forms import CaseForm, ComplaintForm, DashboardForm, FilterForm
from flask_login import logout_user
=======

>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1

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

<<<<<<< HEAD
@app.route('/', methods=['GET'])
def index():
    """Returns the home page with featured cases, complaints, and dashboard metrics."""
    recent_cases = Case.query.order_by(Case.request_received_year.desc(), Case.request_received_month.desc()).limit(5).all()
    recent_complaints = Complaint.query.order_by(Complaint.id.desc()).limit(5).all()
    latest_dashboard = Dashboard.query.order_by(Dashboard.id.desc()).first()
    
    return render_template('index.html', 
                           recent_cases=recent_cases, 
                           recent_complaints=recent_complaints,
                           latest_dashboard=latest_dashboard)

@app.route('/charts')
def display_charts():
    # Generate all charts
    dashboard_chart_html = dashboard_chart()
    complaint_chart_html = complaint_chart()
    dashboard_active_cases_chart_html = dashboard_active_cases_chart()
    complaint_reasons_distribution_html = get_complaint_reasons_distribution()
    case_closure_time_distribution_html = case_closure_time_distribution()

    # Pass all chart HTML strings to the template
    return render_template('charts.html', 
                           dashboard_chart_html=dashboard_chart_html,
                           complaint_chart_html=complaint_chart_html,
                           dashboard_active_cases_chart_html=dashboard_active_cases_chart_html,
                           complaint_reasons_distribution_html=complaint_reasons_distribution_html,
                           case_closure_time_distribution_html=case_closure_time_distribution_html)

@app.route("/add_form", methods=["GET", "POST"])
def add_form():
    # Create instances of the forms
    case_form = CaseForm()
    complaint_form = ComplaintForm()
    dashboard_form = DashboardForm()
    filter_form = FilterForm()

    if request.method == "POST":
        # Check which form was submitted
        if case_form.validate_on_submit():
            # Logic for handling CaseForm submission
            # You can access form data using case_form.data
            flash("Case form submitted successfully!", "success")
            return redirect(url_for("index"))
        elif complaint_form.validate_on_submit():
            # Logic for handling ComplaintForm submission
            # You can access form data using complaint_form.data
            flash("Complaint form submitted successfully!", "success")
            return redirect(url_for("index"))
        elif dashboard_form.validate_on_submit():
            # Logic for handling DashboardForm submission
            # You can access form data using dashboard_form.data
            flash("Dashboard form submitted successfully!", "success")
            return redirect(url_for("index"))
        elif filter_form.validate_on_submit():
            # Logic for handling FilterForm submission
            # You can access form data using filter_form.data
            flash("Filter form submitted successfully!", "success")
            return redirect(url_for("index"))
        else:
            # If none of the forms pass validation, re-render the template with the forms and display error messages
            flash("Form submission failed. Please check the input.", "error")
            return render_template("add_form.html", case_form=case_form, complaint_form=complaint_form, dashboard_form=dashboard_form, filter_form=filter_form)

    # If it's a GET request, render the template with empty forms
    return render_template("add_form.html", case_form=case_form, complaint_form=complaint_form, dashboard_form=dashboard_form, filter_form=filter_form)

@app.route('/settings')
def settings():
    # Logic to render the settings page
    return render_template('settings.html')

@app.route('/logout')
@login_required
def logout():
    """Logout route."""
    logout_user()  # This will log out the current user
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))  # Redirect to the homepage or login page after logout

@app.route('/search')
def search_results():
    query = request.args.get('query')
    if query:
        # Assuming Case is the model and case_type is a searchable field
        cases = Case.query.filter(Case.case_type.ilike(f"%{query}%")).all()
        return render_template('search_results.html', cases=cases, query=query)
    return redirect(url_for('index'))

=======
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
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
<<<<<<< HEAD
    
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = db.session.query(User).get_or_404(user_id)
    return render_template('user_profile.html', user=user)

=======
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1

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
<<<<<<< HEAD
    
@app.route('/cases')
def list_cases():
    cases = db.session.query(Case).all()   # Fetch all cases
    return render_template('list_cases.html', cases=cases)

@app.route('/case/<int:case_id>')
def case_detail(case_id):
    case = db.session.query(Case).get_or_404(case_id)  # Fetch a single case by ID
    return render_template('case_detail.html', case=case)

@app.route('/case-closure-times')
def display_case_closure_times():
    """Displays a histogram of case closure times."""
    # Call your visualization function to get the chart HTML
    chart_html = case_closure_time_distribution()
    
    # Render a template, passing the chart HTML to be displayed
    return render_template('chart.html', fig_html=chart_html)

=======
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1

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

<<<<<<< HEAD
@app.route('/complaints')
def list_complaints():
    complaints = Complaint.query.all()  # Assuming Complaint.query.all() fetches all complaints
    return render_template('list_complaints.html', complaints=complaints)

@app.route('/complaint_chart')
def display_complaint_chart():
    chart_data = complaint_chart()
    return render_template('chart.html', fig_html=chart_data)

@app.route('/complaint-reasons')
def complaint_reasons():
    chart_html = get_complaint_reasons_distribution()
    return render_template("chart.html", fig_html=chart_html)

=======
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
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

<<<<<<< HEAD
=======

>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
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
<<<<<<< HEAD

@app.route('/dashboard')
@login_required  # Ensure only authenticated users can access this route
def show_dashboard():
    dashboard_data = Dashboard.query.filter_by(user_id=current_user.id).first()  # Get the first dashboard entry for the user
    return render_template('dashboard.html', dashboard_data=dashboard_data)

@app.route('/chart')
def display_chart():
    chart_data = dashboard_chart(db)
    return render_template('chart.html', fig_html=chart_data)

@app.route('/dashboard_active_cases_chart')
def display_dashboard_active_cases_chart():
    chart_data = dashboard_active_cases_chart()
    return render_template('chart.html', fig_html=chart_data)
=======
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
    
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

<<<<<<< HEAD
=======

>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
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
<<<<<<< HEAD

=======
    
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not Found"}), 404

<<<<<<< HEAD
@app.route('/')
def hello():
    return f"Hello!"

=======
 
@app.route('/')
def hello():
    return f"Hello!"
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
