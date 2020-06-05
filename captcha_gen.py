# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import captcha_setting
import os

def random_captcha():
    captcha_text = []
    for i in range(captcha_setting.MAX_CAPTCHA):
        c = random.choice(captcha_setting.ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha(width=captcha_setting.IMAGE_WIDTH, height=captcha_setting.IMAGE_HEIGHT)
    captcha_text = random_captcha()
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image

if __name__ == '__main__':
    count = 100000
    paths = [captcha_setting.TRAIN_DATASET_PATH, captcha_setting.TEST_DATASET_PATH,captcha_setting.PREDICT_DATASET_PATH]   #通过改变此处目录，以生成 训练、测试和预测用的验证码集
    #paths = [captcha_setting.TRAIN_DATASET_PATH]   #通过改变此处目录，以生成 训练、测试和预测用的验证码集

    for path in paths:
        if path == captcha_setting.TRAIN_DATASET_PATH:
            count = 100000
        else:
            count = 1000
        if not os.path.exists(path):
            os.makedirs(path)
        for i in range(count):
            now = str(int(time.time()))
            text, image = gen_captcha_text_and_image()
            filename = text+'_'+now+random.choice(captcha_setting.ALL_CHAR_SET)+'.png'
            image.save(path  + os.path.sep +  filename)
            print('saved %d : %s' % (i+1,filename))

