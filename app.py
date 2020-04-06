import db
import validation
import coding
from json import dumps
from flask import Flask, request


app = Flask(__name__)


@app.route("/api/get_url", methods=['GET'])
def get_url():
    response = {}

    code = request.args.get('code')
    url = db.get_url(code)

    if url is None:
        response['success'] = False
        response['message'] = 'code could not be found'
        return dumps(response)

    response['success'] = True
    response['message'] = 'success'
    response['url'] = url

    return dumps(response)


@app.route("/api/shorten_link", methods=['GET'])
def shorten_link():
    response = {}

    url = request.args.get('url')
    code = coding.try_encode(url)

    if code is None:
        response['success'] = False
        response['message'] = 'sent link is not a valid URL'
        return dumps(response)

    result = db.add_url(code, url)

    if result is None:
        response['success'] = False
        response['message'] = 'could not add URL to database'

    response['success'] = True
    response['message'] = 'success'
    response['code'] = code

    return dumps(response)


if __name__ == "__main__":
    app.run()
