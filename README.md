# COMP0034 Coursework 2 2023/24
COMP0034 Coursework 2 starter repository

## MyApp

### Introduction

**App2** is a dynamic data visualization web application that leverages the REST API (App1) to provide users with an intuitive interface for analyzing and interpreting the Metropolitan Police Service's performance in handling Freedom of Information Requests and Appeals. Our web app offers interactive and informative dashboards, empowering users to gain valuable insights and make informed decisions based on the provided data.


### Prerequisites
To work with this application, you'll need the following:

1. **GitHub**: You must have access to GitHub for source code control.

2. **Python Environment**: You should use a Python coding environment such as Visual Studio Code, PyCharm Professional, or a similar tool.

3. **Flask**: This application is built using the Flask Python library to create the core web application.

4. **SQLite**: SQLite is used as the database for this application.

5. **ChromeDriver**: If you plan to run the Selenium test code, you'll need ChromeDriver installed and configured.

### Installation
To set up and install this application, follow these steps:

1. Clone the GitHub repository:
   ```shell
   git clone 'https://github.com/ucl-comp0035/comp0034-cw2i-TommyLau-bit.git'

2. Change to project directory:
   cd /Users/tommy/github-classroom/comp0034-cw2i-TommyLau-bit

3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Check pip is the latest versions: pip install --upgrade pip

5. Install dependencies:
    pip install -r requirements.txt
    pip install plotly pandas
    pip install Flask
    pip install flask_marshmallow
    pip install Flask-Migrate
    pip install marshmallow-sqlalchemy
    pip install pytest
    pip install -e .
    pip install Flask-WTF
    pip install WTForms-SQLAlchemy
    pip install selenium pytest
    pip install requests
    pip install Flask-Login

6. Run Flask application:
    python app.py or 'flask --app src run --debug'

7. To run tests:
    'pytest' or 'pytest -v'

8. Stop application:
    ctrl + c





