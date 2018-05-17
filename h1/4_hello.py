#-*-coding:utf-8-*-
from flask import Flask
from flask_bootstrap import Bootstrap

from flask import render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return '<h1>Test Flasky</h1>'

# 响应flask-bootstrap模板
# @app.route('/user/<name>')
# def hello(name):
    # return render_template("4_1_user.html",name = name)


# 常见错误提示
# 404：找不到资源
@app.errorhandler(404)
def page_not_found(e):
    return render_template('4_2_404.html'), 404

# 服务器内部错误
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('4_3_500.html'), 500

#user页面重写
@app.route('/user/<name>')
def user(name):
    return render_template('4_2_userPlus.html', name = name) 






def main():
   app.run(debug = True)

if __name__ == '__main__':
    main()


