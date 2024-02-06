# COMP0034 Coursework 1 2023/24
COMP0034 Coursework 1 starter repository
# Metropolitan Police Freedom of Information Data API

## Introduction
This Flask application serves as a REST API for storing and retrieving information related to the Metropolitan Police Freedom of Information data. It allows users to access and manage data related to police cases and freedom of information requests.

## Prerequisites
To work with this application, you'll need the following:

1. **GitHub**: You must have access to GitHub for source code control. Repositories should be created in GitHub Classroom to facilitate access for tutors and PGTAs.

2. **Python Environment**: You should use a Python coding environment such as Visual Studio Code, PyCharm Professional, or a similar tool. Jupyter notebooks are not an accepted submission format for this coursework.

3. **Flask**: This application is built using the Flask Python library to create the core REST API. You may use additional Python libraries to support your work.

4. **.pdf or .md Format**: All written content should be combined into a single file and submitted either as a PDF (named `comp0034-coursework1.pdf`) or markdown (named `comp0034-coursework1.md`) as appropriate.

## Installation
To set up and install this application, follow these steps:

1. Clone the GitHub repository:
   ```shell
   git clone https://github.com/ucl-comp0035/comp0034-cw1i-TommyLau-bit.git

2. Change to the project directory:
    cd /Users/tommy/github-classroom/comp0034-cw1i-TommyLau-bit

3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install dependencies:
    pip install -r requirements.txt
    pip install Flask
    pip install flask_marshmallow
    pip install Flask-Migrate
    pip install marshmallow-sqlalchemy
    pip install pytest
    pip install -e .

4. Run Flask application:
    python app.py or flask --app src run --debug

5. Stop application:
    ctrl + c

6. To run tests:
    pytest

