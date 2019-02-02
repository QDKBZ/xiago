from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from flask import request
from . import main
from .forms import RegisterForm
from .. import models


@main.route('/index/')
def index():
    return render_template('index-2.html')


@main.route('/register/', methods=['GET', 'POST'])
def register_wtf():
    # 表单类实例化，渲染模板--在页面上显示表单
    form = RegisterForm()
    # 判断提交方式是否是post，是，说明用户提交的表单
    if request.method == 'POST':
        # 对表单进行验证
        if form.validate_on_submit():
            # 验证通过执行以下代码
            username = request.form.get('username')
            password = request.form.get('password')
            password2 = request.form.get('password2')
            tel = request.form.get('tel')
            sex = request.form.get('sex')
            birthday = request.form.get('birthday')
            email = request.form.get('email')

            print(username, password, password2, tel, sex, birthday, email)
            if password != password2:
                flash("两次密码输入不一致")
            return "验证通过"
        else:
            # 消息闪现，渲染模板
            flash('参数错误')
    else:
        return redirect(url_for('register_wtf'), locals())
    return redirect(render_template('register.html', form=form), locals(), 404)

@main.route('/login/')
def login():
    return render_template('login.html')

