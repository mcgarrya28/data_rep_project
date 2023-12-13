# data_rep_project
Data Representation Project

Required Packages:

1. flask
2. flask_restful
3. flask_sqlalchemy

The Flask application incorporates the Flask-RESTful API for handling CRUD operations on items and includes web pages for viewing, adding, and deleting items. Below is a summary of the key components:

Flask App Configuration:

The app is configured with an SQLite database using Flask-SQLAlchemy.
An instance of the app, Flask-RESTful API, and SQLAlchemy are created.

Database Model:

The Item class is defined as a simple model with an id (primary key) and a name field.

RESTful API Resource:

The ItemResource class is created to handle RESTful API operations (GET, PUT, DELETE) on individual items.

API Endpoint Registration:

The ItemResource is added as a resource to the Flask-RESTful API with the endpoint /api/item/<int:item_id>.

Web Page Routes:

The / route renders the index.html template, displaying a list of items.
The /add route handles the addition of a new item using a form.
The /delete/<int:item_id> route handles item deletion.

HTML Template:

The index.html template displays a list of items and provides a form to add new items. It also includes functionality to delete items.

Running the App:

The app is set to run in debug mode when executed directly.


