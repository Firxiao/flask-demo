from flask import Blueprint
foo = Blueprint('foo', __name__)  # type: Blueprint
from . import views