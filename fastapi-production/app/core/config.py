from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_FROM: str
    MAIL_FROM_NAME: str
    TEST_RECEIVER_EMAIL: str | None = None


    


    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )



settings = Settings()