# # from flask import Flask, request, jsonify
# # from flask_cors import CORS
# #
# # app = Flask(__name__)
# #
# # # 设置 CORS，允许从 http://localhost:8080 访问所有路由
# # CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
# #
# # @app.route('/process', methods=['POST'])
# # def process():
# #     data = request.json
# #     x_start = data.get('xStart')
# #     x_end = data.get('xEnd')
# #     y_start = data.get('yStart', None)  # 多点扫描的情况
# #     y_end = data.get('yEnd', None)
# #
# #     # 模拟一些数据处理
# #     result = {
# #         'xRange': x_end - x_start,
# #         'yRange': (y_end - y_start) if y_start is not None and y_end is not None else None
# #     }
# #
# #     # 返回处理结果，包含 CORS 头
# #     response = jsonify(result)
# #     response.headers.add("Access-Control-Allow-Origin", "http://localhost:8080")
# #     return response
# #
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
# # src/backend/app.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
#
# app = Flask(__name__)
# CORS(app)  # 允许跨域请求
#
# @app.route('/process', methods=['POST'])
# def process_data():
#     data = request.json
#     x_start = data.get("xStart")
#     x_end = data.get("xEnd")
#
#     # 调用 Python 脚本进行数据处理
#     result = run_python_script(x_start, x_end)
#
#     return jsonify({"result": result})
#
# def run_python_script(x_start, x_end):
#     return f"Processed: x_start={x_start}, x_end={x_end}"
#
#
# # app.route('/api/two', methods=['POST'])
# # def process_multi_scan():
# #     data = request.json
# #     x_start = data.get("xStart")
# #     x_end = data.get("xEnd")
# #     y_start = data.get("yStart")
# #     y_end = data.get("yEnd")
# #
# #     # 调用 Python 脚本进行数据处理
# #     result = run_python_script(x_start, x_end, y_start, y_end)
# #
# #     return jsonify({"result": result})
# #
# # def run_python_script(x_start, x_end, y_start, y_end):
# #     return f"Processed: x_start={x_start}, x_end={x_end}, y_start={y_start}, y_end={y_end}"
# if __name__ == '__main__':
#     app.run(debug=True)



# src/backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # 允许所有来源的跨域请求

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json
    x_start = data.get("xStart")
    x_end = data.get("xEnd")

    # 调用 Python 脚本进行数据处理
    result = run_python_script(x_start, x_end)

    return jsonify({"result": result})

def run_python_script(x_start, x_end):
    return f"Processed: x_start={x_start}, x_end={x_end}"

@app.route('/api/two', methods=['POST'])
def process_multi_scan():
    data = request.json
    x_start = data.get("xStart")
    x_end = data.get("xEnd")
    y_start = data.get("yStart")
    y_end = data.get("yEnd")
    # 调用 Python 脚本进行数据处理
    result = two(x_start, x_end, y_start, y_end)

    return jsonify({"result": result})

def two(x_start, x_end, y_start, y_end):
    # 这里可以放你的数据处理逻辑，下面是一个简单的示例
    return f"Processed: x_start={x_start}, x_end={x_end}, y_start={y_start}, y_end={y_end}"

if __name__ == '__main__':
    app.run(debug=True)