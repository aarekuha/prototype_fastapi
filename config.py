# -*- coding: utf-8 -*-
import os
import dotenv


class Config():
    TAGS_METADATA = [
        {
            "name": "Main page",
            "response_description": "DESC_RESPONSE",
            "description": "Health check",
        },
    ]

    HTTP_401 = "Token invalid"

    def __init__(self):
        dotenv.load_dotenv()
        self.__dict__.update(os.environ)


config = Config()
