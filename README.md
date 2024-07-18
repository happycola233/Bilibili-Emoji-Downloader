# 哔哩哔哩表情包下载工具

这是一个Python脚本，用于通过你的`SESSDATA`和`bili_jct` Cookie从哔哩哔哩（Bilibili）下载表情包。

## 环境要求

- Python 3.x
- Requests库 (`pip install requests`)

## 设置步骤

1. 克隆仓库：
   ```
   git clone https://github.com/happycola233/Bilibili-Emoji-Downloader.git
   cd Bilibili-Emoji-Downloader
   ```

2. 安装依赖：
   ```
   pip install requests
   ```

3. 运行脚本：
   ```
   python src/B站表情下载.py
   ```

## 获取 `SESSDATA` 和 `bili_jct`

1. **登录哔哩哔哩网站**：
   - 使用你的浏览器登录到哔哩哔哩的账号。
   - 确保你已经登录并能够访问私信页面。

2. **打开开发者工具**：
   - 在浏览器中按下 F12 键（或右键点击页面并选择“检查”），打开开发者工具。

3. **选择“网络”选项卡**：
   - 在开发者工具中，选择“网络”选项卡。

4. **刷新页面**：
   - 刷新哔哩哔哩页面，以便开发者工具捕获网络请求。

5. **查找请求中的 Cookie**：
   - 在网络请求列表中，找到包含私信请求的条目（通常以 `api.vc.bilibili.com` 开头）。
   - 点击该请求条目，在右侧的“标头”选项卡下找到“请求标头”部分。
   - 在请求标头中，可以找到名为 `Cookie` 的字段。

6. **复制 SESSDATA 和 bili_jct**：
   - 在 Cookie 字段中，复制包含 `SESSDATA` 和 `bili_jct` 的值。这些值通常以分号分隔，类似于 `SESSDATA=xxxxxxxx; bili_jct=xxxxxxxx`。


## 使用方法

1. 在提示时输入你的`SESSDATA`和`bili_jct` Cookie。这些Cookie是访问哔哩哔哩API所必需的。
2. 选择将下载的表情保存到桌面或自定义路径。
3. 脚本将创建一个名为 "表情下载" 的目录，并按表情包的名称将其组织到子目录中。

## 注意事项

- 确保你的`SESSDATA`和`bili_jct` Cookie有效，并具有必要的权限。
- 此脚本将排除“最近使用”和“颜文字”之类的表情包。

## 免责声明

此脚本仅供个人使用。请遵守哔哩哔哩的服务条款和API使用政策。
