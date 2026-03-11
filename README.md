# 高清碑帖收藏网

这是一个基于Python Flask框架开发的碑帖收藏网站，展示历代书法名家的经典碑帖作品。

## 功能特点

- 以卡片形式展示碑帖信息
- 卡片显示碑帖名称和书法家朝代、姓名
- 点击卡片跳转到对应的碑帖详情页面
- 响应式设计，支持不同屏幕尺寸
- 美观的UI设计，符合书法艺术的文化氛围

## 技术栈

- **后端**: Python Flask
- **前端**: HTML5, CSS3, JavaScript
- **样式框架**: Tailwind CSS v3
- **图标库**: Font Awesome

## 项目结构

```
beitie_website/
├── app.py              # 主应用程序
├── requirements.txt    # 依赖项列表
├── README.md          # 项目说明文档
├── server.log         # 服务器日志文件
└── templates/         # HTML模板文件
    └── index.html     # 首页模板
```

## 本地运行

1. 克隆项目到本地
```bash
git clone https://gitee.com/your-username/beitie-website.git
cd beitie-website
```

2. 安装依赖项
```bash
pip3 install -r requirements.txt
```

3. 运行应用程序
```bash
python3 app.py
```

4. 在浏览器中访问
```
http://localhost:5000
```

## 部署到Gitee Pages

Gitee Pages主要用于静态网站部署，由于我们的网站使用了Python后端，需要通过Gitee的云服务或其他方式部署。

### 方法一：使用Gitee云函数
1. 注册Gitee云函数服务
2. 将代码上传到Gitee云函数
3. 配置环境变量和运行参数

### 方法二：使用静态文件部署
1. 生成静态网站文件
2. 将静态文件部署到Gitee Pages

## 数据管理

碑帖数据存储在`app.py`文件的`beitie_data`列表中，您可以通过修改这个列表来添加或删除碑帖信息：

```python
beitie_data = [
    {
        "id": 1,
        "name": "兰亭集序",
        "calligrapher": "东晋 王羲之",
        "image": "https://aka.doubaocdn.com/s/O3PN1w2QQ9",
        "url": "https://www.dpm.org.cn/collection/impres/228604.html"
    },
    # 更多碑帖数据...
]
```

## 自定义配置

### 修改网站主题色
在`index.html`文件中修改Tailwind CSS配置：

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: '#8B4513',    // 主色调（棕色）
                secondary: '#D2691E',  // 辅助色（沙棕色）
                accent: '#F4A460',     // 强调色（沙滩色）
                dark: '#2F1B14',       // 深色
                light: '#FFF8DC'       // 浅色（玉米丝色）
            }
        }
    }
}
```

### 添加更多碑帖
在`app.py`的`beitie_data`列表中添加新的碑帖对象即可。

## 贡献

欢迎提交Pull Request来改进这个项目，您可以：
- 添加更多碑帖数据
- 改进UI设计
- 增加新功能
- 修复bug

## 许可证

本项目采用MIT许可证，详情请见LICENSE文件。

## 联系我们

如果您有任何问题或建议，请联系：
- 邮箱：contact@beitie.com
- 电话：+86 123 4567 8910
