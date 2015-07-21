### 修改 `<YourGameName>.java`
* 修改 `proj.android/src/<package identifier>/<YourGameName>.java` 去添加如下imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* 然后, 修改这个类中的函数 `onCreate(final Bundle savedInstanceState)` ,在其中添加 `SDKBox.init(this);` 这个调用. 你的修改应该和如下差不多:
```java
protected void onCreate(Bundle savedInstanceState){
  super.onCreate(savedInstanceState);
  SDKBox.init(this);
}
```

* 最后, 我们需要添加 __overrides__ 修饰. 这儿有几个规则.
    * 如果这个方法不存在,那么就添加它.

    * 如果这个方法已经存在了,那么就在方法中添加 `SDKBox` 相关的调用.
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
