from model.base import User

def create_token(user:User) -> str:
    return user.id+user.created_at+user.user_name+user.pwd