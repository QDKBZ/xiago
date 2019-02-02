from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Permission:
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

# 用户表
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True, )
    user_password = db.Column(db.String(32), nullable=False)
    user_mobile = db.Column(db.String(11), nullable=False)
    head_portrait = db.Column(db.String(30))
    sex = db.Column(db.Boolean, default=0)
    birthday = db.Column(db.Time)
    email = db.Column(db.String(200), nullable=True)
    if_online = db.Column(db.Boolean, default=0)
    last_login_ip = db.Column(db.String(200))
    last_login_time = db.Column(db.Time)
    user_class_id = db.Column(db.Integer, db.ForeignKey('user_class.uc_id'))
<<<<<<< HEAD
    address = db.relationship("Order_form", backref="user")
    address1 = db.relationship("Estimate", backref="user")
    address2 = db.relationship("Shopping_car", backref="user")
    address3 = db.relationship("Take_information", backref="user")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.user_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.user_password, password)
=======
    # address = db.relationship("Order_form",backref="User")
    # address1 = db.relationship("Estimate", backref="User")
    # address2 = db.relationship("Shopping_car", backref="User")
    # address3 = db.relationship("Take_information", backref="User")
>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1

    def __repr__(self):
        return self.user_name
# 等级表
class User_class(db.Model):
    __tablename__ = "user_class"
    uc_id = db.Column(db.Integer, primary_key=True)
    uc_svip = db.Column(db.Integer)
    uc_vip = db.Column(db.Integer)
    uc_nvip = db.Column(db.Integer)
    # address1 = db.relationship("User", backref="user_class")
    # address2 = db.relationship("Impower", backref="user_class")

# 公司表
class Company_information(db.Model):
    __tablename__ = "company_information"
    cpy_id = db.Column(db.Integer, primary_key=True)
    cpy_num = db.Column(db.Integer, nullable=False)
    cpy_name = db.Column(db.String(200), nullable=False)
<<<<<<< HEAD
    address = db.relationship("Department_information", backref="company_information")
    address1 = db.relationship("Staff_information", backref="company_information")
=======
    # address = db.relationship("department_information", backref="company_information")
    # address1 = db.relationship("staff_information", backref="company_information")
>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1


# 部门表
class Department_information(db.Model):
    __tablename__ = "department_information"
    dt_id = db.Column(db.Integer, primary_key=True)
    dt_num = db.Column(db.Integer, nullable=False)
    dt_name = db.Column(db.String(200), nullable=False)
    dt_cpy_id = db.Column(db.Integer, db.ForeignKey('company_information.cpy_id'))
<<<<<<< HEAD
    address1 = db.relationship("Staff_information", backref="department_information")
=======
    # address1 = db.relationship("staff_information", backref="Department_information")
>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1


# 员工表
class Staff_information(db.Model):
    __tablename__ = "staff_information"
    st_id = db.Column(db.Integer, primary_key=True)
    st_num = db.Column(db.Integer, nullable=False)
    st_name = db.Column(db.String(200), nullable=False)
    st_position = db.Column(db.String(200), nullable=False)
    st_cpy_id = db.Column(db.Integer, db.ForeignKey('company_information.cpy_id'))
    st_dt_id = db.Column(db.Integer, db.ForeignKey('department_information.dt_id'))



#权限表
class Impower(db.Model):
    __tablename__ = "impower"
    im_id = db.Column(db.Integer, primary_key=True)
    im_num = db.Column(db.Integer, nullable=False)
    im_information = db.Column(db.String(500), nullable=False)
    im_class_id = db.Column(db.Integer, db.ForeignKey('user_class.uc_id'))



# 商品表
class Commodity(db.Model):
    __tablename__ = "commodity"
    co_id = db.Column(db.Integer, primary_key=True)
    co_name = db.Column(db.String(200), nullable=False)
    co_new_price = db.Column(db.Float(50), nullable=False)
    co_old_price = db.Column(db.Float(50), nullable=False)
    co_img = db.Column(db.String(200), nullable=False)
    co_information = db.Column(db.String(500), nullable=False)
    # address1 = db.relationship("Estimate", backref="commodity")
    # address2 = db.relationship("Order_form", backref="commodity", uselist=False)
    # address3 = db.relationship("Shopping_car", backref="commodity", uselist=False)
    # address4 = db.relationship("Back_to_buy", backref="commodity", uselist=False)


class Brand(db.Model):
    __tablename__ = "brand"
    b_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    miaoshu = db.Column(db.String(200), nullable=False)
# 评价表
class Estimate(db.Model):
    __tablename__ = "estimate"
    est_id = db.Column(db.Integer, primary_key=True)
    est_text = db.Column(db.Text, nullable= False)
    est_img = db.Column(db.String(200), nullable=True)
    est_class = db.Column(db.Integer, nullable=False)
    est_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    est_co_id = db.Column(db.Integer, db.ForeignKey('commodity.co_id'))



# 订单表
class Order_form(db.Model):
    __tablename__ = "order_form"
    of_id = db.Column(db.Integer, primary_key=True)
    of_co_num = db.Column(db.Integer, nullable=False)
    of_co_infor = db.Column(db.Integer, db.ForeignKey('commodity.co_id'))
    of_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    of_ta_id = db.Column(db.Integer, db.ForeignKey('take_information.ta_id'))



# 购物车
class Shopping_car(db.Model):
    __tablename__ = "shopping"
    s_car_id = db.Column(db.Integer, primary_key=True)
    of_co_name = db.Column(db.Integer, nullable=False)
    s_car_infor_id = db.Column(db.Integer, db.ForeignKey('commodity.co_id'))
    s_car_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))




# 退购表
class Back_to_buy(db.Model):
    __tablename__ = "back_to_buy"
    btb_id = db.Column(db.Integer, primary_key=True)
    btb_text = db.Column(db.Text, nullable=False)
    btb_co_infor_id = db.Column(db.Integer, db.ForeignKey('commodity.co_id'))



# 收货表
class Take_information(db.Model):
    __tablename__ = "take_information"
    ta_id = db.Column(db.Integer, primary_key=True)
    ta_name = db.Column(db.String(50), nullable=False)
    ta_address = db.Column(db.String(200), nullable=False)
    ta_tel = db.Column(db.String(11), nullable=False)
    ta_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
<<<<<<< HEAD
    address1 = db.relationship("Order_form", backref="take_information")
=======
    # address1 = db.relationship("order_form", backref="take_information")
>>>>>>> 946c9d86f2295bab6cadfbbb8cd06b0b4fa070a1
