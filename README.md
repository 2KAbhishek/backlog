# backlog

![Size](https://img.shields.io/github/repo-size/2kabhishek/backlog?style=plastic&color=0f0&label=Size)
![Updated](https://img.shields.io/github/last-commit/2kabhishek/backlog?style=plastic&color=f00&label=Updated)
![Stars](https://img.shields.io/github/stars/2kabhishek/backlog?style=plastic&color=ffc801&label=Stars)
![Forks](https://img.shields.io/github/forks/2kabhishek/backlog?style=plastic&color=003cff&label=Forks)
![Watchers](https://img.shields.io/github/watchers/2kabhishek/backlog?style=plastic&color=ff5500&label=Watchers)
![Contributors](https://img.shields.io/github/contributors/2kabhishek/backlog?style=plastic&color=f0f&label=Contributors)
![License](https://img.shields.io/github/license/2kabhishek/backlog?style=plastic&color=555&label=License)

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
  -h, --help            show this help message and exit
  -d days, --days days  Number of days to go back
  -m minutes, --minutes minutes
                        Number of minutes to go back

EXAMPLE:
backlog 12 -d 1 # Changes the last commit time to 1 day 12 hours ago

```

Hit the :star: button if you found this useful.

### More Info
