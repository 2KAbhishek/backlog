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
