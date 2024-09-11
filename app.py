"""
This project is meant to generate a simple website 
using Python flask. The website has four routes 
(about me, dc, index, marvel pages). In those websites 
are fun facts about Marvel and DC, an About Me page, and
a Home page as well. 
"""

from datetime import datetime
from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def index():
    """
    Render the home page with the current time.
    Returns:
        str: Rendered HTML template.
    """
    # Get the current date and time, and format it as "Month day, Year Hour:MinuteAM/PM"
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    # Render the 'index.html' template with the formatted current time
    return render_template('index.html', current_time=current_time)

# Define a route for the about page
@app.route('/about')
def about():
    """
    Render the about page with the current time.
    Returns:
        str: Rendered HTML template.
    """
    # Get the current date and time, and format it as "Month day, Year Hour:MinuteAM/PM"
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    # Render the 'about.html' template with the formatted current time
    return render_template('about.html', current_time=current_time)

# Define a route for the marvel page
@app.route('/marvel')
def marvel():
    """
    Render the Marvel page with the current time.
    Returns:
        str: Rendered HTML template.
    """
    # Get the current date and time, and format it as "Month day, Year Hour:MinuteAM/PM"
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    # Render the 'marvel.html' template with the formatted current time
    return render_template('marvel.html', current_time=current_time)

# Define a route for the dc page
@app.route('/dc')
def dc():
    """
    Render the DC page with the current time.
    Returns:
        str: Rendered HTML template.
    """
    # Get the current date and time, and format it as "Month day, Year Hour:MinuteAM/PM"
    current_time = datetime.now().strftime("%B %d, %Y %I:%M%p")
    # Render the 'dc.html' template with the formatted current time
    return render_template('dc.html', current_time=current_time)

# Run the application if this script is executed
if __name__ == '__main__':
    app.run()
