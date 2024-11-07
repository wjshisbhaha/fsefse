from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json
    # 假设返回一个处理后的结果
    result = {"result": "处理成功"}
    response = make_response(jsonify(result))
    response.headers.add("Access-Control-Allow-Origin", "*")  # 允许所有域访问
    return response

if __name__ == '__main__':
    app.run(port=5000)

