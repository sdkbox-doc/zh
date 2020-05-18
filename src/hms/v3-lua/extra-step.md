### 修改 `AppActivity.java`

#### 插件版本 >= 2.4.0.3

1. 找到 __AppActivity.java__ 文件
```bash
find . -name "AppActivity.java"
```

2. 把 `extends Cocos2dxActivity` 替换为 `extends com.sdkbox.plugin.SDKBoxActivity`

以下是 __AppActivity.java__ 不同版本的引擎所在的目录：

```
cpp
  - proj.android/src/org/cocos2dx/cpp/AppActivity.java
  - proj.android-studio/app/src/org/cocos2dx/cpp/AppActivity.java
  - proj.android/app/src/org/cocos2dx/cpp/AppActivity.java ( from cocos2d-x 3.17)

lua
  - frameworks/runtime-src/proj.android/src/org/cocos2dx/lua/AppActivity.java
  - frameworks/runtime-src/proj.android-studio/app/src/org/cocos2dx/lua/AppActivity.java
  - frameworks/runtime-src/proj.android/app/src/org/cocos2dx/lua/AppActivity.java (from cocos2d-x 3.17)

js
  - frameworks/runtime-src/proj.android/src/org/cocos2dx/javascript/AppActivity.java
  - frameworks/runtime-src/proj.android/app/src/org/cocos2dx/javascript/AppActivity.java ( from cocos2d-x 3.17)
```

#### 插件版本 < 2.4.0.3

* 如果您使用 cocos2d-x 源代码，假设您在 `proj.android` 目录下，那么您可以在如下位置找到 `Cocos2dxActivity.java` 文件：

    ```
    ../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/
    lib/Cocos2dxActivity.java
    ```

* 如果您使用 cocos2dx-x 预编译库， 假设您在 `proj.android` 目录下，那么您可以在如下位置找到 `Cocos2dxActivity.java` 文件：

    ```
    ./src/org/cocos2dx/lib/Cocos2dxActivity.java
    ```

  __Note:__ 当你使用 cocos2d-x 源代码时，不同的版本中 `Cocos2dxActivity.java` 文件的位置也不同。一个确定该文件位置的方法是查看 `proj.android/project.properties` 。比如：
```
android.library.reference.1=../../cocos2d-x/cocos/platform/android/java
```

在这个例子中， `Cocos2dxActivity.java` 文件应该在如下位置：

```
../../cocos2d-x/cocos/platform/android/java/src/org/cocos2dx/lib/Cocos2dxActivity.java
```

* 修改 `Cocos2dxActivity.java` 文件，导入如下包：
```java
import android.content.Intent;
import com.sdkbox.plugin.SDKBox;
```

* 然后，修改 `Cocos2dxActivity` 类的 `onCreate(final Bundle savedInstanceState)` 函数，添加一个调用语句 `SDKBox.init(this);` 。添加的位置非常重要，必须在调用 `onLoadNativeLibraries();` 之后。如下：
```java
onLoadNativeLibraries();
SDKBox.init(this);
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
