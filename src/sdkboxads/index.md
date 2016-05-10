[&#171; SDKBOX Home](http://sdkbox.com)

<h1>SdkboxAds 插件</h1>

## 介绍
尽管 Sdkbox 对很多广告插件提供了开箱即用式的便捷支持，但 Sdkbox 还提供了一种叫做 SdkboxAds 的容器插件可以方便的管理这些广告插件。它就像一个集中管理不同广告插件的 __管理者__ ，但与此同时其中的每个广告插件还可以独立的连向自己的后端。

![](../../imgs/sdkbox-ads-1.jpg?1)

相比直接使用任何广告插件平台，使用 SdkboxAds 是一种替代的方式。SdkboxAds 支持视频广告， 奖励式广告以及定义 placements 。在深入了解 SdkboxAds 之前，必须阐述一些概念。

### AdUnit
一个 AdUnit 是指能够被 SdkboxAds 管理的任何插件。比如 AdColony，Vungle 或者 Chartboost 都是 AdUnit 。
AdUnit 对已经存在的广告插件做了一个封装并且将它们用一个通用的接口表现出来。没错，您可以通过统一的代码形式来管理所有的 AdUnit 。
每一个 AdUnit 在配置形式上都表现为不同元素的集合，比如 interstitial，videos 或者 rewards 。比如 AdColony 定义了 zones , Chartboost 定义了 locations 以及 Vungle 定义了 places 。所有的这些概念其实都一样：是一种广告类型的名字。

### Placement
一个 Placement 是一组 AdUnit 和 name 键值对的集合。它用所声明的方式调控不同的 AdUnits 显示。
比如，一个 placement 可能像这样：

<pre>
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
          "name": "interstitial"
        }
      ]
    },
   …
]
</pre>

每当这个 Placement 被触发，它都会用 round-robin 的方式去显示每一个定义的 AdUnit 。在任何环境下，任何 AdUnit 如果广告数据没有缓冲完成，那么下一个 AdUnit 将会被显示。如果没有一个 AdUnit 的广告数据缓冲完成，那么什么都不会显示。
现在唯一支持的显示策略只有 “round-robin”，但不久后会支持更多的显示策略。
不需要对某一个 AdUnit 处理自有的概念, 比如 zone, location 或者 place （Fyber 插件）。针对这些， SdkboxAds 插件将统一用 `INTERSTITIAL`， `REWARDED`， `VIDEO` 或者 `BANNER` 来表示广告类型。

### 默认的 AdUnit
定义在 units 列表第一个的 unit 将会被当作 SdkboxAds 的默认 AdUnit 。

<<[../shared/guides.md]


## 样例工程

* [github 上的一个使用 cocos2d-x v3.x 的样例](https://github.com/sdkbox/sdkbox-sample-sdkboxads)
