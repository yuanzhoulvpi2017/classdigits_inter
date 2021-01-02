from __future__ import print_function
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for


import io
import base64
import os
import uuid

from skimage.io import imread
from skimage.transform import resize

import numpy as np
import pandas as pd

import pickle
import time

app = Flask(__name__)
app.secret_key = "s3cr3t"
app.debug = True
app._static_folder = os.path.abspath("templates/")


@app.route("/", methods=['GET'])
def index():
    """
    被渲染的网页
    """
    return render_template("index.html")


@app.route("/postcdata", methods=['POST'])
def post_javascript_data():
    """
    这个网页是用来获得js发送的canvas。然后将canvas的内容提取出来保存到本地图片
    """
    jsdata = request.form['canvasdata']
    print("get image\n")
    unique_id = str(uuid.uuid4())  # 获得每一个图片独一二的名字用作保存文件的文件名
    with open("images/" + unique_id+".png", 'wb') as file:
        file.write(base64.b64decode(jsdata.split(',')[1]))

    data = pc_canvas(unique_id)
    class_type = getclass(data)

    # 在控制台打印结果
    class_typeprob = getclass_proba(data)
    print("*------------------------------------------------------------------------*")
    print("get result:", time.strftime("%Y-%m-%d %X"))
    print(f"this data is ->: {class_type}")
    print_prob(class_typeprob['proba'].values)
    print("*------------------------------------------------------------------------*")
    return str(class_type[0])  # jsdata


def pc_canvas(imgfilepath):
    """
    这个函数是加载本地照片，然后将照片的尺寸从(560, 560) -> （28, 28)
    """
    testimage = imread(f"images/{imgfilepath}.png")

    image3 = transimage(testimage)

    return image3


def transimage(imagedata):
    """
    transform image 
    """
    image2 = imagedata.sum(axis=2)
    # interval = 300
    image2 = imagedata.sum(axis=2).copy()
    image3 = resize(image2, (28, 28))
    image3[np.where(image3 > 0)] = 1
    return image3


def getclass(data):
    """
    这函数是加载sklearn模型，然后做出预测类别
    """
    # Load from file
    pkl_filename = "pickle_model.pkl"

    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    temp_data = data.reshape(1, 784)
    classtype = pickle_model.predict(temp_data)
    return classtype


def getclass_proba(data):
    """
    这函数是加载sklearn模型，然后做出预测概率。
    """
    # Load from file
    pkl_filename = "pickle_model.pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)

    temp_data = data.reshape(1, 784)
    classtype_prob = pickle_model.predict_proba(temp_data)
    classtype_prob = pd.DataFrame({"class": [f'class_{i}' for i in range(10)],
                                   'proba': np.round(classtype_prob.flatten(), 3)})
    return classtype_prob


def print_prob(value):
    """
    这个是为了在控制台里面显示每一个预测类别的概率（数据被取整）1～10
    """
    value = np.round(value*10, 1).flatten()
    classlist = [f"class_{i}" for i in range(10)]
    for i in range(10):
        print(f"{classlist[i]}: {'*' * np.int(value[i])}")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
