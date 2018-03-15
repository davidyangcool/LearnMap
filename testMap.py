from flask import Flask,render_template,jsonify,request
import os
app = Flask(__name__, static_url_path='')

#路径需要动态配置
app.config['UPLOAD_FOLDER'] = '/Users/david/Documents/code/FunanPower/static/uploadimages/'
locations=[[115.7987,32.892284],[115.824965,32.887996],[115.824627,32.878211]]
print(os.getcwd())# 获取当前工作目录
@app.route('/',methods=['GET','POST'])
def showtrace():
    return render_template('map.html',locations=locations)

@app.route('/trace',methods=['POST'])
def trace():
    lat=request.form.get('lat')
    lgt=request.form.get('lgt')
    #point={'lat':float(lat),'lgt':float(lgt)}
    point=[float(lgt),float(lat)]
    locations.append(point)
    print(locations)
    print(request.form.get('username'))
    print(request.form.get('name'))
    return jsonify({'msg':'谢谢，位置数据提交成功'})

@app.route('/heatmap',methods=['GET','POST'])
def heatmap():
    return render_template('heatMap.html')
@app.route('/locations',methods=['GET'])
def getlocations():
    return jsonify({'locations':locations})

@app.route('/temp',methods=['GET'])
def temp():
    return app.send_static_file('temp.html')


@app.route('/test', methods=['GET'])
def test():
    return app.send_static_file('test.html')



#考勤打卡数据接收处理
@app.route('/signUp', methods=['POST'])
def signUp():
    print(request.form.get('code'))# 
    print(request.form.get('location'))
    return jsonify({"result": 1})# 返回 1 数据完整成功

#处理外出的函数
@app.route('/go_out', methods=['POST'])
def go_out():
    print(request.form.get('username'))
    print(request.form.get('name'))
    print(request.form.get('start_date'))
    print(request.form.get('end_date'))
    print(request.form.get('lenth_of_time'))
    print(request.form.get('reason'))
    return jsonify({"result": 1})  # 返回 1 数据完整成功


#处理请假函数的函数
@app.route('/askForLeave', methods=['POST'])
def askForLeave():
    print(request.form.get('username'))
    print(request.form.get('name'))
    print(request.form.get('type'))
    print(request.form.get('start_date'))
    print(request.form.get('end_date'))
    print(request.form.get('length_of_time'))
    print(request.form.get('reason'))
    return jsonify({"result": 1})  # 返回 1 数据完整成功

#处理日报函数
@app.route('/daily',methods=['POST'])
def daily():
    # 处理逻辑在此
    print(request.form.get('done'))
    print(request.form.get('todo'))
    print(request.form.get('need_help'))
    print(request.form.get('ps'))
    #获取第一张图片 
    file=request.files['images0']
    print(len(request.files))
    print(file.filename)
    print(file.content_type)
    #把照片存到图片上传目录
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
    return jsonify({'ret': 0, 'desc': 'Success'})

#处理月度报表函数
@app.route('/monthly', methods=['POST'])
def monthly():
    # 处理逻辑在此
    print(request.form.get('done'))
    print(request.form.get('todo'))
    print(request.form.get('need_help'))
    print(request.form.get('ps'))
    #获取第一张图片
    file = request.files['images0']
    print(len(request.files))
    print(file.filename)
    print(file.content_type)
    #把照片存到图片上传目录
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return jsonify({'ret': 0, 'desc': 'Success'})

@app.route('/access',methods=['POST'])
def access():
    print(request.form.get('custom'))
    print(request.form.get('type'))
    print(request.form.get('thing'))
    print(request.form.get('result'))
    print(request.form.get('ps'))
    #获取第一张图片
    file = request.files['images0']
    print(len(request.files))
    print(file.filename)
    print(file.content_type)
    #把照片存到图片上传目录
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return jsonify({'ret': 0, 'desc': 'Success'})
#处理注册数据
@app.route('/reg', methods=['POST'])
def reg():
    print(request.form.get('name'))
    print(request.form.get('username'))
    print(request.form.get('password'))
    print(request.form.get('dep'))
    return jsonify({"result": 1})
#处理登录
@app.route('/login',methods=['POST'])
def login():
    print(request.form.get('username'))
    print(request.form.get('password'))
    return jsonify({"result":1})
if __name__=="__main__":
    app.run(host='0.0.0.0')
