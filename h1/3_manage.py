#-*-coding:utf-8-*-
from flask import Flask
from flask import render_template   # 导入模板

from flask_script import Manager # flask-script扩展



app = Flask(__name__)
manager = Manager(app)

# 根目录访问
# @app.route('/')
# def index():
#     return render_template('1_index.html')

# @app.route('/user/<name>')
# def user(name):
#     return render_template('1_user.html', name = name)

# 带多参访问
# @app.route('/mydict/<mydict>/mylist/<mylist>/')
# def fun(mydict, mylist):
#     return render_template('2_bianLiang.html', mydict = mydict,mylist = mylist )

#控制结构：条件控制
# @app.route('/user/<name>')
# def user(name):
#     return render_template('3_user.html', user = name)


#模板的继承
@app.route('/')
def ext():
    return render_template('4_ext.html')









def main():
    manager.run()

if __name__ == '__main__':
    main()


