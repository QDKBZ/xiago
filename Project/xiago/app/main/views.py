from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from flask import request
from app.main import blue
from app.models import Brand, Commodity
from .forms import RegisterForm
from .. import models

@blue.route('/index/', methods=['GET', 'POST'])
def index():
    brands = Brand.query.limit(6)
    print(brands)
    return  render_template('index_2.html',brands=brands)

@blue.route('/hotel/<id>')
def hotel(id):
    brand = Brand.query.get(id)
    img = brand.img
    name = brand.title
    coms = Commodity.query.filter_by(co_name=name).limit(8)
    return  render_template('hotel.html',coms=coms,img=img)


@blue.route('/register/', methods=['GET', 'POST'])
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
        pass
        #return redirect(url_for('register_wtf'))
    return render_template('register.html')

#登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


#   {{ url_for('static',filename='') }}