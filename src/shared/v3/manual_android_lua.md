把 `plugin/luabindings` 文件夹中所有的头文件和源文件都拷贝到你的工程的 `Classes` 文件夹中.

把你刚刚拷贝的 `.cpp` 文件添加到 `Android.mk` 文件的的 __LOCAL_SRC_FILES__ 项.比如
```
LOCAL_SRC_FILES := hellocpp/main.cpp \
                ../../Classes/AppDelegate.cpp \
                ../../Classes/HelloWorldScene.cpp \
								../../Classes/NewSourceFile.cpp
```
