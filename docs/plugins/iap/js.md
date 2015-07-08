<!--
Include Base: /Users/niteluo/Projects/store/doc/en/src/iap/v3-cpp
-->

## 介绍
提供了一步集成IAP到cocos2d-x(c, lua, js)工程, __SDKBOX__ 极大地简化了集成sdk的过程.

## 集成

运行下面的命令来集成iap
```bash
sdkbox import iap
```

## 额外的步骤

### 修改 `<游戏所在Activity>.java`
* 在 `<游戏所在Activity>.java` 中添加下面的import:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* 在上面那个类中的 `onCreate(final Bundle savedInstanceState)` 函数中添加 `SDKBox.init(this);` 调用. 添加后的代码:
```java
protected void onCreate(Bundle savedInstanceState){
  super.onCreate(savedInstanceState);
  SDKBox.init(this);
}
```

* 对以下这几个函数中,添加对应的 SDKBox 接口调用,最后你的代码,应该像以下这样:
    * 如果你的类中,有些函数不存在,添加它
    * 如果你的类中,有些函数已经存在,那在其中添加对应的 SDKBox 相关接口调用

```java
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
          if(!SDKBox.onActivityResult(requestCode, resultCode, data)) {
            super.onActivityResult(requestCode, resultCode, data);
          }
    }
    @Override
    protected void onStart() {
          super.onStart();
          SDKBox.onStart();
    }
    @Override
    protected void onStop() {
          super.onStop();
          SDKBox.onStop();
    }
    @Override
    protected void onResume() {
          super.onResume();
          SDKBox.onResume();
    }
    @Override
    protected void onPause() {
          super.onPause();
          SDKBox.onPause();
    }
    @Override
    public void onBackPressed() {
          if(!SDKBox.onBackPressed()) {
            super.onBackPressed();
          }
    }
```

* 备注:

cocos2d-x v2中, `<游戏所在Activtiy>.java` 一般为 `proj.android/src/com/cocos/你的游戏/你的游戏.java`
cocos2d-x v3中, `<游戏所在Activtiy>.java` 一般为 `proj.android/src/org/cocos2dx/LANGUAGE/AppActivity.java`, LANGUAGE为cpp,lua或javascript


### 在游戏源码中调用 SDKBOX 的 IAP 接口

#### 1. 配置 `sdkbox_config.json`
* `sdkbox_config.json` 不存在:
      * 重命名插件中的 `sdkbox_config.json.sample` 为 `sdkbox_config.json`
      * 拷贝 `sdkbox_config.json` 到工程中的 __Resources__ 目录
      * XCode中,还需要把 `sdkbox_config.json` 文件拖到工程的资源文件中,确保这个文件会打包到你的ios应用中

* `sdkbox_config.json` 已经存在:
      * 把插件中的 `sdkbox_config.json.sample` 中的 `IAP` 项拷贝到你工程中的 `sdkbox_config.json` 中

* 修改 `sdkbox_config.json` 中的项为你自己的信息



#### 2 初始化 IAP
* 修改 `AppDelegate.cpp` 包括以下头文件:
```cpp
#include "PluginIAPJS.hpp"
#include "PluginIAPJSHelper.hpp"
```

* 修改 `AppDelegate.cpp` 注册IAP的JS绑定:
```cpp
sc->addRegisterCallback(register_all_PluginIAPJS);
sc->addRegisterCallback(register_all_PluginIAPJS_helper);
```

* 在你的代码中调用 `sdkbox.IAP.init();` 来完成初始化 (强烈推荐在 `app.js` 完成初始化)


#### 3 获取最新的商品信息
当你的游戏启动时,最好获取一次最新商品信息
要获取商品信息,可以调用 `sdkbox.IAP.refresh()`.

> `onProductRequestSuccess` 获取成功,会收到这个回调

> `onProductRequestFailure` 获取失败

#### 4 购买
购买调用接口 `sdkbox.IAP.purchase(name)`

__提示:__ __name__ 是你在 `sdkbox_config.json` 中的 `items` 项存放在的名字, 而不是你在 iTunes 或 GooglePlay Store 的商品名字

> `onSuccess` 购买成功.

> `onFailure` 购买失败.

> `onCanceled` 用户取消购买.

#### 5 恢复购买
恢复购买调用 `sdkbox.IAP.restore()`.

> `onRestored` 恢复成功

__Note:__ `onRestored` 这个回调可能不至只有一次

#### 6 处理购买事件
允许你接收处理游戏中 `IAP` 返回的各种事件

* 注册java script listener:
```Javascript
sdkbox.IAP.setListener({
    onSuccess : function (product) {
        //Purchase success
    },
    onFailure : function (product, msg) {
        //Purchase failed
        //msg is the error message
    },
    onCanceled : function (product) {
        //Purchase was canceled by user
    },
    onRestored : function (product) {
        //Purchase restored
    },
    onProductRequestSuccess : function (products) {
        //Returns you the data for all the iap products
        //You can get each item using following method
        for (var i = 0; i < products.length; i++) {
            // loop
        }
    },
    onProductRequestFailure : function (msg) {
        //When product refresh request fails.
    }
});
```


