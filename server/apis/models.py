from flask_restplus import Model, fields


###################################################
# COMMON models
###################################################
response_model = Model('ResponseModel', {
    'success': fields.Boolean(description='응답되는 값이 성공적인 결과인지 여부'),
    'reason': fields.String(description='응답되는 값의 성공 여부에 대한 설명')
})


###################################################
# TIMELINE models
###################################################
timeLine_filters_detail_model = Model('TimelineFiltersDetailModel', {
    'dates': fields.List(fields.String),
    'mall_names': fields.List(fields.String),
    'cate1s': fields.List(fields.String)
})

timeline_good_model = Model('TimelineGoodModel', {
    '_id': fields.String,
    'mall_name': fields.String,
    'name': fields.String,
    'img': fields.String,
    'url': fields.String,
    'cate1': fields.String,
    'date': fields.String,
    'start_time': fields.String,
    'end_time': fields.String,
    'org_price': fields.Integer,
    'price': fields.Integer,
})
