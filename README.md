# 介绍

这个是一个交互式的手写数值识别，本质上是web应用，使用的就是分类模型，然后将模型放到flask里面，然后写一个web网页用来接受手写内容，使用JavaScript发送手写内容数据给python的flask。然后在控制台获得预测概率和分类类别。



# 具体内容

1. images文件夹用来保存图片的，当你每在网页上按下send的时候，你在html手写的内容都会被保存到这个文件夹下。
2. templates文件夹是用来保存前端的内容，这里主要是保存了前端网页（index.html)，JavaScript、css等内容都放在index.html文件里了。
3. pickle_model.pkl文件是通过pickle包将sklearn模型给保存为二进制文件。这个就是我之前训练好的模型。
4. app.py就是我整个的python运行代码。这里包含对模型的加载、flask的一些后端处理和发送内容、还包括图像处理等一系列代码。
