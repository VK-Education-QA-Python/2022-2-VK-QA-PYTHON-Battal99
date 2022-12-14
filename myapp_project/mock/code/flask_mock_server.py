from flask import Flask, jsonify, request
from conf import MOCK_HOST, MOCK_PORT

app = Flask(__name__)

VK_DATA = {'BATTAL': 'id266'}


@app.route("/vk_id/<username>", methods=['GET'])
def get_id(username):
    if username in VK_DATA:
        return jsonify({"vk_id": str(VK_DATA[username])}), 200
    else:
        return jsonify('Not Found'), 404


@app.route("/vk_id/utils/create/<username>", methods=['POST'])
def create(username):
    id_user = request.get_json()['id']
    VK_DATA[username] = str(id_user)
    return jsonify('OK'), 201


@app.route("/vk_id/utils/delete/<username>", methods=['DELETE'])
def delete(username):
    if username in VK_DATA:
        del VK_DATA[username]
        return jsonify('OK'), 204
    else:
        return jsonify('User does not exist'), 404


if __name__ == "__main__":
    app.run(host=MOCK_HOST, port=MOCK_PORT)
