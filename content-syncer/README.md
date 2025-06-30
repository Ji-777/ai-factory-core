# Content Distribution Syncer

Content Distribution Syncer is a CLI tool that helps you publish a single piece of content across multiple platforms. It works with Markdown or HTML files or a direct link and adapts the content format for each destination platform.

📬 **Author**: Lenox  
📧 **Email**: jx595127@gmail.com  
🌐 **Language**: English first, 中文 follows

---

## Features

- Distribute to Twitter, LinkedIn, Medium, Telegram, and Reddit
- Choose the platforms at runtime via command line
- Supports publishing templates with `{content}` placeholder
- Multiple account configurations via `config.json`
- Logs success or failure of each post to `log.txt`
- Modular platform architecture for easy expansion

## Installation

1. Clone this repository.
2. Install Python 3.8+.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Prepare a configuration file based on `config.json` with your own tokens and credentials.  
Then run the script:

```bash
python main.py --file mypost.md --platforms twitter linkedin reddit
```

You may also share a link instead of a file:

```bash
python main.py --link https://example.com/article --platforms telegram medium
```

Results are written to `log.txt`.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

# 内容分发同步器

Content Distribution Syncer 是一个 CLI 工具，帮助你将一篇内容自动分发到多个平台。支持 Markdown、HTML 文件或链接输入，并会为不同平台自动调整格式。

📬 **作者**: Lenox  
📧 **邮箱**: jx595127@gmail.com  
🌐 **语言**: 英文优先，中文补充

---

## 功能特点

- 支持分发到 Twitter、LinkedIn、Medium、Telegram 和 Reddit
- 可在运行时通过命令行选择平台
- 支持使用带有 `{content}` 占位符的发布模板
- 通过 `config.json` 配置多个账号信息
- 将发布结果记录到 `log.txt`
- 平台模块化架构，方便扩展其他平台

## 安装说明

1. 克隆本仓库  
2. 安装 Python 3.8+  
3. 安装依赖包：

```bash
pip install -r requirements.txt
```

## 使用方式

根据模板配置好你的 `config.json`，然后运行：

```bash
python main.py --file mypost.md --platforms twitter linkedin reddit
```

也可以直接分享链接：

```bash
python main.py --link https://example.com/article --platforms telegram medium
```

发布结果将记录在 `log.txt` 中。

## 开源协议

本项目基于 MIT 协议发布，详见 [LICENSE](LICENSE) 文件。
