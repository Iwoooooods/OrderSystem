import os
import httpx

from fastapi import Form, HTTPException, Depends
from loguru import logger
from model.base import User
from crud.crud_user import crud_get_one_by_condition, crud_add_user
from middleware.token import create_access_token
from enum import Enum

class UserType(Enum):
    CUSTOMER = 'customer'
    MERCHANT = 'merchant'

class AuthService:
    def __init__(self) -> None:
        pass

    async def authenticate(self, db,  api_in: Form = Depends()):
        user = User(user_name=api_in.user_name, pwd=api_in.password)
        #根据用户名查找用户列表 => [{'id', 'created_at', 'modified_at', 'username', 'pwd'}]
        user_exist = crud_get_one_by_condition(db, user.__dict__)
        if user_exist:
            token = create_access_token(user.to_dict())
            with httpx.AsyncClient() as client:
                if api_in.user_type == UserType.CUSTOMER:
                    response = await client.get(url=os.getenv('DEV_API_URL')+'/customer/home',
                                                headers={'Authorization': f'Bearer {token}'})
                    return response.json()
                elif api_in.user_type == UserType.MERCHANT:
                    response = await client.get(url=os.getenv('DEV_API_URL')+'/merchant/home',
                                                headers={'Authorization': f'Bearer {token}'})
                    return response.json()
        else:
            logger.info('login failed due to: Incorrect Credentials')
            raise HTTPException(detail='Incorrect Credentials', status_code=401)

    async def register(self, db,  api_in: Form = Depends()):
        user = User(user_name=api_in.user_name, pwd=api_in.password)
        if crud_get_one_by_condition(db, {'user_name': api_in.user_name}):
            logger.info('User already exists')
            raise HTTPException(detail='User already exists', status_code=401)
        crud_add_user(db, user)
        logger.info(f'User register: {user.user_name} - {user.email}')
        token = create_access_token(user.to_dict())
        with httpx.AsyncClient() as client:
            if api_in.user_type == UserType.CUSTOMER:
                response = await client.get(url=os.getenv('DEV_API_URL') + '/customer/home/',
                                            headers={'Authorization': f'Bearer {token}'})
                return response.json()
            elif api_in.user_type == UserType.CUSTOMER:
                response = await client.get(url=os.getenv('DEV_API_URL') + '/merchant/home/',
                                            headers={'Authorization': f'Bearer {token}'})
                return response.json()
        raise HTTPException(detail='Register failed')

auth_service = AuthService()

