from flask import Flask, Response, request, make_response, jsonify
import pymongo
from bson.objectid import ObjectId
import json
app = Flask(__name__)

mongo = pymongo.MongoClient("mongodb://ip-172-31-46-205.us-east-2.compute.internal:27017/")
db = mongo.User

# status code errors
@app.errorhandler(404)
def hadle_404(_error):
    """ reuturn a 404 status code"""
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def hadle_500(_error):
    """ reuturn a 404 status code"""
    return make_response(jsonify({'error': 'Internal server error'}), 500)


@app.route("/read", methods=["GET"])
def get_user():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(response= json.dumps(data), status=200, mimetype="application/json")

    except Exception as ex:
        print(ex)
        return Response(response= json.dumps({"message": "user not found"}), status=500, mimetype="application/json")

@app.route("/write", methods=["POST"])
def create_user():
    try:
        user= {"name":request.form["name"], "lastname":request.form["lastname"]}
        dbResponse = db.users.insert_one(user)
        return Response(response=json.dumps({"message": "user created", "id": f"{dbResponse.inserted_id}"}),status=200, mimetype="application/json")
    except Exception as ex:
        print("**********")
        print(ex)
        print("***********")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
