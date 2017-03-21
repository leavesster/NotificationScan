# NotificationScan

## You should know

该文件适合还在iOS 9以下的项目使用。
原因：iOS 9，apple对NSNotificationCenter进行了处理，不再需要自行remove，所以适配iOS 9及其以上系统，无需担心这个。

> n OS X 10.11 and iOS 9.0 NSNotificationCenter and NSDistributedNotificationCenter will no longer send notifications to registered observers that may be deallocated. 

from [Foundation Release Notes](https://developer.apple.com/library/content/releasenotes/Foundation/RN-Foundation/index.html#10_11NotificationCenter)

## How To Get Started

需要安装python3。
如果没有，请使用 `brew install python3` 。
什么？你不知道brew？ 屠龙宝刀，点就送[brew](https://brew.sh/index_zh-cn.html)

1. 使用Xcode打开scan.py文件。
2. 在root_path1 = 'absolute project path'，把absolute project path 替换成 需要扫描项目的绝对地址。
3. 打开terminal 输入 `cd path`，进入python文件的地址，不进入也可以，只是影响log文件存储的位置，执行 `python3 notificationScan.py`。输出内容会在当前terminal的目录保存一份log文件，直接查看内warning 关键字即可。

### To Do

* 支持一个实现文件下多个类的情况。
