from flask_jwt_extended import get_jwt_identity
from functools import wraps
from models import User

def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user or user.role != role:
                return {"message": "Unauthorized"}, 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
