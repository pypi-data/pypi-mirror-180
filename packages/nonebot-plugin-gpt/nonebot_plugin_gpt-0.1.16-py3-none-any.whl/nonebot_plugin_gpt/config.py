from nonebot import get_driver
from pydantic import BaseModel, Extra
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    gpt_session_token: str
    gpt_api_key: str
    gpt_sudoers: list[int]
    gpt_probability: float = 0
    gpt_proxy: Optional[str] = None
    gpt_api_baseurl: str = 'https://chat.openai.com'
    gpt_timeout: int = 20
    gpt_request_minimal_interval: int = 5


gpt_config: Config = Config.parse_obj(get_driver().config)
