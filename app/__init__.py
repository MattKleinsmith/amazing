from graphql.utils import schema_printer
import os
from flask import Flask, request, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import generate_csrf
from flask_login import LoginManager
from .models import db, User
from .seeds import seed_commands
from .config import Config
from . import api
from .schema import schema

from flask_graphql import GraphQLView

app = Flask(__name__, static_folder='../react-app/build', static_url_path='/')
app.cli.add_command(seed_commands)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(api.bp)
db.init_app(app)
Migrate(app, db, render_as_batch=True)

login = LoginManager(app)
login.login_view = "api.session.unauthorized"


my_schema_str = schema_printer.print_schema(schema)
fp = open("schema.graphql", "w")
fp.write(my_schema_str)
fp.close()

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        print("REDIRECTING", "-"*50)
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    """
    This route will direct to the public directory in our
    react builds in the production environment for favicon
    or index.html requests
    """
    if path == 'favicon.ico':
        return app.send_from_directory('public', 'favicon.ico')
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route("/api/docs")
def api_help():
    """
    Returns all API routes and their doc strings
    """
    acceptable_methods = ['POST', 'GET', 'PUT', 'DELETE']
    route_list = {rule.rule: [[method for method in rule.methods if method in acceptable_methods],
                              app.view_functions[rule.endpoint].__doc__]
                  for rule in app.url_map.iter_rules() if rule.endpoint != 'static'}
    return route_list
