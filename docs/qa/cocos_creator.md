#SDKBOX Cocos Creator 插件使用指南

##安装

自 Cocos Creator 1.4 版本以后，Cocos用户可以直接从插件商店安装SDKBOX插件

<iframe src='https://gfycat.com/ifr/ConsciousSomberGerenuk' frameborder='0' scrolling='no' width='640' height='360' allowfullscreen></iframe>


当 SDKBOX 插件安装成功之后，就可以在系统菜单里面找到 "SDKBOX"

![](../imgs/ccc_tutorial_sdkbox_menu.png)

##集成SDK

在开始集成 SDKBOX 插件之前，必须先用 Cocos Creator 生成iOS/Android项目

<iframe src='https://gfycat.com/ifr/EntireLinearBeetle' frameborder='0' scrolling='no' width='640' height='360' allowfullscreen></iframe>


##使用指南

当SDKBOX集成完成之后，你就可以开始使用SDK的API了，这里将以Admob作为示例

### 添加按钮控件

首先在场景里面添加两个按钮控件
![](../imgs/ccc_tutorial_ui_design.png)

### 添加JS脚本

创建一个名为 “Admob.js” 的脚本，并且添加以下函数，记得要在“onLoad”函数中初始化Admob

```js
cc.Class({

    ...

    onLoad: function () {
        //Add this line to onLoad
        this.admobInit();
    },

    ...

    admobInit: function() {
        //finish it after import admob, let it empty for now
    },

    cacheInterstitial: function() {
        //finish it after import admob, let it empty for now
    },

    showInterstitial: function() {
        //finish it after import admob, let it empty for now
    },

    ...

});
```

### 添加脚本到场景里

![](../imgs/ccc_tutorial_canvas_script.png)

### 关联按钮事件

![](../imgs/ccc_tutorial_btn_cache_script.png)
![](../imgs/ccc_tutorial_btn_show_script.png)

### 配置AdMob

* 根据Admob账号修改以下文件 `./build/jsb-default/res/sdkbox_config.json`

### 完整的 AdMob.js 代码

```js
cc.Class({

    ...

    admobInit: function() {
        if(cc.sys.isMobile) {
            var self = this
            sdkbox.PluginAdMob.setListener({
                adViewDidReceiveAd: function(name) {
                    self.showInfo('adViewDidReceiveAd name=' + name);
                },
                adViewDidFailToReceiveAdWithError: function(name, msg) {
                    self.showInfo('adViewDidFailToReceiveAdWithError name=' + name + ' msg=' + msg);
                },
                adViewWillPresentScreen: function(name) {
                    self.showInfo('adViewWillPresentScreen name=' + name);
                },
                adViewDidDismissScreen: function(name) {
                    self.showInfo('adViewDidDismissScreen name=' + name);
                },
                adViewWillDismissScreen: function(name) {
                    self.showInfo('adViewWillDismissScreen=' + name);
                },
                adViewWillLeaveApplication: function(name) {
                    self.showInfo('adViewWillLeaveApplication=' + name);
                }
            });
            sdkbox.PluginAdMob.init();
        }
    },

    cacheInterstitial: function() {
        if(cc.sys.isMobile) {
            sdkbox.PluginAdMob.cache('gameover');
        }
    },

    showInterstitial: function() {
        if(cc.sys.isMobile) {
            sdkbox.PluginAdMob.show('gameover');
        }
    },

    ...

});
```

### 重新编译项目

* iOS: 使用Xcode打开 `./build/jsb-default/frameworks/runtime-src/proj.ios_mac/SDKBoxTutorial.xcodeproj`
* Android: 在 `./build/jsb-default` 目录下运行 `cocos run -p android `

![](../imgs/ccc_tutorial_admob_intistial_show.png)

