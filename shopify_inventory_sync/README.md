# Shopify Inventory Sync

This Python script automates the synchronization of product inventory between a local CSV file and a Shopify store using the Shopify Admin API.

Features
- Parses local CSV inventory files
- Updates product quantities on Shopify by matching SKU
- Logs updated items and failures to log.txt
- Supports dry-run mode for previewing changes
- Customizable column mapping

Installation
Install Python 3.8+ and clone the repository. Then install dependencies:

pip install -r requirements.txt

Usage
Prepare your inventory.csv file and run the script with your credentials:

python main.py --file inventory.csv --shop myshop.myshopify.com --token your_token

Command-line options
--file: Path to local CSV file  
--shop: Your Shopify store domain  
--token: Shopify Admin API access token  
--dry-run: Optional, shows what would be updated without making changes  
--sku-col, --qty-col: Customize column names (optional)

Example
Sample input:

sku,quantity  
A1001,12  
A1002,0  
A1003,50  

Generated output (log.txt):

[✓] A1001 updated to 12  
[✓] A1003 updated to 50  
[✗] A1002 not found on store

License  
MIT License
