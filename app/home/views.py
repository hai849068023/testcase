# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/1/8 11:13'
import datetime

from flask import render_template, request, url_for, jsonify

from app.models import db, Case, Task, Beizhu
from . import home


# 首页视图
@home.route('/')
def index():
    tasks = Task.query.filter_by(username=0).all()
    return render_template('home/index.html', data={'tasks': tasks})


# 待参数获取数据
@home.route('/<id>')
def userIndex(id):
    tasks = Task.query.filter_by(username=id).all()
    # for task in tasks:
    #     caselist = task.Cases_id
    #     for case in caselist:
    #         if case.is_validation != 0:
    #             is_active += 1
    return render_template('home/index.html', data={'tasks': tasks, 'userid': id})


# 登录视图
@home.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('home/login.html')


# 添加任务
@home.route('/addtask', methods=['POST'])
def addTask():
    data = request.values
    task = Task(chandao=data['chandao'], content=data['tasktitle'])
    db.session.add(task)
    db.session.commit()
    url = url_for('home.choiceTask', chandao=data['chandao'])
    return url


# 添加用例
@home.route('/addcase/<chandao>', methods=['POST'])
@home.route('/addcase', methods=['POST'])
def addCase(chandao):
    data = request.values
    case = Case(name=data['casename'], content=data['casecontent'], task_chandao=chandao)
    db.session.add(case)
    db.session.commit()
    url = url_for('home.choiceTask', chandao=chandao)
    return url


# 更新用例
@home.route('/editcase', methods=['GET', 'POST'])
def editCase():
    if request.method == 'GET':
        id = request.values
        case = Case.query.get(id['id'])
        data = {
            'id': case.id,
            'name': case.name,
            'content': case.content,
            'is_validation': case.is_validation
        }
        return jsonify(data)
    data = request.values
    datadict = {}
    for key, value in data.items():
        datadict[key] = value
    if 'inlineCheckbox1' in datadict and 'inlineCheckbox2' in datadict and 'inlineCheckbox3' in datadict:
        is_validation = 3
    elif 'inlineCheckbox1' in datadict and 'inlineCheckbox2' in datadict:
        is_validation = 2
    elif 'inlineCheckbox1' in datadict:
        is_validation = 1
    else:
        is_validation = 0
    case = Case.query.get(data['id'])
    case.name = datadict['name']
    case.content = datadict['content']
    case.is_validation = is_validation
    db.session.commit()
    return 'success'


# 获取备注信息
@home.route('/beizhu', methods=['GET', 'POST'])
def beizhu():
    time = datetime.datetime.now()
    if request.method == 'GET':
        id = request.values['id']
        beizhulist = Beizhu.query.filter_by(case_id=id).all()
        data = {}
        beizhuall = []
        for beizhu in beizhulist:
            beizhuall.append(beizhu.casenote + '</br>')
        data['beizhu'] = beizhuall
        data['time'] = time.strftime("%Y-%m-%d") + '_'
        return jsonify(data)
    postdata = request.values
    beizhu = Beizhu(casenote=postdata['casenote'], case_id=postdata['id'])
    db.session.add(beizhu)
    db.session.commit()
    return 'success'


# 删除用例
@home.route('/delcase', methods=['POST'])
def delCase():
    caseid = request.values
    data = int(caseid['caseid'])
    case = Case.query.get(data)
    if case:
        db.session.delete(case)
        db.session.commit()
        return 'success'
    else:
        return 'fail'


# 选择用例
@home.route('/choicetask/<chandao>')
@home.route('/choicetask')
def choiceTask(chandao, page=1):
    tasks = Task.query.all()
    userid = Task.query.filter_by(chandao=chandao).first()
    cases = Case.query.filter_by(task_chandao=chandao).all()
    # casespage = Case.query.paginate(1,per_page=10)  分页
    countnumber = len(cases)
    if cases:
        is_start = 1
    else:
        is_start = 0
    return render_template('home/index.html', data={
        'tasks': tasks,
        'cases': cases,
        'countnumber': countnumber,
        'is_start': is_start,
        'chandao': chandao,
        'userid': userid.username
    })


# 展示脑图
@home.route('/naotu')
def naoTu():
    return render_template('home/naotu.html')
