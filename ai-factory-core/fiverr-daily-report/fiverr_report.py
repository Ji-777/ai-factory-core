from core_sdk.config import settings
from core_sdk.logger import get_logger
from core_sdk.utils import some_helper_function

logger = get_logger(__name__)

import argparse
import csv
from collections import defaultdict


def read_orders(csv_file, date_col, client_col, amount_col, service_col):
    orders = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = row.get(date_col, '').strip()
            client = row.get(client_col, '').strip()
            amt_raw = row.get(amount_col, '0').strip().replace('$', '').replace(',', '')
            try:
                amount = float(amt_raw)
            except ValueError:
                amount = 0.0
            service = row.get(service_col, '').strip()
            orders.append({'date': date, 'client': client, 'amount': amount, 'service': service})
    return orders


def summarize_orders(orders):
    summary = {}
    for order in orders:
        d = order['date']
        s = summary.setdefault(d, {'total_orders': 0, 'total_revenue': 0.0, 'by_service': defaultdict(int), 'details': []})
        s['total_orders'] += 1
        s['total_revenue'] += order['amount']
        s['by_service'][order['service']] += 1
        s['details'].append(order)
    return summary


def render_markdown(date, data, include_type=True):
    lines = [f"## Fiverr Daily Report - {date}", ""]
    lines.append(f"**Total Orders**: {data['total_orders']}  ")
    lines.append(f"**Total Revenue**: ${data['total_revenue']:.2f}  ")
    if include_type:
        lines.append("**Orders by Type**:")
        for service, count in data['by_service'].items():
            lines.append(f"- {service}: {count}")
    lines.append("\n**Details**")
    lines.append("| Time | Client Name | Amount | Service Type   |")
    lines.append("|------|-------------|--------|----------------|")
    for o in data['details']:
        lines.append(f"| {o['date']} | {o['client']} | ${o['amount']:.2f} | {o['service']} |")
    return "\n".join(lines)


def render_text(date, data, include_type=True):
    lines = [f"Fiverr Daily Report - {date}"]
    lines.append(f"Total Orders: {data['total_orders']}")
    lines.append(f"Total Revenue: ${data['total_revenue']:.2f}")
    if include_type:
        lines.append("Orders by Type:")
        for service, count in data['by_service'].items():
            lines.append(f"  {service}: {count}")
    lines.append("Details:")
    lines.append("Time\tClient Name\tAmount\tService Type")
    for o in data['details']:
        lines.append(f"{o['date']}\t{o['client']}\t${o['amount']:.2f}\t{o['service']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Fiverr daily report from CSV")
    parser.add_argument('csv_file', help='Path to Fiverr CSV file')
    parser.add_argument('-o', '--output', default='daily_report.md', help='Output file')
    parser.add_argument('--format', choices=['markdown', 'text'], default='markdown', help='Output format')
    parser.add_argument('--no-type-summary', action='store_true', help='Disable service type summary')
    parser.add_argument('--date-col', default='date', help='CSV column name for date')
    parser.add_argument('--client-col', default='client name', help='CSV column name for client name')
    parser.add_argument('--amount-col', default='amount', help='CSV column name for amount')
    parser.add_argument('--service-col', default='service type', help='CSV column name for service type')

    args = parser.parse_args()

    orders = read_orders(args.csv_file, args.date_col, args.client_col, args.amount_col, args.service_col)
    summary = summarize_orders(orders)

    sections = []
    for date in sorted(summary.keys()):
        data = summary[date]
        if args.format == 'markdown':
            section = render_markdown(date, data, include_type=not args.no_type_summary)
        else:
            section = render_text(date, data, include_type=not args.no_type_summary)
        sections.append(section)
    report = "\n\n".join(sections)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(report)


if __name__ == '__main__':
    main()
