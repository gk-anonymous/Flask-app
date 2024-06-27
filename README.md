# Flask-app
# Flask Web Application

This is a simple Flask web application with multiple routes.

## Project Structure

flask-app/
│
├── app.py
├── env/
│ └── ... (virtual environment files)
└── README.md



## Requirements

- Python 3.x
- Flask

## Setup

### 1. Create a Virtual Environment

Before installing Flask, it is a good practice to create a virtual environment. This helps in managing dependencies specific to this project.

# Create a virtual environment
python -m venv env

# Activate the virtual environment


# On Windows:
env\Scripts\activate


# On macOS/Linux:
source env/bin/activate
2. Install Flask


Once the virtual environment is activated, install Flask using pip.

pip install Flask


Running the Application
To run the application, use the following command:

python app.py


The application will start and be accessible at http://127.0.0.1:5000/.

3. Using Flask CLI
Alternatively, you can use Flask CLI which provides better management for development environments.

Set the environment variables:


# On Windows:
set FLASK_APP=app.py
set FLASK_ENV=development

# On macOS/Linux:
export FLASK_APP=app.py


export FLASK_ENV=development


Run the app using Flask CLI:


flask run
Application Routes


The application has the following routes:

/ - Home page
/home - Home page
/login - Login page
