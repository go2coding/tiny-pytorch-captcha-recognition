改项目是基于 https://github.com/dee1024/pytorch-captcha-recognition

CNN的原理这里就不重点介绍了，需要的可以参考：https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53 等相关的资料。

CNN的模型图：
=========

![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/1_vkQ0hXDaQv57sALXAJquxA.jpeg)


图片字体识别的过程：

![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/1_uAeANQIOQPqWZnnuH-VEyw.jpeg)


修改
=========


这个项目是基于 https://github.com/dee1024/pytorch-captcha-recognition 的修改，修改的原因：

对于这个深度学习的项目，本身来说并没有特别好的机器来跑训练数据，在我这台 处理器为：i5-3570 3.20GHz的电脑上，跑了两天多的时间，达到的效果并不好，识别为为20%左右。

![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/20200605101002.png)

![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/20200605101025.png)

我想可能也有很多人和我的情况一样，在学完了机器学习的算法后，想跑跑其他的项目，但是机子的性能又不允许。

还有一个原因是这个项目的写法，并不适合初学者，数据的准备和测试不太方便，这里进行了简单的修改。


先说一下配置：
====

虚拟机 Ubuntu 20.04 LTS (GNU/Linux 5.4.0-33-generic x86_64)

环境：
====

Python 3.8.2

python 2.7的我也试过，pytorch出现了一大堆的错误，建议不要使用。

ImageCaptcha库(pip install captcha)、 Pytorch(参考官网http://pytorch.org)


运行的结果：


	python captcha_test.py
	
	
====

![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/20200605103409.png)



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
	
其它
===
* 机器学习交流 qq：1752338621


	
深度学习识别验证码
=========

本项目致力于使用神经网络来识别各种验证码。

特性
===
- __端到端，不需要做更多的图片预处理（比如图片字符切割、图片尺寸归一化、图片字符标记、字符图片特征提取）__
- __验证码包括数字、大写字母、小写__
- __采用自己生成的验证码来作为神经网络的训练集合、测试集合、预测集合__
- __纯四位数字，验证码识别率高达 99.9999 %__
- __四位数字 + 大写字符，验证码识别率约 96 %__
- __深度学习框架pytorch + 验证码生成器ImageCaptcha__


原理
===

- __训练集合生成__

    使用常用的 Python 验证码生成库 ImageCaptcha，生成 10w 个验证码，并且都自动标记好;
    如果需要识别其他的验证码也同样的道理，寻找对应的验证码生成算法自动生成已经标记好的训练集合或者手动对标记，需要上万级别的数量，纯手工需要一定的时间，再或者可以借助一些网络的打码平台进行标记

- __训练卷积神经网络__
    构建一个多层的卷积网络，进行多标签分类模型的训练
    标记的每个字符都做 one-hot 编码
    批量输入图片集合和标记数据，大概15个Epoch后，准确率已经达到 96% 以上


验证码识别率展示
========
![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/number.png)
![](https://raw.githubusercontent.com/dee1024/pytorch-captcha-recognition/master/docs/number2.png)


快速开始
====
- __步骤一：10分钟环境安装__

    Python2.7+ 、ImageCaptcha库(pip install captcha)、 Pytorch(参考官网http://pytorch.org)


- __步骤二：生成验证码__
    ```bash
    python captcha_gen.py
    ```
    执行以上命令，会在目录 dataset/train/ 下生成多张验证码图片，图片已经标注好，数量可以是 1w、5w、10w，通过 captcha-gen.py 内的 count 参数设定
    
- __步骤三：训练模型__
    ```bash
    python captcha_train.py
    ```
    使用步骤一生成的验证码图集合用CNN模型（在 catcha_cnn_model 中定义）进行训练，训练完成会生成文件 model.pkl

- __步骤四：测试模型__
    ```bash
    python captcha_test.py
    ```
    可以在控制台，看到模型的准确率（如 95%） ，如果准确率较低，回到步骤一，生成更多的图片集合再次训练

- __步骤五：使用模型做预测__
    ```bash
    python captcha_predict.py
    ```
    可以在控制台，看到预测输出的结果
    
贡献
===
我们期待你的 pull requests !

作者
===
* __Dee Qiu__ <coolcooldee@gmail.com>

其它
===
* __Github项目交流QQ群__ 570997546


声明
===
本项目仅用于交流学习