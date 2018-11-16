import psycopg2
import flickrapi
import requests

class CloudDatabase(object):
    # Init database and input ip
    # 初始化数据库并传入ip
    def __init__(self, database, user, password, ip="127.0.0.1", port="5432"):
        self.database = database
        self.user = user
        self.password = password
        self.ip = ip
        self.port = port

    # Connect database and set input as host, return connection and cursor
    # 连接ip端数据库并返回connection和cursor
    def db_connect(self):
        self.connection = psycopg2.connect(database=self.database, user=self.user,
                                           password=self.password, host=self.ip, port=self.port)
        self.cursor = self.connection.cursor()

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            
    # Write log file
    # 输出日志
    def write_log(self, e):
        self.connection.rollback()
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))


def test_flickr(api_key, api_secret):
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
    # 获取所有图片
    try:
        photos = flickr.walk(lat='40.7831', lon='-73.9712', radius=1, per_page=500, extras='url_c')
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))
    # 获取每一张图片
    try:
        for photo_url in photos:
            url = photo_url.get('url_c')
            # 如果url不为空,将该图片插入数据库
            if url is not None:
                photo_id = int(photo_url.get('id'))
                print("Success! Photo id:" + str(photo_id) + "\tPhoto url:" + url)
                print("Success! Key:" + str(api_key) + "\tSecret:" + str(api_secret))
                break
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))

def test_facepp(key, secret):
    try:
        url = 'https://api-us.faceplusplus.com/facepp/v3/detect'
        params = {
            "api_key": key,
            "api_secret": secret,
            "image_url": 'https://www.faceplusplus.com/scripts/demoScript/images/demo-pic6.jpg',
            "return_attributes": "gender,age,smiling,emotion,facequality,ethnicity"
        }
        r = requests.post(url, params)
        # 如果没有超过并发限制
        if r.status_code == 200:
            print("Success! Key:" + str(key) + "\tSecret:" + str(secret))
        else:
            print("Failed! Key:" + str(key) + "\tSecret:" + str(secret))
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))

if __name__ == '__main__':
    database = CloudDatabase("PlaceEmotion", "postgres", "postgres", "127.0.0.1")
    database.db_connect()
    # Test Flickr API
    sql = '''
	SELECT key, secret
	FROM API
	WHERE type = 'flickr'
	'''
    database.execute(sql)
    for i, api in enumerate(database.cursor.fetchall()):
        print(i)
        test_flickr(api[0], api[1])

    # Test Face++ API
    sql = '''
	SELECT key, secret
	FROM API
	WHERE type = 'Face++'
	'''
    database.execute(sql)
    for i, api in enumerate(database.cursor.fetchall()):
        print(i)
        test_facepp(api[0], api[1])
