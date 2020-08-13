改项目是基于 https://github.com/dee1024/pytorch-captcha-recognition

CNN原理
=========

CNN的原理这里就不重点介绍了，需要的可以参考：https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 等相关的资料。

CNN的模型图：


![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/1_vkQ0hXDaQv57sALXAJquxA.jpeg)


图片字体识别的过程：

![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/1_uAeANQIOQPqWZnnuH-VEyw.jpeg)


修改
=========


这个项目是基于 https://github.com/dee1024/pytorch-captcha-recognition 的修改，修改的原因：

对于兴冲冲的我，拿到了这个项目，就开始训练数据，跑了两天多的时间，达到的效果并不好，识别准确率仅仅为20%左右。

![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/20200605101002.png)

![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/20200605101025.png)

我想有两个方面的原因：

1.我的计算机太烂了，处理器：i5-3570 3.20GHz，跑数据太慢。

2.我的训练样本太少了。


我想可能也有很多人和我的情况一样，在学完了机器学习的算法后，想跑跑其他的项目，但是机子的性能又不允许。

还有一个原因是这个项目的写法，并不适合初学者，数据的准备和测试不太方便，这里进行了简单的修改。


修改识别的难度：原项目识别4个（数字和字母）。首先，把难度降到最低试试。修改`captcha_setting.py` 把参数 MAX_CAPTCHA 改为1。



**为了在低计算力的地方进行训练，原项目的验证码为四位数，这里改为1位数：（相当于手写数字识别）**


![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/number.jpg)

先说一下配置：
====

虚拟机 Ubuntu 20.04 LTS (GNU/Linux 5.4.0-33-generic x86_64)

环境：
====

- Python 3.8.2

> python 2.7的我也试过，pytorch出现了一大堆的错误，建议不要使用。

- ImageCaptcha库(pip install captcha)

- Pytorch(参考官网http://pytorch.org)

到官网，根据自己实际的配置选择，

![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/20200813131209.png)

安装命令就很简单了：

	pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html


	
先看看准确率高不高
====

用默认的训练模型，看看测试的结果怎么样。

运行的结果：


	python captcha_test.py
	
	

![](https://raw.githubusercontent.com/go2coding/tiny-pytorch-captcha-recognition/master/docs/20200605103409.png)



测试了200张的图片识别率；: 98.500000 %。

识别错误的图片，这里都标注出来了，可以看到因为数字0和字母o长得太像了，没办法区分开来。


如何学习
====

- 生成验证码__

    ```bash
    python captcha_gen.py
    ```
这个地方有修改过，运行后训练数据生成10w张，测试和预测各生成1000张。

- 训练模型__
    ```bash
    python captcha_train.py
    ```
    使用步骤一生成的验证码图集合用CNN模型（在 catcha_cnn_model 中定义）进行训练，训练完成会生成文件 model.pkl

- 测试模型__
    ```bash
    python captcha_test.py
    ```
    可以在控制台，看到模型的准确率（如 95%） ，如果准确率较低，回到步骤一，生成更多的图片集合再次训练

可以改变`captcha_setting.py` 中 `MAX_CAPTCHA`的大小，来提高识别的难度。

**在MAX_CAPTCHA为3的情况下，10w训练样本是足够的，超过3的话，需要增加训练样本的个数。**
	
	
其它
===
* 机器学习交流 http://go2coding.com/