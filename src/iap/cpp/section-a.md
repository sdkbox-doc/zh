

#### 2 初始化 IAP
* 在你的代码中调用 `sdkbox::IAP::init();` 来完成初始化 (强烈推荐在 `AppDelegate::applicationDidFinishLaunching()` 或 `AppController:didFinishLaunchingWithOptions()` 完成初始化)
* 在调用初始化的代码中,一定要包括如下头文件:
```cpp
#include "PluginIAP/PluginIAP.h"
```

#### 3 获取最新的商品信息
当你的游戏启动时,最好获取一次最新商品信息
要获取商品信息,可以调用 `sdkbox::IAP::refresh()`.

> `onProductRequestSuccess` 获取成功,会收到这个回调

> `onProductRequestFailure` 获取失败

#### 4 购买
购买调用接口 `sdkbox::IAP::purchase(name)`

__提示:__ __name__ 是你在 `sdkbox_config.json` 中的 `items` 项存放在的名字, 而不是你在 iTunes 或 GooglePlay Store 的商品名字

> `onSuccess` 购买成功.

> `onFailure` 购买失败.

> `onCanceled` 用户取消购买.

#### 5 恢复购买
恢复购买调用 `sdkbox::IAP::restore()`.

> `onRestored` 恢复成功

__Note:__ `onRestored` 这个回调可能不至只有一次

#### 6 处理购买事件
允许你接收处理游戏中 `IAP` 返回的各种事件

* 你可以继承这个类 `sdkbox::IAPListener`:
```cpp
    #include "PluginIAP/PluginIAP.h"
    class MyClass : public sdkbox::IAPListener
    {
    private:
        virtual void onSuccess(sdkbox::Product const& p) override;
        virtual void onFailure(sdkbox::Product const& p, const std::string &msg)
           override;
        virtual void onCanceled(sdkbox::Product const& p) override;
        virtual void onRestored(sdkbox::Product const& p) override;
        virtual void onProductRequestSuccess(std::vector<sdkbox::Product> const &products)
        override;
        virtual void onProductRequestFailure(const std::string &msg) override;
    }
```

* 创建上面类的实例,传到 `IAP` 中:
```cpp
sdkbox::IAP::setListener(listener);
```
