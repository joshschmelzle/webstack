from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl

    PROJECT_NAME: str

    class Config:
        case_sensitive = True


settings = Settings()
