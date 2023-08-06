# AMAP

## Introduction

AMAP is a command line interface tool similar to the famous NMAP. It scans an IP address or a domain name to find active ports and returns related information.

It uses FOFA AMAP API to implement the function.

## Installation

```bash
pip install amap-holydragon
```

## Usage & Options

Usage:

  amap [-h | --help]

  amap <ip_address_or_domain_name> [-n | --nmap] [-x <filename\> | --xml=<filename\>]

Options:

  -h --help  Show help information

  -n --nmap  Use nmap to scan

  -x <filename\> --xml=<filename\>  Output XML file

## Information

* Python version >= 3.7 is required to run `subprocess.run()`
* Package `docopt` is required as a CLI builder