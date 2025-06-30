# Shopify Inventory Sync

Shopify Inventory Sync is a Python script that automates syncing product inventory from a local CSV file to a Shopify store via the Admin API.

📬 **Author**: Lenox  
📧 **Email**: jx595127@gmail.com  
🌐 **Language**: English first, 中文 follows

---

## Features

- Parse local CSV inventory files  
- Update product quantities on Shopify by SKU match  
- Log success/failure to `log.txt`  
- Support dry-run preview mode  
- Allow custom column names

## Installation

1. Clone this repository  
2. Install Python 3.8+  
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Prepare your `inventory.csv` file and run:

```bash
python main.py --file inventory.csv --shop myshop.myshopify.com --token your_token
```

### Command-line Options

- `--file`: Path to local CSV file  
- `--shop`: Your Shopify store domain  
- `--token`: Shopify Admin API token  
- `--dry-run`: (Optional) Preview changes without updating  
- `--sku-col`, `--qty-col`: (Optional) Customize column names

### Example

Sample CSV:

```
sku,quantity
A1001,12
A1002,0
A1003,50
```

Result in `log.txt`:

```
[✓] A1001 updated to 12  
[✓] A1003 updated to 50  
[✗] A1002 not found on store
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

# Shopify 库存同步器

Shopify Inventory Sync 是一个 Python 脚本，用于将本地 CSV 文件中的库存数据同步到 Shopify 商店，使用的是 Shopify Admin API。

📬 **作者**: Lenox  
📧 **邮箱**: jx595127@gmail.com  
🌐 **语言**: 英文优先，中文补充

---

## 功能特点

- 解析本地库存 CSV 文件  
- 根据 SKU 更新 Shopify 上的商品库存  
- 成功或失败将记录在 `log.txt` 中  
- 支持 dry-run 模式预览更新效果  
- 支持自定义列名（如 SKU、库存数量）

## 安装步骤

1. 克隆本项目仓库  
2. 安装 Python 3.8+  
3. 安装依赖：

```bash
pip install -r requirements.txt
```

## 使用方式

准备好你的 `inventory.csv` 文件后运行：

```bash
python main.py --file inventory.csv --shop myshop.myshopify.com --token your_token
```

### 命令行参数说明

- `--file`：本地 CSV 文件路径  
- `--shop`：你的 Shopify 商店域名  
- `--token`：Shopify Admin API 访问令牌  
- `--dry-run`：（可选）仅预览变更  
- `--sku-col`, `--qty-col`：自定义列名（可选）

### 示例输入

```
sku,quantity
A1001,12
A1002,0
A1003,50
```

生成的 `log.txt` 内容：

```
[✓] A1001 updated to 12  
[✓] A1003 updated to 50  
[✗] A1002 not found on store
```

## 开源协议

本项目基于 MIT 协议开源，详见 [LICENSE](LICENSE)。
