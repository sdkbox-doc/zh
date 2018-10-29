### iOS 工程的手动集成

将如下 framework 拷到 iOS 工程目录下，并将它添加到 Xcode 中

> sdkbox.framework

> PluginMisc.framework

如果你的工程中没有包含如下系统 framework, 你还需要添加它们:

> SystemConfiguration.framework

以下是文件修改列表:

- proj.ios_mac/ios/AppController.mm

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

