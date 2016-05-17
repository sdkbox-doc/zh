![](SDKBOX_logo.png)


# SocialShare 插件文档

更多的信息，请访问我们的主页：[www.sdkbox.com](http://cocos2d-x.org/sdkbox)

## 集成 SDKBOX SocialShare

首先将 ```sdkbox_socialshare``` unity 包导入您的工程中。这将会在 Assets 目录下创建两个目录（Plugins 和 SDKBOX）。

![](socialshare_folder.jpg)

在开始使用 SocialShare 之前，在 Assets/SDKBOX/socialshare 目录下找到 SocialShare prefab 。

![](socialshare_folder_prelab.png)

在您想使用 SocialShare package 的场景中创建一个 SocialShare prefab 的实例。在任何时候，您只需要一个 prefab 的实例。

在 hierarchy 中选择 SocialShare 游戏对象，并且在您的 inspector pane 中您可以配置这个对象并且定制 SockalShare 对话框。

## 配置 SocialShare 插件

![](socialshare_config.png)

### 配置字段说明

##### Twitter Key IOS
这个字段定义了 ios 平台上的 twitter key, 如果为空，那么 twitter 不会显示在分享面板上。

##### Twitter Secret IOS
这个字段定义了 ios 平台上的 twitter secret, 如果为空，那么 twitter 不会显示在分享面板上。

##### Twitter Key Android
这个字段定义了 Android 平台上的 twitter key, 如果为空，那么 twitter 不会显示在分享面板上。

##### Twitter Secret Android
这个字段定义了 Android 平台上的 twitter secret, 如果为空，那么 twitter 不会显示在分享面板上。

##### facebook enable

这个字段指示是否要在分享面板上显示 facebook 。

##### Social Panel Title

这个字段设置分享面版的自定义标题。

##### Social Panel Cancel

这个字段定制分享面板上的取消按钮。

## 处理 SocialShare 事件

您可以在 SocialShare 脚本 inspector pane 中找到 ```Callbacks``` 项， 然后单击 ```+``` 添加一个回调，并指定想要触发的对象及方法。

![](callbacks.png)

## SocialShare API

```
void setSharePanelTitle(string s)
void setSharePanelCancel(string s)
void share(SocialShareInfo info)

```

## 手动集成

##### IOS 平台

- 在编译 ios 工程的时候，您需要在 info.plist 文件中插入以下内容，并且将 `280194012150923` 替换为您的 facebook app id 。


```
<key>FacebookAppID</key>
<string>280194012150923</string>
<key>FacebookDisplayName</key>
<string>helloworld - Test1</string>
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>fb280194012150923</string>
        </array>
    </dict>
</array>
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>fbapi</string>
    <string>fb-messenger-api</string>
    <string>fbauth2</string>
    <string>fbshareextension</string>
</array>
```

- 如果您使用的 unity 版本低于5.0， 您需要在 ios 工程编译配置的 `other linker flag` 项中添加 '-ObjC' 。

![](socialshare_ios_project_setting.png)

##### Android 平台

当编译 android, 您需要执行以下两步修改。

- 用您的 facebook app id 替换 `Assets/Plugins/Android/sdkbox\_facebook\_lib/AndroidManifest.xml` 文件中的 `280194012150923` 。

```
<provider android:authorities="com.facebook.app.FacebookContentProvider280194012150923"
            android:name="com.facebook.FacebookContentProvider"
            android:exported="true" />
```

- 用您的 facebook app id 替换 `Assets/Plugins/Android/sdkbox\_facebook\_lib/res/values/string.xml` 文件中的 `facebook\_app\_id` 的值。

```
<resources>
    <string name="facebook_app_id">280194012150923</string>
    ....
</resources>
```

<h2>Additional iOS Instructions</h2>
## 额外的 iOS 平台下的步骤
在一些低版本的 unity 中，在 SocialShare/Assets/Plugins/iOS 下的静态库文件不会被包含在 XCode 工程中。在这种情况下，您需要将它们移动到 Assets/Plugins/iOS 目录中或者手动添加它们到 XCode 工程中。
