# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/8 11:12'
from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

from . import views