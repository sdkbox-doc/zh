### 修改 `project.properties`
添加 __Google Play Services__ Android 库引用, 其路径因你的配置而有所不同.
并且 __Google Play Services__ 不是默认下载的, 您需要打开 __sdk installer__ ， 选择 __extras->google play services__ 下载并安装。例子:
```
android.library.reference.1=
../android/sdk.latest/extras/google/google_play_services/libproject/
google-play-services_lib
```

__注意:__ 如果已经存在 `android.library.reference.1`, 您可以递增数字, 例如 `android.library.reference.2`, 等等.

