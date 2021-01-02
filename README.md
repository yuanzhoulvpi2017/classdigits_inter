# 介绍

这个是一个交互式的手写数值识别，本质上是web应用，使用的就是分类模型，然后将模型放到flask里面，然后写一个web网页用来接受手写内容，使用JavaScript发送手写内容数据给python的flask。然后在控制台获得预测概率和分类类别。

![example](https://github.com/yuanzhoulvpi2017/classdigits_inter/blob/main/images/%E6%88%AA%E5%B1%8F2021-01-02%20%E4%B8%8B%E5%8D%882.21.20.png)


# 具体内容

1. images文件夹用来保存图片的，当你每在网页上按下send的时候，你在html手写的内容都会被保存到这个文件夹下。
2. templates文件夹是用来保存前端的内容，这里主要是保存了前端网页（index.html)，JavaScript、css等内容都放在index.html文件里了。
3. pickle_model.pkl文件是通过pickle包将sklearn模型给保存为二进制文件。这个就是我之前训练好的模型。
4. app.py就是我整个的python运行代码。这里包含对模型的加载、flask的一些后端处理和发送内容、还包括图像处理等一系列代码。



# 运行部分

1. 先将整个仓库下载，然后在文件夹下运行python代码即可

```bash
python app.py
```

这里运行好之后，就开业在控制台看到一些信息，然后在本地浏览器里面打开链接：[http://127.0.0.1:5000/](http://127.0.0.1:5000/)。即可看到一个网页。

2. 使用鼠标在虚线框内绘画（手写0-9）。按下鼠标左键然后拖住移动，写出一个数字，可以多次绘画内容，如果不满意可以按`clear`按钮。当写好之后，按下`send`按钮，就可以在控制台看到被计算的结果。最后计算手写的所有数值都在images文件夹里面。



# 训练数据部分

1. 这个训练数据集，来自kaggle的数据 [mnistasjpg](https://www.kaggle.com/scolianni/mnistasjpg)。使用的主要是scikit-learn和numpy、scikit-image、matplotlib等，这个重要的不是对模型的训练，强调的是对整个数据建模、发布模型的把握。





