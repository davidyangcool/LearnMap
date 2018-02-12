from flask import  Flask,jsonify,request
app= Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return jsonify({'msg':'It works!'})


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)