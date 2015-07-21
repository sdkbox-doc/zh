### 修改 `<YourGameName>.java`
* 修改 `proj.android/src/<package identifier>/<YourGameName>.java` 文件，导入如下包：
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* 然后，修改您的类 `onCreate(final Bundle savedInstanceState)` 函数，添加一个调用语句 `SDKBox.init(this)` 。如下：
```java
protected void onCreate(Bundle savedInstanceState){
  super.onCreate(savedInstanceState);
  SDKBox.init(this);
}
```

* 最后, 我需要提供合适的 __overrides__ 方法的代码。这里有一些约定如下。
    * 如果这个被列出的方法没有在 `SDKBox` 中定义，那么__定义它__。

    * 如果这个被列出的方法已经被定义在 `SDKBox` 中，那么请调用这个在 `SDKBox` 中的__同名方法__。
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
