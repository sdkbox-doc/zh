[&#8249; Misc Doc Home](./)

<h1>Misc 集成向导</h1>
<<[../../shared/-VERSION-/version.md]

## 集成

打开终端, 在其中输入以下命令来安装 SDKBox Misc 插件.
```bash
$ sdkbox import misc
```

### iOS额外修改

文件改动列表:

__Note__: 以下所有改动都以 diff 形式展示相应的修改, 在不同的版本上可能会有细微差异

- `proj.ios_mac/ios/AppController.mm`
```diff

  #import "RootViewController.h"

+ #include "PluginMisc/PluginMisc.h"

  @implementation AppController


  - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
      ...
      //run the cocos2d-x game scene
      app->run();

+     if (launchOptions[UIApplicationLaunchOptionsLocalNotificationKey]) {
+         [self handleLocalNotification:launchOptions[UIApplicationLaunchOptionsLocalNotificationKey]];
+     }

      return YES;
  }
  
+ - (void)application:(UIApplication *)application didReceiveLocalNotification:(UILocalNotification *)notification {
+     [self handleLocalNotification:notification.userInfo];
+ }
+ 
+ - (void)handleLocalNotification:(NSDictionary *)payloadDic {
+     NSError *error = nil;
+     NSData *jsonData = [NSJSONSerialization dataWithJSONObject:payloadDic
+                                                        options:0
+                                                          error:&error];
+     if (nil != jsonData) {
+         NSString *jsonString = [[NSString alloc] initWithData:jsonData encoding:NSUTF8StringEncoding];
+         sdkbox::PluginMisc::handleLocalNotify([jsonString UTF8String]);
+     } else {
+         NSLog(@"Error:%@", error);
+     }
+ }
  
  - (void)applicationWillResignActive:(UIApplication *)application {

```

### Android 额外修改

文件改动列表:

- proj.android/app/src/org/cocos2dx/cpp/AppActivity.java

    this should be your app activity java file
```diff
  package org.cocos2dx.cpp;

+ import android.content.Intent;
  import android.os.Bundle;
  import org.cocos2dx.lib.Cocos2dxActivity;

- public class AppActivity extends Cocos2dxActivity {
+ public class AppActivity extends com.sdkbox.plugin.SDKBoxActivity {

      @Override
      protected void onCreate(Bundle savedInstanceState) {
              return;
          }
          // DO OTHER INITIALIZATION BELOW

+         com.sdkbox.plugin.PluginMisc.onHandleNotification(getIntent());
          
      }

+     @Override
+     protected void onNewIntent(Intent intent) {
+         super.onNewIntent(intent);
+         com.sdkbox.plugin.PluginMisc.onHandleNotification(intent);
+     }

  }
```

-proj.android/app/AndroidManifest.xml

    add `singleTask` to your activity
```diff
              android:screenOrientation="landscape"
              android:configChanges="orientation|keyboardHidden|screenSize"
              android:label="@string/app_name"
              android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
+             android:launchMode="singleTask" >
              <intent-filter>
                  <action android:name="android.intent.action.MAIN" />

```

### JSON 配置

SDKBox 安装会自动插件一个配置信息到 `sdkbox_config.json` 中, 目前只需要保持 Misc 配置为空就好, 如下:

```json

{
    "ios": {
        "Misc":{
        }
    },
    "android": {
        "Misc":{
        }
    }
}

```

## 用法
<<[usage.md]

<<[api-reference.md]

<<[manual_integration.md]

<<[manual_ios.md]

<<[manual_android.md]

<<[proguard.md]
