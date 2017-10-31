
## Promotion IAP

### 启用 Promotion IAP

如果你想使用 iOS Promoting IAP 的话:

1. 实现 `IAPListener` 中的 `onShouldAddStorePayment`.
2. 在 `itunes connect` 网页中做相关配置

现在在 `onShouldAddStorePayment` 中，我们默认返回 true. 所以每次用户在 store 中点击，都会弹出购买提示。
如果你的应用有存在需要取消购买或延迟购买的情况，你需要在这个回调中实现自己的逻辑来返回 true 或 false.

### Promotion IAP 设置

你可以设置 promotion iap 商品在不同手机显示不同的商品，或以不同的顺序显示:

1. `static void updateStorePromotionOrder(const std::vector<std::string>& productNames)`;
2. `static void updateStorePromotionVisibility(const std::string& productName, bool visibility)`;
3. `static void fetchStorePromotionOrder()`;
4. `static void fetchStorePromotionVisibility(const std::string& productName)`;

更多详情见[Promoting IAP 官方文档](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html)
