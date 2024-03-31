# Import necessary modules
from flask import current_app as app, jsonify, request
from .models import User, Case, Complaint, Dashboard, Filter
from .schemas import UserSchema, CaseSchema, ComplaintSchema, DashboardSchema, FilterSchema
from . import db  # Import the SQLAlchemy instance
from flask import Flask, render_template,  flash, redirect, url_for, request
from flask_login import login_required, current_user 
from .figures import dashboard_chart, complaint_chart, dashboard_active_cases_chart, get_complaint_reasons_distribution, case_closure_time_distribution
from .forms import CaseForm, ComplaintForm, DashboardForm, FilterForm
from flask_login import logout_user

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

# Define the routes
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

# Add a new route to display all cases
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

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    user = db.session.query(User).get_or_404(user_id)
    return render_template('user_profile.html', user=user)

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
    
