# xianshangtupianchaxun
一个图片查询项目，可以根据用户输入的特定字符返回特定图像资源。

使用了python中的flash模块做后端，

html文件在templates文件夹里面，按照查询前和查询后制作了两个界面。

data.json用于记录匹配键值

conformed.json用于记录已确认的图片信息（自动生成）

feedback.text用于存储反馈信息（自动生成）

能看到的大概都是160班的同学，所以我简单讲一下这个怎么使用的：

首先：你需要将图片资源放在phonos的文件夹中

第二步：更新data.json文件，按照提示格式把要查查询的键值输入在里面

第三步：双击运行app.py。输入本地网址即可发访问

另外，如果你想要把它放到公网上，让大家都可以访问，你可以使用Cloudflare Tunnel软件来帮助你，或者你可以去租借一台服务器（如果你有钱的话）
下面介绍怎么使用Cloudflare Tunnel

下载：

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/

下载 Windows 版本

得到文件：

cloudflared.exe

把它放到你的项目目录里面

在项目目录打开 CMD

运行：

cloudflared tunnel --url http://localhost:5000（）

注意localhost是一个变量，需要输入你自己的本地网址，如
cloudflared tunnel --url http://127.0.0.1:5000

运行后会看到类似输出：

https://random-name.trycloudflare.com

例如：

https://blue-tree-planet.trycloudflare.com

把这个网址发给同学

同学直接打开：

就能看到你的系统。
不需要：同一 WiFi校园网IP 地址手机电脑都可以访问。

如果你有心愿意花点时间折腾，并且还有疑问的，可以来私信我，欢迎随时为你答疑
