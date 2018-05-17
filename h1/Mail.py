#-*-coding:utf-8-*-
from flask import Flask, render_template
import os
from flask_mail import Mail  # 引入邮箱模块
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy #引用数据库，需要安装MySQL-python
from flask import session, redirect,url_for # 引入重定向和用户会话
from flask import flash     #Flash消息
# 引入表单模块
from flask_wtf import Form
from wtforms import StringField, SubmitField    # 引入文本和提交按钮
from wtforms.validators import Required     # 引入校验
# from wtforms import PasswordField   # 引入密码输入框
from flask_moment import Moment # 本地化时间
from datetime import datetime   # 引入时间模块
from flask_script import Shell  # 引入集成的pythonShell
from flask_migrate import Migrate, MigrateCommand   # 引入迁移仓库

basedir = os.path.abspath(os.path.dirname(__file__))
# 返回一个文件在当前环境中的绝对路径，这里file 一参数

app = Flask(__name__)
mail = Mail(app)
manager = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY']  = r'\xa7\xdb\xfd\xcetp\xf2\x9df+\xe20\x92\x1f\x18\x90\xcb\x0b\xd8RY$3\x8b'
# 创建mysql数据库链接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345679@localhost:3306/h1'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True   # 设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)


# 自定义对象
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref = 'role',lazy = 'dynamic')
    #  backref 参数向 User 模型中添加一个 role 属性，从而定义反向关系

    def __repr__(self):
        return '<Role %r >' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True )
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 设置外键

    def __repr__(self):
        return '<User %r >' % self.username


# 定义表单
class NameForm(Form):
    name = StringField('what is your name?', validators= [Required()])
    # required：必要的，必须的
    submit = SubmitField('submit')




# 配置Flask-Mail使用goole邮箱
app.config['MAIL_SEVER'] = 'smtp.googlemail.com'#'smtp.qq.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_SSL'] = True   # 谷歌的安全协议：TLS qq和别的一些：SSL
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = "zzz1171284619@gmail.com"#os.environ.get('MAIL_USERNAEM')
app.config['MAIL_PASSWORD'] = "zcf.19970125"#os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
app.config['FLASKY_ADMIN'] ="1171284619@qq.com"#os.environ.get('FLASKY_ADMIN')#收件人
# mail.init_app(app)  # 应用配置


#发送邮件函数
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,\
                    sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)



# 在视图函数中操作数据库
# @app.route('/', methods = ['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username = form.name.data).first()
#         #查询过滤器在数据库中查找提交的名字
#         if user is None:
#             user = User(username = form.name.data)
#             db.session.add(user)
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('7_SQL.html',form = form,name = session.get('name'),\
#                             known = session.get('known', False), current_time = datetime.utcnow())



#发送邮件
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',\
                                        'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('Mail.html', form=form, name=session.get('name'),\
                            known=session.get('known', False), current_time = datetime.utcnow())


def main():
    manager.run()

if __name__ == '__main__':
    main()

