#!/usr/bin/python
# coding=utf-8
import time
import random
import numpy as np
import xlrd2
from xlrd2 import xldate_as_tuple
import json
import calendar, time, os
from datetime import datetime
from werkzeug.datastructures import FileStorage
from flask import Flask, render_template, jsonify, request, redirect, url_for, session, Response
# 自己写的文件
import db
import get_data, sub_data
from page_utils import Pagination

app = Flask(__name__)
app.secret_key = 'znlpxt'
app.config['DEBUG'] = True


# 网站主页
@app.route('/')
def data_show():
    return render_template('index.html')


# 登录功能
@app.before_request
def is_login():
    # print(request.path)
    # print(session)
    if request.path == "/user_login" or request.path == "/login" or request.path == "/login_out" or request.path == "/":
        return None
    if request.path.startswith("/static"):
        return None
    if not session.get("user"):
        return redirect("/user_login")
    return None


@app.route('/user_login')
def user_login():
    return render_template('user_login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('user_login.html')
    user = request.form.get('usernum')
    pwd = request.form.get('password')
    flag = get_data.login_verify(user, pwd)
    #print(flag)
    if flag:
        session['user'] = user
        return redirect('/')
    return render_template('user_login.html')


@app.route('/login_out')
def login_out():
    del session['user']
    return redirect('/')


# 提交数据并预测
@app.route('/user_pre')
def user_pre():
    return render_template('user_pre.html')


@app.route('/to_excel', methods=['GET', 'POST'])
def to_excel():
    if request.method == 'POST':
        file = request.files.get('pre_file')
        if not file:
            return redirect('/user_pre')
        file_name = file.filename
        suffix = os.path.splitext(file_name)[-1]  # 获取文件后缀（扩展名）
        basePath = os.path.dirname(__file__)  # 当前文件所在路径print(basePath)
        nowTime = calendar.timegm(time.gmtime())  # 获取当前时间戳改文件名
        upload_path = os.path.join(basePath, 'upload',
                                   str(nowTime))  # 改到upload目录下# 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        upload_path = os.path.abspath(upload_path)  # 将路径转换为绝对路径
        file.save(upload_path + suffix)  # 保存文件
        file_add = upload_path + suffix
        file.seek(0)
        f = file.read()
        data_file = xlrd2.open_workbook(file_contents=f)
        # 选取sheet1
        table = data_file.sheet_by_index(0)
        data = []
        for row_num in range(1, table.nrows):
            data.append(table.row_values(row_num))
            data[row_num - 1][0] = int(table.row_values(row_num)[0])
            data[row_num - 1][4] = datetime(*xldate_as_tuple(table.row_values(row_num)[4], 0)).strftime('%Y/%m/%d')
            data[row_num - 1][5] = datetime(*xldate_as_tuple(table.row_values(row_num)[5], 0)).strftime('%Y/%m/%d')
        # print(data)
        return render_template('user_pre.html', datas=data, file=file_add)
    return redirect('/user_pre')


@app.route('/data_pre', methods=['POST'])
def data_pre():
    file = request.form.get('file')
    f = open(file, "rb").read()
    data_file = xlrd2.open_workbook(file_contents=f)
    table = data_file.sheet_by_index(0)
    feature = {}
    for col_num in range(0, table.ncols):
        feature[table.col_values(col_num)[0]] = table.col_values(col_num)[1:]
    #print(feature)
    flag = sub_data.sub_review_data(feature)
    result = '200'
    return Response(result)

#展示已审核数据
@app.route('/reviewed_data')
def reviewed_data():
    return render_template('reviewed_data.html')

#展示未审核数据
@app.route('/review_data')
def review_data():
    data = get_data.show_review()
    pager_obj = Pagination(request.args.get("page", 1), len(data), request.path, request.args, per_page_count=6)
    data_list = data[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('review_data.html', datas = data_list, html=html)


@app.route('/review_data_delete/<int:id>')
def rolled_steel_test_delete(id):
    sql = 'delete from review_data where 序号=' + str(id)
    db.insert_or_update_data(sql)
    return render_template("review_data.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
