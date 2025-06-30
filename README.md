![AI Factory Banner](./docs/public/banner.png)

# 🏭 AI Factory Core

> A curated collection of lightweight, AI-powered automation tools built by [Lenox](mailto:jx595127@gmail.com), designed for freelancers and solopreneurs.

# 🏗️ ai-factory-core

**The unified warehouse for modular AI-powered automation tools.**

This repository serves as the central hub for managing multiple AI-enhanced productivity tools, integrating core SDKs, workflow logic, reusable modules, and components for future SaaS deployment.

---

## 📦 Directory Structure

ai-factory-core/
│
├── fiverr-daily-reporter/ # 🎯 Automated daily report generator for Fiverr
├── shopify-sync-engine/ # 🛒 Shopify inventory sync engine
├── content-distribution-kit/ # 📤 Cross-platform content distributor
│
├── core-sdk/ # 🧱 Shared utilities and core functions
├── .factory.yaml # ⚙️ Declarative workflow definition (DAG)
├── LICENSE # MIT License
└── README.md # Project description

---

## 🔧 Core Modules

| Module             | Description                                                      |
|--------------------|------------------------------------------------------------------|
| `csv_reader.py`     | Universal data parser for Fiverr, Shopify exports, etc.         |
| `markdown_generator.py` | Converts structured data to clean Markdown reports          |
| `api_client.py`     | Unified wrapper for external APIs (Shopify, Notion, etc.)       |
| `event_logger.py`   | Logs user activity and feedback for future analytics            |
| `user_auth.py`      | Basic multi-user authentication for future SaaS infrastructure |
| `task_scheduler.py` | Handles scheduled/batch task execution                          |

---

## 🌐 Included Tools

| Tool Name            | Purpose                                                        | Status     |
|----------------------|----------------------------------------------------------------|------------|
| Fiverr Reporter      | Auto-generate daily Markdown reports from Fiverr CSV exports   | ✅ Complete |
| Shopify Sync Tool    | Sync inventory to Shopify with multi-SKU support               | ✅ Complete |
| Content Distributor  | Publish content to Notion, Medium, Xiaohongshu, etc.           | ✅ Complete |

---

## 🚀 Roadmap

- ✅ Unified into mono-repo
- 🔜 Integrate Stripe for subscription billing
- 🔜 Add Supabase Auth for multi-user control
- 🔜 Connect to EventBus + DuckDB for behavior logging
- 🔜 Deploy via Docker on Render/Railway
- 🔜 Write tutorials and publish on GitHub Pages & Medium

---

## 🪪 License

This project is licensed under the **MIT License**.  
You are free to use, modify, distribute, and commercialize with attribution.

---

## 🙌 Powered by

- ChatGPT (OpenAI / Codex)
- Python 3.11+
- Notion API, Shopify API, Fiverr CSV exports
- GitHub Actions (upcoming)
- Supabase, DuckDB, Stripe

---

> 🧠 Build your AI Factory — one tool at a time.  
> Modular, scalable, automated.
