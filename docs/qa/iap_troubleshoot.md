
# IAP 常见问题

## Android In-App Billing

> Google 支付初始化失败, 支付对话框未弹出

可能有如下原因:

1. 国内的 Google 相关服务一般都是单独安装的. 这时需要确保 Google 服务有相应的权限. 以及允许后台运行.
2. 支付需要确保 Google 帐号已登录.


## iOS In-App Purchase

> 出现这一行 `IAP :WARNING!, Products size is 0` log 信息

可能有如下原因:

* iTunes Connect -> Agreements, Tax, and Banking -> Master Agreements -> Paid Applications-> Contact Info / Bank Info / Tax Info , 将税务信息填好.

* 检查 sdkbox_config.json 文件

```json
"ios" :
{
    "iap":{
        "items":{
            "remove_ads":{
                "id":"<这里是你在 iTunes Connect 中的配置的 IAP 商品的 Product id>"
            }
        }
    }
}
```

![](../imgs/iap_products_id.png)

* 将 Xcode -> Capablities -> In-App Purchase 打开

## iOS requestUpdateTransaction 没有回调

尽早初始化 IAP 

```
sdkbox::IAP::setListener(new your_iap_listener());
sdkbox::IAP::init();
``` 