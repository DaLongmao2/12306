# coding = utf-8
import time

from flask import Flask, render_template, request, flash
from app.query_request import query
from app.get_stations import *
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST', 'GET'])
def index():
    localtime = time.localtime()
    station = eval(read2())
    # 当前时间 年月日
    localtime_ = '{}-{}-{}'.format(localtime[0], localtime[1], localtime[2])
    if request.method == 'POST':
        chu = request.form.get('chu')
        dao = request.form.get('dao')
        time_ = request.form.get('time')
        type_stu = request.form.get('type_stu')


        # 获取表单数据
        c = station.get('{}'.format(chu))
        d = station.get('{}'.format(dao))
        if c is None and d is None:
            flash('输入的城市不存在')


        print(d, c, time_)
        #　票种转换为　代码
        if type_stu == "普通票":
            type_stu1 = "ADULT"
        elif type_stu == "学生票":
            type_stu1 = "0X00"

        print(time_, c, d, type_stu1)

        #　出发地(c) 到达地点(d) 如果都存在
        if c and d:
            # 则传入 query（出发地点， 到达地点， 票种） 进行爬去获取
            data = query(time_, c, d, type_stu1)
            if data:
                return render_template('index.html',
                                       data=data, chu=chu, dao=dao, localtime_=localtime_, type_stu=type_stu, station1=station.keys())
        # flash('信息有误...')
        else:
            return 'ERROR'
    return render_template('index.html', localtime_=localtime_, station1=station.keys())


if __name__ == '__main__':
    app.run(port=5050)
