from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    #you can return a stastus value, we use it for the first time because default is 200
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    #you can return a stastus value, we use it for the first time because default is 200
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    #you can return a stastus value, we use it for the first time because default is 200
    return render_template('errors/500.html'), 500