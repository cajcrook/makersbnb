# MakersBnB Python Project 

This repo contains our Python project, MakersBnb.
Alongside Python we used Flask and Pytest.

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
