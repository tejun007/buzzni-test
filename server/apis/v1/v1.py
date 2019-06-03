from flask import Blueprint
from flask_restplus import Api

from server.apis.v1.v1_timeline import create_v1_timeline

v1 = Blueprint('api_v1', __name__)
v1_api = Api(
    v1,
    version='1.0',
    title='Buzzni-test: API',
    description='버즈니 과제를 위한 API DOC 페이지 입니다.'
)


def create_v1_api():
    create_v1_timeline(v1_api)
