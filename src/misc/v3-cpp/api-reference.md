## API 文档

### 方法
```cpp
static bool init ( ) ;
```
>  初始化插件

```cpp
static void setListener ( MiscListener * listener ) ;
```
> 设置插件的 Listener

```cpp
static MiscListener * getListener ( ) ;
```
> 取插件的 Listener

```cpp
static void removeListener ( ) ;
```
> 删除 Listener

```cpp
static std::string localNotify ( const std::string & title, const std::string & content, int delaymisillensecond ) ;
```
> 发送一个本地消息
@return 消息的id

### Listeners
```cpp
void onHandleLocalNotify ( const std::string & payloadJson ) 
```

