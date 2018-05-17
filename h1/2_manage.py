#-*-coding:utf-8-*-

from flask import Flask
from flask import make_response # 创建响应对象
from flask import redirect  # 重定向响应
from flask import abort # 特殊响应：错误处理


from flask_script import Manager # flask-script扩展


app = Flask(__name__)
manager = Manager(app)    # flask-script扩展


# 空白请求
# @app.route('/')
# def index():
#     return '<h1>Hello</h1>'

#cookie
# @app.route('/')
# def index():
#     response = make_response('<h1>这是一个带有cokie的请求</h1>')
#     response.set_cookie('answer', 42)
#     return response

# 重定向响应
# @app.route('/')
# def index():
#     return redirect('http://www.baidu.com')

#特殊响应：处理错误
# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello,%s </h1>' % user.name

#Flask扩展
#Flask-Script

def main():
    #app.run(debug = True)
    manager.run()    #flask-script扩展启动

if __name__ == '__main__':
    main()