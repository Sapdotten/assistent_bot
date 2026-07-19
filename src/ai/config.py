from pydantic_settings import BaseSettings, SettingsConfigDict


class AiConfig(BaseSettings):
    api_key: str
    proxy_protocol: str = 'socks5'
    proxy_addr: str = "127.0.0.1"
    proxy_port: str = "10808"

    model_config = SettingsConfigDict(
        env_prefix="AI_",
        extra="ignore",
        env_file="./.docker/.env",
    )

    @property
    def proxy(self) -> str:
        return f"{self.proxy_protocol}://{self.proxy_addr}:{self.proxy_port}"
