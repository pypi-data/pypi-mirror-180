# Example Package

## Introduction

AMAP is command line interface tool similar to the famous NMAP. It scans an IP address or domain name to find active ports and related information.

It uses FOFA AMAP API to implement the function.

## Usage & Options

Usage:

  amap <ip_address_or_domain_name> [options]

Options:

  -h --help  Show help information

  -n --nmap  Use nmap tool to scan

## Information

* Python version >= 3.7 is required to run `subprocess.run()`
* Package `docopt` is required as a CLI builder