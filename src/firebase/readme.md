[&#8249; Firebase Doc Home](./)

<h1>Firebase 集成指南</h1>
<<[../../shared/-VERSION-/version.md]

## 集成
用如下命令来集成 SDKBOX Firebase 插件,请确保您可以正常执行的 SDKBOX 安装器.
```bash
$ sdkbox import firebase
```

<<[../../shared/notice.md]

<!--## Configuration
<<[../../shared/sdkbox_cloud.md]
<<[../../shared/remote_application_config.md]-->

### JSON 配置

Firebase 的配置可以在 firebase 官网去[下载](https://console.firebase.google.com)

#### iOS Plist
iOS 的配置文件是在对应 `iOS 工程` 中的设置中，下载 `GoogleService-Info.plist` 文件, 并把它拖到你的 iOS 工程中

#### Android Json
Android 的配置文件是在对应 `Android 工程` 中的设置中, 下载 `google-services.json` 文件.

__注意__:
`google-services.json` 是要和对应的 Firebase Gradle插件一起配合使用的. 在这里并没有使用 Firebase Gradle 插件,所以我们需要把 `google-services.json` 转为 xml 再使用, 步骤如下:

 * 打开命令行窗口
 * 进入到 `google-services.json` 文件所在目录
 * 运行如下命令

```python
python -c """import urllib; import sys; sys.argv = ['transpy', '-i', './google-services.json', '-o', './googleservices.xml']; s = urllib.urlopen('https://raw.githubusercontent.com/sdkbox-doc/en/master/tools/generate_xml_from_google_services_json.py').read(); exec(s);"""
```

 * 命令运行完成后, 会有一个 `googleservices.xml` 生成, 把它放到你的 Android 工程中的 `res/values/googleservices.xml` 就可以了

更多信息可以见[这里](https://support.google.com/firebase/answer/7015592)

<!--<<[sdkbox-config-encrypt.md]-->

## 使用
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[../../shared/manual_integration_android_and_android_studio.md]

<<[manual_android.md]

<<[extra-step.md]

<<[proguard.md]

<<[../shared/debug.md]
