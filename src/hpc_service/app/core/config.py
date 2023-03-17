from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "hpc_service"
    HPC_HOST: str = "127.0.0.1"

    class Config:
        env_prefix: str = "HPC_SERVICE_"
        case_sensitive = True


settings = Settings()
