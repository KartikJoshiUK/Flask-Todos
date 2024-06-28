from flask import Blueprint, request, url_for, make_response, jsonify

indexRouter = Blueprint("/", __name__)

@indexRouter.route("/")
def index():
    return "Hello World!!"

@indexRouter.route("/dynamic/<string:name>")
def dynamic(name):
    queries = request.args
    return f"Hello {name} searched for {queries.get('search')}!!"

@indexRouter.route('/urlfor/<username>')
def urlfor(username):
    user_url = url_for('/.dynamic', name=username, search='search', pageNumber=1, _external=True)
    return f"Link to user profile: <a href='{user_url}'>{username}</a>"

@indexRouter.route('/formdata', methods=['POST'])
def formdata():
    name = request.form.get('name')
    return f"Form submitted by {name}"

@indexRouter.route('/jsondata', methods=['POST'])
def jsondata():
    name = request.get_json().get('name')
    return f"Form submitted by {name}"


@indexRouter.route('/custom_response')
def custom_response():
    response = make_response("Custom Response", 205)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Custom-Header'] = 'CustomValue'
    return response

@indexRouter.route('/json_response')
def json_response():
    data = {'key': 'value'}
    return jsonify(data), 201

@indexRouter.route('/method', methods=['GET','POST','PUT',"DELETE", "PATCH"])
def method():
    return jsonify({'method': request.method}), 200