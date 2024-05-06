from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, validator

#基本设置，用于main.py中的启动，并读取.env中的环境配置
class Settings(BaseSettings):
    PROJECT_NAME: str = "OrderSystem"
    PROJECT_DESCRIPTION: str = '这是一个网上订单系统'
    pass

    class Config:
        #设置大小写敏感以及环境变量文件
        case_sensitive = True
        env_file = '.env'

settings = Settings()