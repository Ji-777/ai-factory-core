# Content Distribution Syncer

Content Distribution Syncer is a CLI tool that helps you publish a single piece of content across multiple platforms. It works with Markdown or HTML files or a direct link and adapts the content format for each destination platform.

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
