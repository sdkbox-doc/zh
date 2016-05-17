[&#171; SDKBOX Home](http://sdkbox.com)

<h1>Share 插件</h1>

## 介绍
您可以访问 [这里](http://www.cocos2d-x.org/sdkbox/share) 取更多关于插件的细节。

## Facebook 支持
if you want to use Facebook share on SocialShare Plugin, please follow these two steps:
如果您想使用 SocialShare 插件的分享到 Facebook 功能，请按照以下两个步骤进行配置：

1. 在您的工程根目录运行 `sdkbox import facebook`。
    这条命令将会把 Facebook 插件导入安装到您的工程中。Facebook 插件的安装还需要一些额外的步骤，请参考 [这里](http://docs.sdkbox.com/en/plugins/facebook/v3-cpp/#extra-steps) 完成安装配置。

2. 添加 Facebook 到 SocialShare 插件的 platforms 配置项中。如下所示：

```

"android": {
        "Facebook": {
            "debug": false
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "nlmUdPNcFGLWhyLu9cD794EDuDrVQnjd0YjTpB6sX8oHIQRrne",
                        "key": "EuovpLL0UhSGB7Jv5eKFJNMqO"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    },
    "ios": {
        "Facebook": {
            "debug": true
        },
        "Share": {
            "platforms": {
                "Twitter": {
                    "params": {
                        "secret": "haVcKarM96Sr4390XLQoHjyRUSyuHdkMX6letcc38h8TOWyiR9",
                        "key": "BUJTV6NEM7BAhhm82B12VbKGy"
                    }
                },
                "Facebook": {}    //support facebook share
            }
        }
    }

```


<<[../shared/guides.md]


## 样例工程

[github 上的一个样例](https://github.com/sdkbox/sdkbox-sample-share)
