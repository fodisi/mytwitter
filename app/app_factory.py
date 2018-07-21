#!/usr/bin/env python3

from flask import Flask


class ApplicationFactory():

    @staticmethod
    def create_application(config_pyfile: str) -> Flask:
        app = Flask(__name__)
        app.config.from_pyfile(config_pyfile)
        return app
