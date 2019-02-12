
# SDKBoxPlay 疑问

## Keystore

SDKBox经常会出现登录失败, 其中比较常见的原因就是 Keystore .

主要是三个地方的 Keystore:

1. Google Play Console 中配置的 Keystore 的 SHA-1
2. 真实用户下载的 APK 的 Keystore 的 SHA-1 应与 1 项的值保持一致
3. 开发者调试时的 APK 的 Keystore 的 SHA-1 应与 1 项的值保持一致(如果不需要调试SDKBoxPlay相关功能，可以不一致)

具体介绍:

- Google Game services 中的 SHA-1

    * 打开 [Google Play Console](https://play.google.com/apps/publish)
    * 点击 'Game services' -> app
    * 到相应的 Google API Console

    ![](../imgs/sdkboxplay_game_services.png)

    * 检查其中 Android Client 中配置的 SHA-1

    ![](../imgs/sdkbox_android_client.png)


- 真实用户下载的 APK 的 SHA-1

现在 GooglePlay 提供了两种 APK 签名方式:

第一种用户下载的 APK 就是开发者上传的 APK, GooglePlay不会重新签名, 这种方式下, 需要保证开发者上传的 APK 的 Keystore 与 Google Play Console 一致.

第二种是 GooglePlay 提供 App signing 这种方式，如果开发者使用了 App signing, 那么这种方式下, 需要保证 App Signing 与 Google Play Console 一致. 关于 App signing 的[说明](https://support.google.com/googleplay/android-developer/answer/7384423)

不管使用的是第一种还是第二种, 最终都是一个目的，保证真实用户下载到的 APK 的 Keystore 与 Google Play Console 一致.

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

- 开发者本地调试工程时所用到的 keystore's SHA-1

如果开发者需要在本地调试 SDKBoxPlay 相关的功能, 一样需要使用与 Google Play Console 相同的 Keystore.

如果不需要在本地调试，可以忽略此项.

运行命令 `keytool -list -v -keystore your.keystore` , 可以得到类型的如下结果, 请注意其中的 SHA1 :

```bash

...

Certificate fingerprints:
	 MD5:  09:F2:CA:99:6A:EF:8D:B7:17:B8:25:AE:36:40:9F:E2
	 SHA1: C7:4F:9C:6C:54:67:BC:81:27:25:40:EA:24:3D:B7:AA:1E:7A:7B:7D
	 SHA256: 92:51:09:9D:4A:A0:E5:4B:A8:6D:62:8B:3A:1B:F0:96:02:55:B9:1A:05:E4:68:32:0D:E1:F5:8A:A2:66:24:B1

...

```

## Server Auth Code

`web_client_id` 不是必须配置项

如果你想通过自己的服务器直接去访问 Google API, 你需要取得用户登录后的 Server Auth Code, 那么请在 `sdkbox_config.json` 中配置 `web_client_id`.

如果不需要, 可以忽略 `web_client_id`.

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


如果你不需要 server auth code 的话，请移除掉 `web_client_id`.

关于ServerAuthCode的[说明](https://developers.google.cn/identity/sign-in/android/offline-access)


