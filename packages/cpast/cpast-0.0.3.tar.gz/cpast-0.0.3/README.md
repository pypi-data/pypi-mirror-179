# 🕓 Cpast

[![python](https://img.shields.io/badge/python->=%203.7%20-blue)](https://www.python.org/downloads)
[![pypi](https://img.shields.io/pypi/v/cpast)](https://pypi.org/project/cpast)
[![license](https://img.shields.io/github/license/skuzow/cpast.svg)](https://github.com/skuzow/cpast/blob/master/LICENSE)
[![release](https://github.com/skuzow/cpast/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/skuzow/cpast/actions/workflows/release.yml)
[![test](https://github.com/skuzow/cpast/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/skuzow/cpast/actions/workflows/test.yml)

Commit in the past.

## 🗿 Usage

```bash
  python -m cpast [-h] -d DATE -t TIME -m MESSAGE
```

- Date format: `YYYY-MM-DD`
- Time format: `HH:MM:SS`

## ⚙️ Options

- `-h, --help` Show help message and exit
- `-d DATE, --date DATE` Commit date, example: 2021-12-25
- `-t TIME, --time TIME` Commit time, example: 22:13:05
- `-m MESSAGE, --message MESSAGE` Commit message, example: "init :)"

## 🧩 Install

```bash
  pip install cpast
```
