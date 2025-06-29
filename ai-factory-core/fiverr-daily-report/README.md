# Fiverr Daily Report Generator

This Python script automates the generation of daily summary reports from Fiverr order data exported as CSV files.

## Features

- Parses Fiverr order CSVs
- Summarizes daily order count and revenue
- Groups orders by service type
- Outputs in Markdown or plain text
- Supports customization via command-line arguments

## Usage

```bash
python fiverr_report.py orders.csv --output daily_report.md --format markdown
```

### Command-line options

- `--output`: Output file name (default: `daily_report.md`)
- `--format`: Output format: `markdown` or `text`
- `--no-type-summary`: Disable service type breakdown
- `--date-col`, `--client-col`, `--amount-col`, `--service-col`: Customize column names

## Example

Sample input:
```
date,client name,amount,service type
2025-06-27,John Doe,$75,SEO Writing
2025-06-27,Jane Smith,$120,Logo Design
```

Generated output:
```markdown
## Fiverr Daily Report - 2025-06-27

**Total Orders**: 2  
**Total Revenue**: $195.00  
**Orders by Type**:
- SEO Writing: 1
- Logo Design: 1
```

## License

MIT License
