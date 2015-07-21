### 修改 `Cocos2dxActivity.java`
* 如果你用的是 cocos2d-x 源码, 假定你当前在 `proj.android` 目录, 那么`Cocos2dxActivity.java` 的路径在这个位置:

    ```
    ../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/
    lib/Cocos2dxActivity.java
    ```

* 如果你用的是预编译的 cocos2d-x 库, 假定你当前在 `proj.android`, 那么 `Cocos2dxActivity.java` 的路径在这个位置:

    ```
    ./src/org/cocos2dx/lib/Cocos2dxActivity.java
    ```

  __注意:__ 当使用 Cocos2d-x 源码时,不同版本的 `Cocos2dxActivity.java` 在不同的路径. 有一个方法就是去看 `proj.android/project.properties`. 比如:
```
android.library.reference.1=../../cocos2d-x/cocos/platform/android/java
```

如上, `Cocos2dxActivity.java` 的路径应该是在:

```
../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxActivity.java
```

* 修改 `Cocos2dxActivity.java` 包含如下imports:
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* 然后, 修改 `Cocos2dxActivity` 中的 `onCreate(final Bundle savedInstanceState)` 函数, 在其中调用 `SDKBox.init(this);`. 这个函数调用的位置很重要. 它必须在 `onLoadNativeLibraries();` 之后调用. 比如:
```java
onLoadNativeLibraries();
SDKBox.init(this);
```

* 最后, 我们需要插入 __overrides__ 属性. 这里有几个规定.
    * 如果以下方法不存在,那么就添加它.

    * 如果以下方法已经定义了,那么在其中添加调用 `SDKBox` 的相关的接口.
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
