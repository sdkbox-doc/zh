### 初始化 SdkboxAds
在您的代码的合适的位置初始化这个插件，我们建议您在 `AppDelegate:applicationDidFinishLaunching()` 或者 `AppController:didFinishLaunchingWithOptions()` 中进行初始化。并确保您的代码中包含了正确的头文件。举例如下：

```cpp
#include "PluginSdkboxAds/PluginSdkboxAds.h"
AppDelegate::applicationDidFinishLaunching()
{
     sdkbox::PluginSdkboxAds::init();
}
```

### 使用 SdkboxAds

#### 配置
SdkboxAds 是一个提供调控广告显示服务的插件。这意味着它将在运行时管理一堆在预先定义好的 AdUnit 。
它的配置分为两个部分：配置 AdUnits 以及 配置 Placement 。每一个 AdUnit 都是对一个Sdkbox 广告插件的映射。
举例如下：
<pre>
    "SdkboxAds": {
        "units": [
            "AdColony",
            "Fyber",
            "Chartboost",
            "Vungle"
        ]
    }
</pre>

Placement 则设定了对于某一个给定的 AdUnit 将会被显示的广告类型。一个完整的 SdkboxAds 配置文件的例子如下所示：

<pre>
    "SdkboxAds": {
        "units": [
                "AdColony",
                "Fyber",
                "Chartboost",
                "Vungle"
            ],
        "placements": [
            {
                "id" : "placement-1",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "AdColony",
                      "name": "video"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Default"
                    }
                ]
            },
            {
                "id" : "placement-2",
                "strategy" : "round-robin",
                "units" : [
                    {
                      "unit": "Vungle",
                      "name": "reward"
                    },
                    {
                      "unit": "AdColony",
                      "name": "v4vc"
                    },
                    {
                      "unit": "Chartboost",
                      "name": "Next Level"
                    }
                ]
            }
        ]
    }
</pre>

#### 使用

调用 `sdkbox::SdkboxAds::init()` 将完成 SdkboxAds 实例化并且开始管理所有的定义在配置文件里的 AdUnit 。

请求显示一个在默认的 AdUnit 中的默认广告，并以此完成一次简单的集成测试：
```cpp
sdkbox::SdkboxAds::playAd()
```

请求显示默认 AdUnit 中的广告：
```cpp
sdkbox::SdkboxAds::playAd( const std::string& zone_place_location );
sdkbox::SdkboxAds::playAd( const std::string& zone_place_location, const AdUnitParams& params );

// AdUnitParams is a typedef for std::map<std::string,std::string>
```
> 提示：每一个 AdUnit 都有自己的参数，可以参考每一个插件的文档。

请求显示一个指定的 AdUnit 中的广告：
```cpp
sdkbox::SdkboxAds::playAd(
        const std::string& ad_unit_name,
        const std::string& zone_place_location );

sdkbox::SdkboxAds::playAd(
        const std::string& ad_unit_name,
        const std::string& zone_place_location,
        const AdUnitParams& params );
```

请求显示定义在 sdkbox\_config.json 的 Placement 中的广告：
```cpp
sdkbox::SdkboxAds::placement( const str::string& placement );
```

更好的控制广告数据缓冲：
```cpp
sdkbox::SdkboxAds::cacheControl(
        const std::string& ad_unit,
        const std::map<std::string, std::string>& cacheOpts );
```
> 缓冲的选项是由 AdUnit 指定的， 请参考每个插件的相关文档。

### SdkboxAds 事件
这个插件允许您捕捉事件。

* 允许您自己的类继承 `sdkbox::SdkboxAdsListener` 并且覆盖（override）下列函数的实现：
```cpp
#include "PluginSdkboxAds/PluginSdkboxAds.h"
class MyClass : public sdkbox::SdkboxAdsListener
{
private:
    void onAdAction(
            const std::string& ad_unit_id,
            const std::string& zone_location_place_you_name_it,
            sdkbox::AdActionType action_type);

    void onRewardAction(
            const std::string& ad_unit_id,
            const std::string& zone_id,
            float reward_amount,
            bool reward_succeed);

};
```
> `sdkbox::AdActionType` 是一个枚举类型， 定义如下：

```cpp
    enum AdActionType {

        LOADED=0,           	// content loaded
        LOAD_FAILED,        	// content failed to load

        CLICKED,            	// clicked on content

        REWARD_STARTED,	 	// reward started
        REWARD_ENDED,       	// reward achieved
        REWARD_CANCELED,    	// reward aborted

        AD_STARTED,         	// start showing.
        AD_CANCELED,        	// start showing.
        AD_ENDED,           	// content shown

        ADACTIONTYPE_UNKNOWN	// mostly on error situations.

    };

```

* 创建一个 __listener__ 处理回调：
```cpp
sdkbox::PluginSdkboxAds::setListener( new MyClass() );
```
