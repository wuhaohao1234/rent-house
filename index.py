import requests
import json

url = 'https://dbzz.house/api'

city = '北京'

time = '7'

size = '10'

requestStr = url + '/search?city=' + city + '&keyword=&recent_days=' + time + '&publisher_role=&unique_flag=true&page_size=' + size + '&current_page=1'

res = requests.get(requestStr)

data = json.loads(res.text)

print(data)

fo = open(city + '租房.json', 'w')

fo.write(res.text)

fo.close()

# 'https://www.douban.com/group/topic/' + postId