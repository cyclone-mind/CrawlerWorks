# JS 逆向工程案例集合

简体中文 | [English](README_en_us.md)

## 项目简介

本项目收集了常见的 JavaScript 逆向工程案例，包括加密算法分析、代码混淆处理等实例。

## 系统要求

- 操作系统：Ubuntu（Linux）
- Node.js 环境

## 技术栈

- Node.js
- @babel/parser
- @babel/traverse
- @babel/generator
- @babel/types
- crypto-js

## 功能特性

- AST分析与转换
- 加密算法还原
- 代码混淆处理
- 请求参数分析

## 使用说明

```bash
# 安装依赖
node --version ## 22.04
npm install
python --version ## 3.9
pip install -r requirements.txt
```

## 案例列表

| 案例名称 | 说明 | 难度 | 相关文件 |
|---------|------|------|----------|
| 基础代码 | 常用加密解密示例 | ⭐️ | [查看](/JS%20Reverse/00%20code/) |
| 福建电子交易平台 | 参数加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/01%20福建电子交易平台/) |
| 数位观察 | 参数加密分析 | ⭐️ | [查看](/JS%20Reverse/02%20数位观察/) |
| 全国建筑市场监管平台 | 请求参数处理 | ⭐️⭐️ | [查看](/JS%20Reverse/03%20全国建筑市场监管公共服务平台/) |
| 极志愿 | 登录加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/04%20极志愿/) |
| 优志愿 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/05%20优志愿/) |
| 吉林长春产权交易中心 | 请求参数加密 | ⭐️ | [查看](/JS%20Reverse/06%20吉林长春产权交易中心/) |
| 阿尔法 | 复杂环境模拟 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/07%20阿尔法/) |
| 中远 | 请求参数加密 | ⭐️⭐️ | [查看](/JS%20Reverse/08%20中远/) |
| 五矿 | 环境模拟与加密 | ⭐️⭐️ | [查看](/JS%20Reverse/09%20五矿/) |
| 蜂鸟竞技 | 复杂加密分析 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/10%20蜂鸟竞技/) |
| 补环境案例 | JS环境模拟技巧 | ⭐️⭐️ | [查看](/JS%20Reverse/11%20补环境/) |
| 抖音 | 签名算法分析 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/12%20抖音/) |
| 喜马拉雅 | 登录加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/13%20喜马拉雅/) |
| Subprocess模块 | Python与JS交互 | ⭐️ | [查看](/JS%20Reverse/14%20subprocess模块/) |
| Webpack分析 | 前端打包逆向分析 | ⭐️⭐️ | [查看](/JS%20Reverse/16%20webpack/) |
| 瑞数案例 | 指纹与算法分析 | ⭐️⭐️⭐️⭐️ | [查看](/JS%20Reverse/17%20瑞数案例/) |
| Hook案例 | JS Hook技术实践 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/18%20hook案例/) |
| 无限debugger案例 | 反调试对抗技术 | ⭐️⭐️ | [查看](/JS%20Reverse/19%20无限debugger案例/) |
| 艺恩数据 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/20%20艺恩数据/) |
| 同花顺 | 行情数据加密 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/22%20同花顺/) |
| 看准网 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/23%20看准网/) |
| 天翼云 | 登录认证分析 | ⭐️⭐️ | [查看](/JS%20Reverse/24%20天翼云/) |
| Drission案例 | 自动化工具应用 | ⭐️ | [查看](/JS%20Reverse/25%20drission%20page案例/) |
| 点点数据 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/26%20点点数据/) |
| 欧科区块链 | 区块链数据分析 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/27%20欧科区块链/) |
| 财联社 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/28%20财联社/) |
| 沃邮箱 | 登录认证分析 | ⭐️⭐️ | [查看](/JS%20Reverse/29%20沃邮箱/) |
| 丁香医生 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/30%20丁香/) |
| 全国招标公告 | 参数加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/31%20全国招标公告/) |
| B站播放量分析 | Cookie逆向分析 | ⭐️⭐️ | [查看](/JS%20Reverse/32%20B站刷播放--cookie逆向/) |
| AST分析 | 语法树转换技术 | ⭐️⭐️⭐️ | [查看](/JS%20Reverse/33%20AST/) |
| 竞技世界登录 | 登录认证分析 | ⭐️⭐️ | [查看](/JS%20Reverse/34%20竞技世界登录-/) |
| 安居客登录 | 登录认证分析 | ⭐️⭐️ | [查看](/JS%20Reverse/35%20安居客登录/) |
| 丰巢 | 滑块分析 | ⭐️⭐️ | [查看](/JS%20Reverse/36%20丰巢/) |
| 全国政策大数据平台 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/41%20全国政策大数据平台/) |
| 链家 | 数据加密分析 | ⭐️⭐️ | [查看](/JS%20Reverse/45%20链家/) |

## 注意事项

- 本项目仅用于学习研究
- 请遵守相关法律法规
- 不得用于非法用途

## 许可证

MIT License - 查看 [LICENSE](LICENSE) 文件了解更多信息。

## 贡献指南

欢迎提交 Issue 和 Pull Request。

## 联系方式

- 作者：Shouyu Zhou
- GitHub：[CycloneMind](https://github.com/CycloneMind/)
- Mail: [zhousy953933@gmail.com](zhousy953933@gmail.com)
