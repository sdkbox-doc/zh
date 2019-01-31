## 服务器认证

如果需要用开发者自己的服务器来作认证，可以按下面的步骤

### iOS

1. 实现 `SdkboxPlayListener` 中的 `onGenerateIdentityVerificationSignature`
2. 调用 `sdkbox::PluginSdkboxPlay::generateIdentityVerificationSignature();`

### Android

* 在 `sdkbox_config.json` 中添加 `web_client_id`
```json
    "sdkboxplay" : {
        "web_client_id": "......."
    }
```
web_client_id的生成可以参见这个[文档](https://developers.google.com/identity/protocols/OAuth2WebServer)

* 登录
* 调用 `sdkbox::PluginSdkboxPlay::getPlayerAccountField("server_auth_code")` 以获取 google server auth code

