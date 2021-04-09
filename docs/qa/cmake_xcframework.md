<h1>FAQ</h1>

## CMake XCFramework

现在 CocosCreator 3+ 已经使用 CMake 来作 iOS/Android 工程的生成与编译.

但是 CMake 还不支持直接链接 XCFramework , 所以我们目前还是链接到 XCFramework 中特定的工程. 现在我们是默认链接到 `ios-i386_x86_64-simulator` 架构.

当你想链接到其它架构时, 需要手动修改一下 CMakeLists.txt 中引用的架构.

请查看文件 `$CreatorProjectRoot/native/engine/ios/CMakeLists.txt`

这里的代码显示, 库 ${LIB_NAME} 是链接到 ios simulator i386/x86_64 架构.
```CMake

LinkXCFramework("${CMAKE_CURRENT_LIST_DIR}/Firebase/FirebaseAnalytics/FirebaseCore.xcframework" ios-i386_x86_64-simulator ${LIB_NAME})

```

现在库就是链接到 ios 设备 armv7/arm64
```CMake

LinkXCFramework("${CMAKE_CURRENT_LIST_DIR}/Firebase/FirebaseAnalytics/FirebaseCore.xcframework" ios-armv7_arm64 ${LIB_NAME})

```

这里架构的名字其实来源于 `${CMAKE_CURRENT_LIST_DIR}/Firebase/FirebaseAnalytics/FirebaseCore.xcframework` 对应的子文件夹名字. 请根据你的实际情况作对应修改替换.

### 另一种方案

当然你也可以在生成后的 Xcode 工程中, 直接引用 XCFramework 库, 这样不用修改 `CMakeLists.txt` . 这时你应该把 CMakeLists.txt 中 `LinkXCFramework(*/*.xcframework ios-i386_x86_64-simulator ${LIB_NAME})` 的调用都去掉, 以免冲突.

同时也要注意, Xcode 工程其实是生成的, 在 Creator 中, 每次的生成工程操作, 都有可能会覆盖掉直接在 Xcode 作的修改.


[CMake XCFramework Issue](https://gitlab.kitware.com/cmake/cmake/-/issues/21752)

