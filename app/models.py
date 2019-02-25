# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/8 11:28'
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from . import app
from datetime import datetime

# 数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1/testcase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 数据库迁移
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# 用户表
class Users(db.Model):
    __tablename__ = 'test_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, index=True)
    password = db.Column(db.String(100), nullable=False)


# 任务表
class Task(db.Model):
    __tablename__ = 'test_task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chandao = db.Column(db.Integer, index=True)
    content = db.Column(db.String(500))
    username = db.Column(db.Integer,nullable=False, index=True, default=0) # 0.预留 1.刘旭 2.林凤 3.蓉蓉
    Cases_id = db.relationship('Case', backref='task',lazy=True)


# 用例表
class Case(db.Model):
    __tablename__ = 'test_case'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    content = db.Column(db.Text)
    is_validation = db.Column(db.Integer, default=0)
    task_chandao = db.Column(db.Integer, db.ForeignKey('test_task.chandao'), nullable=False)
    beizhu = db.relationship('Beizhu', backref='case')


# 备注记录表
class Beizhu(db.Model):
    __tablename__ = 'test_beizhu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    casenote = db.Column(db.String(500))
    datatime = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    case_id = db.Column(db.Integer,db.ForeignKey('test_case.id'), nullable=False)



