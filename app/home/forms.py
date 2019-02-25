# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/8 11:30'
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError


# 用户登录
class LoginUser(FlaskForm):
    wxname = StringField(
        '用户名',
        validators=[DataRequired('请输入账号！')],
        description='账号',
        render_kw={'class': "form-control", 'placeholder': "用户名"})
    password = PasswordField(
        '密码',
        validators=[DataRequired('请输入密码！')],
        description='账号',
        render_kw={'class': "form-control", 'placeholder': "用户名"})
    submit = SubmitField('登录', render_kw={'class': 'btn btn-primary block full-width m-b'})


# 添加用例
class AddCase(FlaskForm):
    name = StringField(
        '用例名称',
        validators=[DataRequired('请输入用例名称！')],
        description='名称',
        render_kw={'type':"text", 'placeholder':"用例名称",'class':"form-control"}
    )