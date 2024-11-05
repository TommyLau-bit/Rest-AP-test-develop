**App2** is a dynamic data visualization web application that leverages the REST API (App1) to provide users with an intuitive interface for analyzing and interpreting the Metropolitan Police Service's performance in handling Freedom of Information Requests and Appeals. Our web app offers interactive and informative dashboards, empowering users to gain valuable insights and make informed decisions based on the provided data.


### Prerequisites
To work with this application, you'll need the following:

1. **GitHub**: You must have access to GitHub for source code control.

2. **Python Environment**: You should use a Python coding environment such as Visual Studio Code, PyCharm Professional, or a similar tool.

3. **Flask**: This application is built using the Flask Python library to create the core web application.

4. **SQLite**: SQLite is used as the database for this application.

5. **ChromeDriver**: If you plan to run the Selenium test code, you'll need ChromeDriver installed and configured.

### Installation
=======

## Introduction
This Flask application serves as a REST API for storing and retrieving information related to the Metropolitan Police Freedom of Information data. It allows users to access and manage data related to police cases and freedom of information requests.

## Prerequisites
To work with this application, you'll need the following:

1. **GitHub**: You must have access to GitHub for source code control. Repositories should be created in GitHub Classroom to facilitate access for tutors and PGTAs.

2. **Python Environment**: You should use a Python coding environment such as Visual Studio Code, PyCharm Professional, or a similar tool. Jupyter notebooks are not an accepted submission format for this coursework.

3. **Flask**: This application is built using the Flask Python library to create the core REST API. You may use additional Python libraries to support your work.

4. **.pdf or .md Format**: All written content should be combined into a single file and submitted either as a PDF (named `comp0034-coursework1.pdf`) or markdown (named `comp0034-coursework1.md`) as appropriate.

## Installation
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
To set up and install this application, follow these steps:

1. Clone the GitHub repository:
   ```shell
<<<<<<< HEAD
   git clone 'https://github.com/ucl-comp0035/comp0034-cw2i-TommyLau-bit.git'

2. Change to project directory:
   cd /Users/tommy/github-classroom/comp0034-cw2i-TommyLau-bit
=======
   git clone https://github.com/ucl-comp0035/comp0034-cw1i-TommyLau-bit.git

2. Change to the project directory:
    cd /Users/tommy/github-classroom/comp0034-cw1i-TommyLau-bit
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1

3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

<<<<<<< HEAD
4. Check pip is the latest versions: pip install --upgrade pip

5. Install dependencies:
    pip install -r requirements.txt
    pip install plotly pandas
=======
4. Install dependencies:
    pip install -r requirements.txt
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1
    pip install Flask
    pip install flask_marshmallow
    pip install Flask-Migrate
    pip install marshmallow-sqlalchemy
    pip install pytest
    pip install -e .
<<<<<<< HEAD
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




=======

4. Run Flask application:
    python app.py or flask --app src run --debug

5. Stop application:
    ctrl + c

6. To run tests:
    pytest
>>>>>>> 80d383b5124e4d5eab5e0f8fa6c3685fca041ae1

