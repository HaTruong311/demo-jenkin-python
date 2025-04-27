from flask import Blueprint

# Create a Blueprint for our controller
controller_bp = Blueprint('controller', __name__)

@controller_bp.route('/api/hello', methods=['GET'])
def hello():
    """
    A simple GET endpoint that returns 'hello world'
    """
    return {'message': 'hello world'}
