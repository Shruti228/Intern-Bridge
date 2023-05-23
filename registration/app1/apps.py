from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'app1'
from flask import Flask

app = Flask(__name__)

# Add your routes and other Flask code here

# Route for serving the favicon.ico file
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# Run the Flask application
if __name__ == '__main__':
    app.run()
