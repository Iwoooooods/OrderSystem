from fastapi import Form, HTTPException

from model.base import User
from schema.base import UserQuery
from api.service import create_token
from crud.crud_user import crud_get_multi_by_condition

class AuthService:
    def __init__(self) -> None:
        pass

    def authenticate(self, api_in: Form(), db):
        user = User(user_name=api_in.user_name, pwd=api_in.password)
        #根据用户名查找用户列表 => [{'id', 'created_at', 'modified_at', 'username', 'pwd'}]
        user_list = crud_get_multi_by_condition(user.__dict__, db)
        #读取数据库验证用户
        result = []
        if user_list:
            for user in user_list:
                result.append(user)
            return result
        else:
            raise HTTPException(detail='Incorrect Credentials', status_code=401)

auth_service = AuthService()

