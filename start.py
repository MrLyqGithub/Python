# -*-coding:utf-8-*-

from flask import render_template
from flask import Flask
from flask import request, flash
from flask import make_response, redirect, session
import sqlite3

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/user_login', methods=['POST'])
def userlogin():
    user_name = request.form['user_name']
    password = request.form['user_password']

    # 查询语句
    sql = "select * from mes where username=?"

    # 查询是否存在该用户
    users = execute_query(sql, [user_name])

    # 判断是否存在该用户
    if users and len(users) == 1:

        # 从结果中获取第一条数据
        user = users[0]

        # 第一条数据中密码的下标位置
        pwd = user[2]

        # 判断密码数据库中的密码是否与表单的密码一致
        if password == pwd:

            # 允许登陆
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['password'] = user[2]

        # 密码错误
        else:
            return redirect('/error/password error')

    # 用户不存在
    else:
        return render_template('registe.html')

    # 登陆成功跳转页面
    return redirect('/get_session')


# 查询函数（查询语句，查询值）
def execute_query(sql, args=()):
    con = sqlite3.connect('mysql.db')
    curs = con.cursor()
    curs.execute(sql, args)
    datas = curs.fetchall()
    curs.close()
    con.close()
    return datas


@app.route('/user_registe', methods=['POST'])
def user_registe():
    user_name = request.form['user_name']
    user_password = request.form['user_password']

    sql_select = "select * from mes where username=?"
    result = execute_query(sql_select, [user_name])

    # 判断是否存在该用户
    if result and len(result) == 1:
        return redirect('/error/user is exist')

    else:
        sql_insert = "INSERT INTO mes (username,password) VALUES ('" + user_name + "','" + user_password + "')"
        execute_insert(sql_insert)

        session['username'] = request.form['user_name']
        session['password'] = request.form['user_password']

        return redirect('/get_session')

    # 插入数据（语句）


def execute_insert(sql):
    con = sqlite3.connect('mysql.db')
    curs = con.cursor()
    curs.execute(sql)
    curs.close()
    con.commit()
    con.close()


# 提交按钮后渲染模板
@app.route('/get_session')
def get_session():
    return render_template('user.html', session=session)


# 网页找不到
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# 
@app.route('/error/<error>')
def page_error(error):
    return render_template('404.html', error=error)


# @app.route('/count')
# def count():
#     user_name = request.form['user_name']
#     user_password = request.form['user_password']
#     query="select count(*) cnt from mes where username=?"
#     cnts = execute_query(query, [user_name])
#     cnt=0
#     if cnts and len(cnts)>0:
#         cnt=cnts[0][0]
#     if cnt > 0:
#         print cnt

@app.route('/db')
def result():
    user = []
    user_id = []
    con = sqlite3.connect('mysql.db')
    curs = con.cursor()
    sql = 'select * from mes'
    curs.execute(sql)
    datas = curs.fetchall()
    curs.close()
    con.close()
    for data in datas:
        user_id.append(data[0])
        user.append(data[1])
    print (user)
    return render_template('db.html', datas=user, datas_id=user_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
