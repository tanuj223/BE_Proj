from flask import request
from flask.json import jsonify
from flask_cors import CORS
from flask import Blueprint
from models.notes import extract_summary
from models.recommend import rec

api = Blueprint(
    'api', 'api', url_prefix='/')
CORS(api)


@api.route("/notes", methods=['POST'])
def notes():
    request_data = request.get_json()
    chapter = request_data["chapter"]
    return jsonify(extract_summary(chapter, 3, True))


@api.route("/recommend", methods=['POST'])
def recommend():
    request_data = request.get_json()
    chapter = request_data["chapter"]
    return jsonify(rec(chapter, max_ngram_size=1, deduplication_threshold=0.5, numOfKeywords=5))
