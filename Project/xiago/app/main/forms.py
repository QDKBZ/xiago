from flask_wtf import FlaskForm, validators
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import DataRequired, EqualTo


# 自定义注册表单， 继承FlaskForm类
class RegisterForm(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired('请输入用户名')], render_kw={'placeholder': '请输入用户名'})
    password = PasswordField("密码：", validators=[DataRequired('请输入密码')], render_kw={'placeholder': '请输入密码'})
    password2 = PasswordField("确认密码：", validators=[DataRequired('请再次输入密码'), EqualTo(password, '两次密码输入不一致')], render_kw={'placeholder': '请确认密码'})
    tel = StringField("电话：", validators=[DataRequired('请输入手机号')])
    sex = BooleanField("性别", {'男': 1, '女': 0})
    birthday = DateField("生日：")
    email = StringField("邮箱：")

    submit = SubmitField("注册")