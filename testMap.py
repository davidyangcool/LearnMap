from flask import Flask,render_template,jsonify,request

app=Flask(__name__)
locations=[[115.7987,32.892284],[115.824965,32.887996],[115.824627,32.878211]]

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
    return jsonify({'msg':'谢谢，位置数据提交成功'})

@app.route('/heatmap',methods=['GET','POST'])
def heatmap():
    return render_template('heatMap.html')
@app.route('/ipcamera')
def ipcamera():
    return render_template('window_info.html')
@app.route('/locations',methods=['GET'])
def getlocations():
    return jsonify({'locations':locations})
if __name__=="__main__":
    app.run(host='0.0.0.0')