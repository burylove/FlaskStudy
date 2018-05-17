#-*-coding:utf-8-*-
from flask import Flask
from flask_bootstrap import Bootstrap   # 链接bootstrap模板
from flask_moment import Moment # 本地化时间
from datetime import datetime   # 引入时间模块


from flask import render_template   # 链接templates中的html

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# 渲染时间戳
@app.route('/')
def now_time():
    return render_template('5_1_nowTime.html',
                          current_time = datetime.utcnow())









def main():
    app.run(debug = True)

if __name__ == '__main__':
    main()