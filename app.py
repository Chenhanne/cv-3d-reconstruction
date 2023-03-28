from flask import Flask, render_template, request, jsonify
from neo_db.query_graph import query, get_KGQA_answer, get_answer_profile
from KGQA.ltp import get_target_array

app = Flask(__name__)
# 装饰器，路由分发，根据url找到视图函数


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])  # index 界面
def index(name=None):
    return render_template('index.html', name=name)


@app.route('/search', methods=['GET', 'POST'])  # search 按人名搜索界面
def search():
    return render_template('search.html')


@app.route('/KGQA', methods=['GET', 'POST'])  # 问答界面
def KGQA():
    return render_template('KGQA.html')


@app.route('/get_profile', methods=['GET', 'POST'])  # KGQA 界面 跳转至 /get_profile 时执行，
def get_profile():
    name = request.args.get('character_name')
    json_data = get_answer_profile(name)  # 是 query_graph 内定义的方法
    return jsonify(json_data)


@app.route('/KGQA_answer', methods=['GET', 'POST'])
def KGQA_answer():
    question = request.args.get('name')  # 获得查询的问题
    # get_target_array 是ltp模型的方法； get_KGQA_answer 是 query_graph 内定义的方法；
    json_data = get_KGQA_answer(get_target_array(str(question)))
    return jsonify(json_data)


@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data = query(str(name))
    return jsonify(json_data)


@app.route('/get_all_relation', methods=['GET', 'POST'])
def get_all_relation():
    return render_template('all_relation.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
