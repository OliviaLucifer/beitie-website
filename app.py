from flask import Flask, render_template
import os

app = Flask(__name__)


# 碑帖数据
beitie_data = [
    {
        "id": 1,
        "name": "碑帖合集",
        "calligrapher": "  ",
        "image": "https://aka.doubaocdn.com/s/MBLy1w2QQG",
        "url": "http://www.hanmofengya.com/Index.html"
    },
    {
        "id": 2,
        "name": "《隶书千字文》",
        "calligrapher": "清 席夔",
        "image": "http://5b0988e595225.cdn.sohucs.com/images/20190114/870fb57263ce45a599c419b3b0b47796.jpeg",
        "url": "https://www.sohu.com/a/288899061_100118760"
    },
    {
        "id": 3,
        "name": "《宣示表》",
        "calligrapher": "魏 钟繇",
        "image": "https://b.sfzd.cn/upload/20150208/14233646785957.jpg",
        "url": "https://www.shufazidian.com/ziliao/41429.html"
    },
    {
        "id": 4,
        "name": "《黄庭经》",
        "calligrapher": "晋 王羲之",
        "image": "https://p9.itc.cn/images01/20230811/f5c7939016bd484fa5fe58025d172a5a.jpeg",
        "url": "https://www.sohu.com/a/710839137_99985427"
    },
    {
        "id": 5,
        "name": "《草堂十志》",
        "calligrapher": "明 文徵明",
        "image": "	https://p3.itc.cn/q_70/images03/20220928/d7d204b18f0b4924a35be8c9170ffd59.jpeg",
        "url": "https://www.sohu.com/a/588758958_121124765"
    },
    {
        "id": 6,
        "name": "《琴赋》",
        "calligrapher": "明 文徵明",
        "image": "https://5b0988e595225.cdn.sohucs.com/images/20190910/933872c88e754f0e9412d56eb1975186.jpeg",
        "url": "https://www.sohu.com/a/339951625_227108"
    },
    {
        "id": 7,
        "name": "《落花诗册》",
        "calligrapher": "明 文徵明",
        "image": "https://pic2.zhimg.com/v2-85f2a96bf277403f351bcd5ea79aa0f5_1440w.jpg",
        "url": "https://zhuanlan.zhihu.com/p/667313472"
    },
    {
        "id": 8,
        "name": "《般若波罗蜜多心经》",
        "calligrapher": "唐 欧阳询",
        "image": "https://static.lingyinsi.org/attachment/upload/2021/11/15/194313.jpeg",
        "url": "https://www.toutiao.com/article/7215876513542636089/"
    }

]

@app.route('/')
def index():
    return render_template('index.html', beitie_list=beitie_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)