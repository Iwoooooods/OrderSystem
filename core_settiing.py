from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME : str = "OrderSystem"
    PROJECT_DESCRIPTION : str
    PROJECT_VERSION : str

    LOCAL_DATABASE_URL : str
    REMOTE_DATABASE_URL : str

    SECRECT_KEY : str
    ALGORITHM : str

    class Config:
        case_sensitive = True
        env_file = ".env"

setting = Settings()

if __name__ == '__main__':
    print(setting.LOCAL_DATABASE_URL)