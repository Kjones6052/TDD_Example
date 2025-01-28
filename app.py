from flask import Flask, request, jsonify

app = Flask(__name__)

# create /sum endpoint route to get sum of 2 numbers

#  1st run at /sum endpoint route code (commented out but retained for example notes)
# @app.route('/sum', methods=['POST'])
# def sum():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = num1 + num2
#     return jsonify({'result': result}), 200

# 2nd run at /sum endpoint route code (refactor stage)
@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    try:
        return jsonify({'result': data['num1'] + data['num2']}), 200
    except KeyError:
        return jsonify({'message': 'Missing properties num1 and/or num2'}), 400
    
# create /subtract endpoint route to get difference of 2 numbers

#  1st run at /subtract endpoint route code (commented out but retained for example notes)
# @app.route('/subtract', methods=['POST'])
# def subtract():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = num1 - num2
#     return jsonify({'result': result}), 200

# 2nd run at /subtract endpoint route code (refactor stage)
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    try:
        return jsonify({'result': data['num1'] - data['num2']}), 200
    except KeyError:
        return jsonify({'message': 'Missing properties num1 and/or num2'}), 400
    
# create /multiply endpoint route to get product of 2 numbers

#  1st run at /multiply endpoint route code (commented out but retained for example notes)
# @app.route('/multiply', methods=['POST'])
# def multiply():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = num1 * num2
#     return jsonify({'result': result}), 200

# 2nd run at /multiply endpoint route code (refactor stage)
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    try:
        return jsonify({'result': data['num1'] * data['num2']}), 200
    except KeyError:
        return jsonify({'message': 'Missing properties num1 and/or num2'}), 400
    
# create /divide endpoint route to get quotient of 2 numbers

#  1st run at /divide endpoint route code (commented out but retained for example notes)
# @app.route('/divide', methods=['POST'])
# def divide():
#     data = request.get_json()
#     num1 = data['num1']
#     num2 = data['num2']
#     result = num1 / num2
#     return jsonify({'result': result}), 200

# 2nd run at /divide endpoint route code (refactor stage)
@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    try:
        return jsonify({'result': data['num1'] / data['num2']}), 200
    except KeyError:
        return jsonify({'message': 'Missing properties num1 and/or num2'}), 400

if __name__ == '__main__':
    app.run(debug=True)