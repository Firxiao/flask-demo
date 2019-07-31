from flask import Blueprint
bar = Blueprint('bar', __name__)  # type: Blueprint
from . import views