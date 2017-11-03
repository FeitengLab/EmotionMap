# coding:utf-8
# version:python3.5.1
# author:kyh
# test if face++ api expires

import requests

API_KEY = "Dm18HrboYUuAVeX6A-_6Y0q27OkE3cvN"
API_SECRET = "3FPheINGB2qLTDcV-FOpjloXmOjDDG4A"


def detect_emotion(img_url):
    url = "https://api-us.faceplusplus.com/facepp/v3/detect"
    params = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "image_url": img_url,
        "return_attributes": "gender,age,smiling,emotion,facequality,ethnicity"
    }
    r = requests.post(url, params)
    print(r.status_code)

if __name__ == '__main__':
    detect_emotion("https://www.learnopencv.com/wp-content/uploads/2015/10/Facial-Feature-Detection-1024x577.jpg")
