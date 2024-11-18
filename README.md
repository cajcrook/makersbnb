# MakersBnB Python Project 
## WORK IN PROGRESS

This repo contains our group project - MakersBnb. 
It is a simple replica of a popular holiday rental website build using Python, Flask and Pytest.

Current functionality:
- Add user details.
- Add properties.
- Search property by date.
- Request/ Approve reservations.

Currently scope of update:
- Update CSS structure to be more uniform across pages.
- Improve UI.
- Improve navigation buttons across app.
- Review password validation.
- Automate currency selection.
- Update booking process.



## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install

# Create a test and development database
(makersbnb-venv); brew install postgresql@15
(makersbnb-venv); createdb MAKERSBNB
(makersbnb-venv); createdb MAKERSBNB_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```
