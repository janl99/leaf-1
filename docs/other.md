# 其他问题

这里说明一些关于 `Leaf` 的其他问题。

1. 项目的名称为什么有 `leaf` 和 `wxleaf` 两个版本呢？

项目开发时没有考虑到在 `Pypi` 上 *leaf* 这个名称已被占用，而项目与微信相关，于是便添加了 *wx* 作为前缀。所以您可以叫它 `wxleaf` ，在安装之后的调用使用 `leaf` 即可。



2. 项目为什么需要如此新的 `Python` 版本？

项目完全使用了 `TypeHinting` 的代码提示特性，而这个特性在 `Python3.6+` 的版本才被完全支持，所以我们才需要新的版本支持；

当然，我相信对大家来说安装 `Python3.6+` 不算难事，毕竟都2020年了。



3. 我可以去哪里反馈问题？

您可以到项目的 [GitHub 代码仓库](https://github.com/guiqiqi/leaf) 通过 Issue 的方式提交问题，记得查看 Issue 的模板，确保自己的提问符合要求，也方便我第一时间跟进。