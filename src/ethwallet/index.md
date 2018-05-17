[&#171; SDKBOX Home](http://sdkbox.com)

<h1>ETHWallet 插件</h1>

## 介绍

ETHWallet 是一个实现了以太坊支付的插件. (目前仅支持 `Cocos Creator` JS 工程)


## 样例工程

[github 上的一个样例](https://github.com/sdkbox/ETHWallet)

## 集成

在您确保正确安装了 SDKBOX Installer 的情况下，运行下面的命令来集成 SDKBOX ETHWallet 插件。

```bash
$ sdkbox import ethwallet -p `path/to/build/jsb-xxx`
```

## 插件使用

### 引入

creator 上有两种引入方式:

* 以非插件的方式引入 `ethwallet.js` (现在默认的方式), 当在代码中想要引用 `ETHWallet` 时，调用

```
const ETHWallet = require('../sdkbox/ethwallet/ethwallet');
const ethwallet = new ETHWallet();
```

* 以插件的方式引入 `ethwallet.js`, 当在代码中想要引用 `ETHWallet` 时，调用

```
const ethwallet = new ETHWallet();
```

### 初始化
初始化时需提供一个 `provider` , 这是一个以太坊的结点, 可以用 [Infura](https://infura.io/) 或 [Etherscan](https://etherscan.io/), 也可以搭建一个自己的结点.
```
const PROVIDER_URL = 'https://ropsten.infura.io/L3BRNAgKihyPmcyI1ESe';
ethwallet.init(PROVIDER_URL);
```

### 创建用户地址
创建或加载一个用户地址.

第一次的话, 这里会创建一个内部的用户地址, 已创建的话, 只会加载本地已保存的帐号信息.
传入的参数是 `DCPay` 内部保存用户地址的加密使用.
返回的地址应该在需要时展示给用户，以便用户支付到这个地址, 返回的私钥, 只能是开发者使用, 一定要小心保存.
```
const pw = 'password';
const acc = ethwallet.newAccountIf(pw);
```

### 检查帐号余额

```
ethwallet.getBalance(function(result){
    self.log(JSON.stringify(result));
}, this.acc.address);
```


## API

---
`ETHWallet` 初始化

参数: `providerURL`, 要联接到的区块结点 `URL`

```js
ETHWallet.init(providerURL)
```

---
设置 `ETHWallet` 的转帐 `Gas` 最大限额, 默认为 `21000`
```js
ETHWallet.setGasLimit(valueInWei)
```

---
创建或加载已创建的 `ETHWallet` 用户支付帐号
参数: `password`， 存储帐号的密码
```js
ETHWallet.newAccountIf(password)
```

---
提取用户帐号中的余额到传入的地址中

参数:

* `cb`, 结果回调
* `address`, 要提取到的地址, 开发者可传入自己的接收地址
* `valueInWei`, 要转移的数额, 默认为传出地址的所有余额
* `privateKey`, 要传出地址的私解, 默认为内部用户支付地址

```js
ETHWallet.remit(cb, address, valueInWei, privateKey)
```

---
查询帐号余额
参数:

* `cb`, 结果回调
* `address`, 要查询的帐号

```js
ETHWallet.getBalance(cb, address)
```

---
查询帐号余额
参数:

* `cb`, 结果回调
* `address`, 要提取到的地址, 开发者可传入自己的接收地址
* `valueInWei`, 要转移的数额, 默认为传出地址的所有余额
* `privateKey`, 要传出地址的私解, 默认为内部用户支付地址
* `includeGas`, `Gas`费用是否从 `valueInWei` 中扣除, 默认为单独扣

```js
ETHWallet.sendTransaction(cb, toAddr, valueInWei, privateKey, includeGas)
```


## 手动集成

将安装包目录下的

> `plugin/lib/a-ethwallet-polyfill-fore-cocos.js`,

> `plugin/lib/a-ethwallet-polyfill-fore-cocos.js.meta`,

> `plugin/lib/ethwallet.js`,

> `plugin/lib/ethwallet.js.meta`

拷贝到 `asset` 目录 `sdkbox/ethwallet` 下

在代码中调用
```xml
const ETHWallet = require('../sdkbox/ethwallet/ethwallet');
const ethwallet = new ETHWallet();
```


## 注意项

代码中的发送货币操作, 可以通过 `https://etherscan.io/` 来查询对应的交易.

