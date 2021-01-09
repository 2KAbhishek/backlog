import argparse

# Initialize parser
parser = argparse.ArgumentParser(prog="backlog", description="Change time of last commit in git.",
                                 epilog="Visit github.com/2KAbhishek/backlog for more.")

# Positional arguments
parser.add_argument("hours", metavar="hours", type=int,
                    help="Number of hours to go back")

# Optional arguments
parser.add_argument("-d", "--days", metavar="days", type=int,
                    action="store", default=0, help="Number of days to go back")


parser.add_argument("-m", "--minutes", metavar="minutes",
                    type=int, action="store", default=0, help="Number of minutes to go back")

args = parser.parse_args()

days = args.days
hours = args.hours
minutes = args.minutes


def get_time(days: int, hours: int, minutes: int) -> str:
    """Use arguments to get time string in required format, e.g: Sat Jan 9 16:46:28 2021 +0530"""
    import time
    back_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60)
    time_now = time.time()
    commit_time = time_now - back_seconds
    return(time.strftime("%a %b %d %H:%M %Y %z", time.localtime(commit_time)))


def update_commit(time_str: str):
    """Set environment variables and updates commit time."""
    import os
    os.environ["GIT_AUTHOR_DATE"] = time_str
    os.environ["GIT_COMMITTER_DATE"] = time_str
    os.system("git commit --reset-author --amend --no-edit")


time_str = get_time(days, hours, minutes)
update_commit(time_str)
