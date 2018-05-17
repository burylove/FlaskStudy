# -*- coding: UTF-8 -*-
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from flask import session, redirect,url_for # 引入重定向和用户会话
from flask import flash     #Flash消息

from flask_moment import Moment # 本地化时间
from datetime import datetime   # 引入时间模块

# 引入表单模块
from flask_wtf import Form
from wtforms import StringField, SubmitField    # 引入文本和提交按钮
from wtforms.validators import Required     # 引入校验
from wtforms import PasswordField   # 引入密码输入框

app = Flask(__name__)
bootstrap = Bootstrap(app)
# 夸站请求伪造保护，生成密钥
app.config['SECRET_KEY']  = r'\xa7\xdb\xfd\xcetp\xf2\x9df+\xe20\x92\x1f\x18\x90\xcb\x0b\xd8RY$3\x8b'

moment = Moment(app)

# 定义表单
class NameForm(Form):
    name = StringField('what is your name?', validators= [Required()])
    # required：必要的，必须的
    password = PasswordField('input your password:',validators = [Required()])
    submit = SubmitField('submit')

# 实现功能在注释中
# @app.route('/', methods = ['GET', 'POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         # name = form.name.data
#         # form.name.data = ''   #以上两句为没有重定向的返回表单写法

#         session['name'] = form.name.data
#         session['password'] = form.password.data    # 实现重定向和用户会话
#         return redirect(url_for('index'))   # url_for参数名与函数名相同

#     return render_template('6_1_wtf.html',form = form, name = session.get('name'), password = session.get('password'), current_time = datetime.utcnow())

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_password = session.get('password')

        if (old_name is not None and old_name !=form.name.data) and \
                (old_password is not None and old_password != form.password.data):
            flash('Looks like you have changed your name and password!')
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('index'))
        
    return render_template('6_1_wtf.html', form = form,name = session.get('name'),\
                            password = session.get('password'), current_time = datetime.utcnow())





def main():
    app.run(debug = True)

if __name__ == '__main__':
    main()    
