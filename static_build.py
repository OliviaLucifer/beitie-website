from flask import Flask, render_template
import os
from shutil import copytree, copy2

# 初始化Flask应用（和app.py保持一致）
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


# 首页路由（复制app.py中的index路由，确保一致）
@app.route('/')
def index():
    return render_template('index.html', beitie_list=beitie_data)


# 核心：手动生成静态文件（无需复杂命令，执行该脚本即可）
def build_static_files():
    # 定义静态文件输出目录（和之前一致，仍为static_dist）
    output_dir = 'static_dist'
    # 若目录已存在，先删除（避免旧文件干扰）
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    # 创建输出目录
    os.makedirs(output_dir)

    # 生成首页index.html文件
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(app.test_client().get('/').data.decode('utf-8'))

    # 复制templates文件夹中的其他HTML文件（若有）
    templates_dir = 'templates'
    if os.path.exists(templates_dir):
        for root, dirs, files in os.walk(templates_dir):
            for file in files:
                if file.endswith('.html'):
                    # 生成对应路由的静态文件（若有其他路由，可参考index路由添加）
                    route = '/' + file.replace('.html', '') if file != 'index.html' else '/'
                    try:
                        html_content = app.test_client().get(route).data.decode('utf-8')
                        target_path = os.path.join(output_dir, file)
                        with open(target_path, 'w', encoding='utf-8') as f:
                            f.write(html_content)
                    except:
                        # 若有异常，直接复制文件（避免报错）
                        copy2(os.path.join(root, file), output_dir)

    # 复制static文件夹（CSS、JS、图片等静态资源）
    static_dir = 'static'
    if os.path.exists(static_dir):
        copytree(static_dir, os.path.join(output_dir, 'static'))

    print("静态文件生成完成！已保存到 static_dist 文件夹")


# 执行静态化
if __name__ == '__main__':
    build_static_files()