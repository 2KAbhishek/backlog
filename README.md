<div align = "center">

<h1><a href="https://2kabhishek.github.io/backlog">backlog</a></h1>

<a href="https://github.com/2KAbhishek/backlog/blob/main/LICENSE">
<img alt="License" src="https://img.shields.io/github/license/2kabhishek/backlog?style=flat&color=eee&label="> </a>

<a href="https://github.com/2KAbhishek/backlog/graphs/contributors">
<img alt="People" src="https://img.shields.io/github/contributors/2kabhishek/backlog?style=flat&color=ffaaf2&label=People"> </a>

<a href="https://github.com/2KAbhishek/backlog/stargazers">
<img alt="Stars" src="https://img.shields.io/github/stars/2kabhishek/backlog?style=flat&color=98c379&label=Stars"></a>

<a href="https://github.com/2KAbhishek/backlog/network/members">
<img alt="Forks" src="https://img.shields.io/github/forks/2kabhishek/backlog?style=flat&color=66a8e0&label=Forks"> </a>

<a href="https://github.com/2KAbhishek/backlog/watchers">
<img alt="Watches" src="https://img.shields.io/github/watchers/2kabhishek/backlog?style=flat&color=f5d08b&label=Watches"> </a>

<a href="https://github.com/2KAbhishek/backlog/pulse">
<img alt="Last Updated" src="https://img.shields.io/github/last-commit/2kabhishek/backlog?style=flat&color=e06c75&label="> </a>

</div>

Backlog is a tool that allows developers to alter the time of their git commits.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of `python3`

## Installing backlog

To install backlog, follow these steps:

```bash
git clone https://github.com/2kabhishek/backlog
cd backlog
# Setup symlink, make sure target directory is added to PATH
ln -sfnv "$PWD/backlog.py" ~/Applications/bin/backlog
```

## Using backlog

```bash
USAGE:
    backlog [-h] [-d days] [-m minutes] hours

Change time of last commit in git.

positional arguments:
  hours                 Number of hours to go back

optional arguments:
  -h,          --help                  Show this help message and exit
  -hr hours,   --hours   hours         Number of hours to go back
  -d  days,    --days    days          Number of days to go back
  -m  minutes, --minutes minutes       Number of minutes to go back

EXAMPLE:
backlog -d 1 -hr 12 # Changes the last commit time to 1 day 12 hours ago

```

Hit the :star: button if you found this useful.

### More Info
