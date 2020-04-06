import db
from json import dumps
from flask import Flask, request


app = Flask(__name__)


@app.route("/api/get_url", methods=['GET'])
def get_url():
    response = {}
    try:
        code = request.args.get('code')

        if code is None:
            raise Exception('code not specified')

        url = db.get_url(code)

        if url is None:
            response['success'] = False
            response['message'] = 'code could not be found'
        else:
            response['success'] = True
            response['message'] = 'success'
            response['url'] = url

        return dumps(response)
    except Exception as e:
        print(e)
        response['success'] = False
        response['message'] = 'code not specified'

    return dumps(response)


if __name__ == "__main__":
    app.run()
