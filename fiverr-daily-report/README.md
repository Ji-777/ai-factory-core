# Fiverr Report Bot

Fiverr Report Bot is a Python automation tool that fetches your daily Fiverr sales data and emails it to you in a clean report format.

📬 Author: Lenox  
📧 Email: jx595127@gmail.com
🌐 **Language**: English first, 中文 follows

---

## Features

- Retrieves earnings and order summary from Fiverr
- Sends email summary report via SMTP
- Supports scheduled daily execution
- Configurable credentials and recipients
- Lightweight and easy to deploy

## Installation

1. Clone this repository  
2. Install Python 3.8 or above  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Edit `config.json` with your Fiverr cookie and email details. Then run:

```bash
python main.py
```

To automate daily reports, use Windows Task Scheduler or a cron job.

### Configuration

`config.json` format:

```json
{
  "fiverr_cookie": "your_cookie_here",
  "email": {
    "from": "your_email@gmail.com",
    "to": "recipient_email@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your_email@gmail.com",
    "password": "your_email_password"
  }
}
```

---

# Fiverr 日报助手

Fiverr Report Bot 是一个 Python 自动化工具，用于抓取你的 Fiverr 每日销售数据并以简洁的邮件形式发送给你。
📬 **作者**: Lenox  
📧 **邮箱**: jx595127@gmail.com  
🌐 **语言**: 英文优先，中文补充

---

## 功能亮点

- 获取 Fiverr 收入与订单概览
- 通过 SMTP 邮件发送日报
- 支持定时每日自动运行
- 可配置邮箱账号与收件人
- 部署简单，运行轻量

## 安装方法

1. 克隆本项目  
2. 安装 Python 3.8 或以上版本  
3. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方式

编辑 `config.json`，填入 Fiverr Cookie 和邮箱信息。运行：

```bash
python main.py
```

如需每天自动运行，请使用 Windows 任务计划或 Linux cron。

### 配置说明

`config.json` 示例格式：

```json
{
  "fiverr_cookie": "your_cookie_here",
  "email": {
    "from": "your_email@gmail.com",
    "to": "recipient_email@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "your_email@gmail.com",
    "password": "your_email_password"
  }
}
```

## License

MIT License. See [LICENSE](LICENSE) for more details.
