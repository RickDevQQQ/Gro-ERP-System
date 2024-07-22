from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):

    MODE: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    ECHO: bool

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def default_asyncpg_url(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


config = Config()
