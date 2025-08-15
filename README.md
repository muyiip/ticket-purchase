# 大麦抢票脚本 V1.0
### 特征

- 自动无延时抢票
- 支持人员、城市、日期场次、价格选择

## 功能介绍
通过selenium打开页面进行登录，模拟用户购票流程自动购票

其流程图如下:

<img src="img/大麦抢票流程.png" width="50%" height="50%" />

## 准备工作
### 1. 配置环境

#### 1.1安装python3环境

**Windows**

1. 访问Python官方网站：https://www.python.org/downloads/windows/
2. 下载最新的Python 3.9+版本的安装程序。
3. 运行安装程序。
4. 在安装程序中，确保勾选 "Add Python X.X to PATH" 选项，这将自动将Python添加到系统环境变量中，方便在命令行中使用Python。
5. 完成安装后，你可以在命令提示符或PowerShell中输入 `python3` 来启动Python解释器。

**macOS**

1. 你可以使用Homebrew来安装Python 3。

   - 安装Homebrew（如果未安装）：打开终端并运行以下命令：

     ```shell
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

   - 安装Python 3：运行以下命令来安装Python 3：

     ```shell
     brew install python@3
     ```

#### 1.2 安装所需要的环境

在命令窗口输入如下指令

```shell
pip3 install selenium
```

#### 1.3 下载google chrome浏览器

下载地址: https://www.google.cn/intl/zh-CN/chrome/?brand=YTUH&gclid=Cj0KCQjwj5mpBhDJARIsAOVjBdoV_1sBwdqKGHV3rUU1vJmNKZdy5QNzbRT8F5O0-_jq1WHXurE8a7MaAkWrEALw_wcB&gclsrc=aw.ds

### 2. 修改配置文件

在运行程序之前，需要先修改`config.json`文件。该文件用于指定用户需要抢票的相关信息，包括演唱会的场次、观演的人员、城市、日期、价格等。文件结果如下图所示：

<img src="img/config_json.png" width="50%" height="50%" />

#### 2.1 文件内容说明

- `index_url`为大麦网的地址，**无需修改**
- `login_url`为大麦网的登录地址，**无需修改**
- `target_url`为用户需要抢的演唱会票的目标地址，**待修改**
- `users`为观演人的姓名，**观演人需要用户在手机大麦APP中先填写好，然后再填入该配置文件中**，**待修改**
- `city`为城市，**如果用户需要抢的演唱会票需要选择城市，请把城市填入此处。如无需选择，则不填**
- `date`为场次日期，**待修改，可多选**
- `price`为票档的价格，**待修改，可多选**
- `if_commit_order`为是否要自动提交订单，**改成 true**
- if_listen为是否回流监听，**改成true**



#### 2.2 示例说明

进入大麦网https://www.damai.cn/，选择你需要抢票的演唱会。假设如下图所示：

<img src="img/example.png" width="50%" height="50%" />

接下来按照下图的标注对配置文件进行修改：

<img src="img/example_detail.png" width="50%" height="50%" />

最终`config.json`的文件内容如下：

```json
{
  "index_url": "https://www.damai.cn/",
  "login_url": "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F",
  "target_url": "https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e1JQGWHg&id=740680932762",
  "users": [
    "名字1",
    "名字2"
  ],
  "city": "广州",
  "date": "2023-10-28",
  "price": "1039",
  "if_listen":true,
  "if_commit_order": true
}
```



### 3.运行程序

运行程序开始抢票，进入命令窗口，执行如下命令：

```shell
cd damai
python3 damai.py
```



# 大麦app抢票

大麦app抢票脚本需要依赖appium，因此需要现在安装appium server&client环境，步骤如下：

## appium server

### 下载

- 先安装好node环境（具备npm）node版本号18.0.0

- 先下载并安装好android sdk，并配置环境变量（appium server运行需依赖android sdk)

- 下载appium

  ```shell
  npm install -g appium
  ```

- 查看appium是否安装成功

  ```shell
  appium -v
  ```

- 下载UiAutomator2驱动

  ```shell
  npm install appium-uiautomator2-driver
  ```

​		可能会遇到如下错误：

```tex
➜  xcode git:(master) ✗ npm install appium-uiautomator2-driver

npm ERR! code 1
npm ERR! path /Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver
npm ERR! command failed
npm ERR! command sh -c node install-npm.js
npm ERR! [11:57:54] Error installing Chromedriver: Request failed with status code 404
npm ERR! [11:57:54] AxiosError: Request failed with status code 404
npm ERR!     at settle (/Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/axios/lib/core/settle.js:19:12)
npm ERR!     at IncomingMessage.handleStreamEnd (/Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver/node_modules/axios/lib/adapters/http.js:572:11)
npm ERR!     at IncomingMessage.emit (node:events:539:35)
npm ERR!     at endReadableNT (node:internal/streams/readable:1344:12)
npm ERR!     at processTicksAndRejections (node:internal/process/task_queues:82:21)
npm ERR! [11:57:54] Downloading Chromedriver can be skipped by setting the'APPIUM_SKIP_CHROMEDRIVER_INSTALL' environment variable.

npm ERR! A complete log of this run can be found in:
npm ERR!     /Users/chenweicheng/.npm/_logs/2023-10-26T03_57_35_950Z-debug-0.log
```

​		解决办法（添加环境变量，错误原因是没有找到chrome浏览器驱动，忽略即可）

```shell
export APPIUM_SKIP_CHROMEDRIVER_INSTALL=true
```

### 启动

启动appium server并使用uiautomator2驱动

```shell
appium --use-plugins uiautomator2
```

启动成功将出现如下信息：

```
[Appium] Welcome to Appium v2.2.1 (REV 2176894a5be5da17a362bf3f20678641a78f4b69)
[Appium] Non-default server args:
[Appium] {
[Appium]   usePlugins: [
[Appium]     'uiautomator2'
[Appium]   ]
[Appium] }
[Appium] Attempting to load driver uiautomator2...
[Appium] Requiring driver at /Users/chenweicheng/Documents/xcode/node_modules/appium-uiautomator2-driver
[Appium] Appium REST http interface listener started on http://0.0.0.0:4723
[Appium] You can provide the following URLs in your client code to connect to this server:
[Appium] 	http://127.0.0.1:4723/ (only accessible from the same host)
[Appium] 	http://172.31.102.45:4723/
[Appium] 	http://198.18.0.1:4723/
[Appium] Available drivers:
[Appium]   - uiautomator2@2.32.3 (automationName 'UiAutomator2')
[Appium] No plugins have been installed. Use the "appium plugin" command to install the one(s) you want to use.
```

其中`[Appium] 	http://127.0.0.1:4723/ (only accessible from the same host)
[Appium] 	http://172.31.102.45:4723/
[Appium] 	http://198.18.0.1:4723/`为appium server连接地址



## appium client

- 先下载并安装好python3和pip3

- 安装

  ```shell
  pip3 install appium-python-client
  ```

- 在代码中引入并使用appium

  ```python
  from appium import webdriver
  from appium.options.common.base import AppiumOptions
  
  device_app_info = AppiumOptions()
  device_app_info.set_capability('platformName', 'Android')
  device_app_info.set_capability('platformVersion', '10')
  device_app_info.set_capability('deviceName', 'YourDeviceName')
  device_app_info.set_capability('appPackage', 'cn.damai')
  device_app_info.set_capability('appActivity', '.launcher.splash.SplashMainActivity')
  device_app_info.set_capability('unicodeKeyboard', True)
  device_app_info.set_capability('resetKeyboard', True)
  device_app_info.set_capability('noReset', True)
  device_app_info.set_capability('newCommandTimeout', 6000)
  device_app_info.set_capability('automationName', 'UiAutomator2')
  
  # 连接appium server，server地址查看appium启动信息
  driver = webdriver.Remote('http://127.0.0.1:4723', options=device_app_info)
  
  ```

- 启动脚本程序

  ```shell
  cd damai_appium
  python3 damai_appium.py
  ```

  

## 大麦 iOS 抢票（Appium + XCUITest）

### 前置条件（必须在 macOS 上执行）
- 安装 Xcode（含命令行工具）并登录 Apple 开发者账号
- 安装 Node 18+ 与 Appium 2.x
  - `npm install -g appium`
  - 安装 iOS 驱动：`appium driver install xcuitest`
- 可选：`brew install ios-deploy`（提升真机部署稳定性）
- iPhone 打开“开发者模式”，用数据线连接 Mac，信任此电脑

### 准备配置
- 进入 `damai_appium_ios/`，修改 `config.json`：
  - `server_url`: 一般为 `http://127.0.0.1:4723`
  - `device_name`: iPhone 设备名称（如“iPhone 14 Pro”）
  - `platform_version`: iOS 版本（如“17.5”）
  - `udid`: 设备 UDID（在 Finder 或 Xcode 设备列表查看）
  - `bundle_id`: 大麦 iOS App 的 Bundle ID（示例：`cn.damai.iphone`，请以实际为准）
  - `keyword`/`city`/`date`/`price`/`users`/`if_commit_order`
  - 如首次在真机部署 WDA，需要配置 `xcode_org_id` 与 `xcode_signing_id`（Apple Development）

### 启动 Appium Server（iOS）
```bash
appium
```
- 终端中会打印出监听地址（例如 `http://127.0.0.1:4723`），与 `config.json` 对应

### 运行脚本
```bash
cd damai_appium_ios
python3 damai_ios.py
```

### 说明与限制
- 脚本运行在 Mac 上，通过 Appium/XCUITest 远程控制 iPhone；无法将此 Python 脚本“安装到 iPhone 内部直接运行”
- 首次运行会自动在真机上部署 WebDriverAgent（WDA），需保证签名配置正确并在手机上信任证书
- 为避免外部滥用，请仅在本机 `127.0.0.1` 启动 Appium Server
- 根据页面变化，需适时调整定位策略（本仓库已提供通用的 iOS Predicate / Class Chain 兜底）



