import json
import random
import RedisHelper
import datetime

# 헬퍼 클래스 호출
rh = RedisHelper.RedisHelper()

for i in range(50):
    # 예제 데이터
    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(days=1)
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    tomorrowDatetime = tomorrow.strftime('%Y-%m-%d %H:%M:%S')

    customer = {
        'id': random.randrange(0, 100000, 5),
        'name': '최은혁',
        'history': [
            {'date': nowDatetime, 'item': 'iPhone'},
            {'date': tomorrowDatetime, 'item': 'Monitor'},
        ]
    }
    jsonString = json.dumps(customer)
    # 푸시
    rh.lpush_data(jsonString)


for i in range(50):
    data = rh.rpop_data()
    if data is not None:
        customerData = json.loads(data)
        print(customerData)
    else:
        print("none")
