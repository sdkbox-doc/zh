
# SDKBoxPlay 疑问

## Keystore

SDKBox经常会出现登录失败, 其中比较常见的原因就是 Keystore , 以下介绍怎么检查 Keystore.

其实主要就是要保证以下三个地方的 Keystore 的 SHA-1 是一样的.

- 你的调试工程中所用到的 keystore's SHA-1

运行命令 `keytool -list -v -keystore your.keystore` , 可以得到类型的如下结果, 请注意其中的 SHA1 :

```bash

...

Certificate fingerprints:
	 MD5:  09:F2:CA:99:6A:EF:8D:B7:17:B8:25:AE:36:40:9F:E2
	 SHA1: C7:4F:9C:6C:54:67:BC:81:27:25:40:EA:24:3D:B7:AA:1E:7A:7B:7D
	 SHA256: 92:51:09:9D:4A:A0:E5:4B:A8:6D:62:8B:3A:1B:F0:96:02:55:B9:1A:05:E4:68:32:0D:E1:F5:8A:A2:66:24:B1

...

```

- APK中的 SHA-1

从 GooglePlay 中下载下来当前活跃的包

获取 APK 的 SHA-1 可以运行以下命令:

```bash

unzip download.apk -d apk
keytool -printcert -file ./apk/META-INF/CERT.RSA

```

然后会得到类似的如下结果，注意其中的 SHA-1 :

```

Certificate fingerprints:
	 MD5:  09:F2:CA:99:6A:EF:8D:B7:17:B8:25:AE:36:40:9F:E2
	 SHA1: C7:4F:9C:6C:54:67:BC:81:27:25:40:EA:24:3D:B7:AA:1E:7A:7B:7D
	 SHA256: 92:51:09:9D:4A:A0:E5:4B:A8:6D:62:8B:3A:1B:F0:96:02:55:B9:1A:05:E4:68:32:0D:E1:F5:8A:A2:66:24:B1

```

- Google Game services 中的 SHA-1

    * 打开 [Google Play Console](https://play.google.com/apps/publish)
    * 点击 'Game services' -> app
    * 到相庆的 Google API Console

    ![](../imgs/sdkboxplay_game_services.png)

    * 检查其中 Android Client 中配置的 SHA-1

    ![](../imgs/sdkbox_android_client.png)


__注意: 这上面的三个 SHA-1 应该是一样的.__


## Server Auth Code

如果你需要 Goolge 登录的 server auth code的话，你需要在 `sdkbox_config.json` 配置 `web_client_id`.

```json
{
    "android": {
        "sdkboxplay": {
            ...
            "debug": true,
            "web_client_id": "340534096218-goaafgmlsc8ut9730lae5kg2kh9m2i35.apps.googleusercontent.com"
        }
    },
    "ios": {
        "sdkboxplay": {
            ...
        }
    }
}
```

注意，`web_client_id`是从这里得到的:

![](../imgs/sdkboxplay_webclientid.png)


如果你需要 server auth code 的话，请移除掉 `web_client_id`.

