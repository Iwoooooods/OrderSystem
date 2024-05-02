from fastapi import Form, HTTPException

from model.base import User
from crud.crud_user import crud_get_multi_by_condition

class AuthService:
    def __init__(self) -> None:
        pass

    def authenticate(self, api_in: Form, db):
        user = User(user_name=api_in.user_name, pwd=api_in.password)
        #根据用户名查找用户列表 => [{'id', 'created_at', 'modified_at', 'username', 'pwd'}]
        user_list = crud_get_multi_by_condition(db, user.__dict__)
        #读取数据库验证用户
        result = []
        from middleware.token import create_access_token
        if user_list:
            for user in user_list:
                token = create_access_token(user.to_dict())
                result.append(token)
            return result
        else:
            raise HTTPException(detail='Incorrect Credentials', status_code=401)

auth_service = AuthService()

