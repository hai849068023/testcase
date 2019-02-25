# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/8 10:58'
from flask import Flask

app = Flask(__name__)

from .home import home as home_blueprint

app.register_blueprint(home_blueprint)