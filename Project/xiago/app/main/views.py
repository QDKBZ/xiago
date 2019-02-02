from datetime import datetime
from flask import render_template, session, redirect, url_for, flash
from flask import request
from flask_login import login_user, logout_user, login_required
from app.email import send_email
from app.main import blue
<<<<<<< HEAD
from .forms import RegistrationForm, LoginForm
=======
from app.models import Brand, Commodity
from .forms import RegisterForm
>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1
from .. import models

@blue.route('/index/', methods=['GET', 'POST'])
def index():
<<<<<<< HEAD
    return render_template('index_2.html')

@blue.route('/hotel/', methods=['GET', 'POST'])
def hotel():
    return render_template('hotel_detail.html')
=======
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

>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1

@blue.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = models.User(email=form.email.data,
                    user_name=form.user_name.data,
                    user_password=form.password.data,
                           user_mobile=form.tel.data)
        models.db.session.add(user)
        models.db.session.commit()
        # token = user.generate_confirmation_token()
        # send_email(user.email, 'Confirm Your Account',
        #            'auth/email/confirm', user=user, token=token)
        # flash('确认信息已经发邮件给你了')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


#登录
@blue.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('mian.index')
                return redirect(next)
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@blue.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已经注销')
    return redirect(url_for('index'))

#   {{ url_for('static',filename='') }}