from datetime import datetime, timedelta

import pymongo
from flask_restplus import Resource, fields, reqparse

from server.apis.models import response_model, timeLine_filters_detail_model, timeline_good_model
from server.apis.utils import get_start_limit_dates, get_start_limit_times
from server.common.constants import ERROR_REASON, SUCCESS_REASON
from server.databases.mongodb import meta_collection, timeline_goods_collection


def create_v1_timeline(api):
    timeline_ns = api.namespace('timeline', description='Buzzni-test v1 api for timeline')

    @timeline_ns.route('/filters')
    class TimelineGoodsCategories(Resource):
        # RESPONSE: response models
        timeLine_filters_detail_model = api.clone('TimelineFiltersDetailModel', timeLine_filters_detail_model)
        timeline_filters_model = api.clone('TimelineFiltersModel', response_model, {
            'timeline_filters': fields.Nested(timeLine_filters_detail_model)
        })

        @timeline_ns.doc(
            description='Timeline 필터링에 사용할 수 있는 메타 데이터값들을 반환합니다.'
        )
        @timeline_ns.marshal_with(timeline_filters_model)
        def get(self):
            try:
                timeline_filters = meta_collection.find_one({'timeline_filters': {'$exists': 1}},
                                                            {'_id': -1, 'timeline_filters': 1})
                if not timeline_filters:
                    return dict(success=False,
                                reason=ERROR_REASON['ResultNotFound'],
                                timeline_filters=dict(dates=[], mall_names=[], cate1s=[])), 204, {}
                timeline_filters = timeline_filters['timeline_filters']

                return dict(success=True,
                            reason=SUCCESS_REASON['SUCCESS'],
                            timeline_filters=dict(dates=timeline_filters['dates'],
                                                  mall_names=timeline_filters['mall_names'],
                                                  cate1s=timeline_filters['cate1s'])), 200, {}
            except Exception as e:
                print(e)
                return dict(success=False,
                            reason=ERROR_REASON['InternalServerError'],
                            timeline_filters=dict(dates=[], mall_names=[], cate1s=[])), 500, {}

    @timeline_ns.route('/goods')
    class TimelineGoods(Resource):
        parser = reqparse.RequestParser()

        # REQUEST: request args
        # required
        parser.add_argument('date', required=True, type=str, location='args', default='20171125',
                            help='날짜 ex) YYYYMMDD')
        parser.add_argument('start_time', required=True, type=str, location='args', default='1300',
                            help='시간 ex) 100(=1:00) / 1300(=13:00)')
        parser.add_argument('scroll_direction', required=True, type=str, location='args', default='down',
                            help='시간 ex) init / up / down')
        # optional
        parser.add_argument('mall_names', type=str, location='args',
                            help='쇼핑사 ex) mall_name|mall_name|mall_name')
        parser.add_argument('cate1s', type=str, location='args',
                            help='카테고리 1 ex) category|category|category')

        # RESPONSE: response models
        timeline_good_model = api.clone('TimelineGoodModel', timeline_good_model)
        timeline_goods_model = api.clone('TimelineGoodsModel', response_model, {
            'timeline_goods': fields.List(fields.Nested(timeline_good_model))
        })

        @timeline_ns.doc(
            description='필터링 값등을 사용하여 타임라인 상품 리스트를 조회할 수 있습니다.'
        )
        @timeline_ns.expect(parser)
        @timeline_ns.marshal_with(timeline_goods_model)
        def get(self):
            args = self.parser.parse_args()
            scroll_direction = args.get('scroll_direction', 'down')
            date = args.get('date')
            start_time = args.get('start_time')

            mall_names = args.get('mall_names', None)
            cate1s = args.get('cate1s', None)
            try:
                start_time_hour = start_time[:-2]
                start_time_minute = start_time[2:]

                query_filter = {}

                if mall_names and mall_names != '':
                    mall_names = mall_names.split('|')
                    query_filter.update({'mall_name': {'$in': mall_names}})

                if cate1s and cate1s != '':
                    cate1s = cate1s.split('|')
                    query_filter.update({'cate1': {'$in': cate1s}})

                if scroll_direction == 'down':
                    start_datetime = datetime.strptime(date, '%Y%m%d') \
                        .replace(hour=int(start_time_hour),
                                 minute=int(start_time_minute))
                    limit_datetime = start_datetime + timedelta(hours=4)
                elif scroll_direction == 'up':
                    limit_datetime = datetime.strptime(date, '%Y%m%d') \
                        .replace(hour=int(start_time_hour),
                                 minute=int(start_time_minute))
                    start_datetime = limit_datetime - timedelta(hours=4)
                else:
                    # when scroll_direction == 'init',
                    # loading goods from time 4 hour before and to time 4 hours later
                    start_datetime = datetime.strptime(date, '%Y%m%d') \
                        .replace(hour=int(start_time_hour),
                                 minute=int(start_time_minute))
                    start_datetime = start_datetime - timedelta(hours=4)
                    limit_datetime = start_datetime + timedelta(hours=12)

                start_date, end_date = get_start_limit_dates(start_datetime, limit_datetime)
                start_time, limit_time = get_start_limit_times(start_datetime, limit_datetime)

                and_or_filter = '$and' if start_date == end_date else '$or'

                query_filter.update({
                    and_or_filter: [
                        {
                            'date': int(start_date),
                            'start_time': {
                                '$gte': int(start_time)
                            }
                        },
                        {
                            'date': int(end_date),
                            'start_time': {
                                '$lt': int(limit_time)
                            }

                        }
                    ],
                    'org_price': {'$ne': 0},
                    'price': {'$ne': 0}
                })
                timeline_goods = list(timeline_goods_collection.find(query_filter).sort('date', pymongo.ASCENDING))
                if not timeline_goods:
                    return dict(success=False,
                                reason=ERROR_REASON['ResultNotFound'],
                                timeline_goods=[]), 204, {}

                return dict(success=True,
                            reason=SUCCESS_REASON['SUCCESS'],
                            timeline_goods=timeline_goods), 200, dict()
            except Exception as e:
                print(e)
                return dict(success=False,
                            reason=ERROR_REASON['InternalServerError'],
                            timeline_goods=[]), 500, dict()
