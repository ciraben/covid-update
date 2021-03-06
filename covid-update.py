#!/usr/bin/env python3
#covid_update.py
#Tom, 2020
'''Print regional COVID case data from the BCCDC.

From the BCCDC data notes:
"Case Details and Laboratory Information are updated daily Monday through Friday at
5:00 pm."

See
http://www.bccdc.ca/Health-Info-Site/Documents/BC_COVID-19_Disclaimer_Data_Notes.pdf
for more info.

---Options---

-a, --all-regions

Print data for all regions.

-d N, --days N

Print data for the past N days.

-h, --help

Print a help message covering these options.

--no-hist

Don't print the histogram.

-r REGION, --region REGION

Specify a region. Defaults to Vancouver Island. Valid regions are I (Interior), F (Fraser), C (Vancouver Coastal), V (Vancouver Island), N (Northern).

-t, --today

Print today's data only.

--testing

Read data from sample2.txt instead of BCCDC.

--version

Print covid-update version.

-w N, --weeks N

Print data for the past N weeks.

'''

import os
from sys import exit
import requests
import datetime
import argparse

REGION_DICT = {
    "I": "Interior",
    "F": "Fraser",
    "C": "Vancouver Coastal",
    "V": "Vancouver Island",
    "N": "Northern",
}

# interface with command line
# argparse gives nice help for users
parser = argparse.ArgumentParser(
    description="Print regional COVID case data from the BCCDC."
)
region_group = parser.add_mutually_exclusive_group()
region_group.add_argument(
    "-a",
    "--all-regions",
    default=False,
    help="Print data for all regions.",
    action="store_true",
    dest="all_regions"
)
region_group.add_argument(
    "-r",
    "--region",
    metavar="R",
    choices=[
        "I", "F", "C", "V", "N",
        # "Interior", "Fraser", "Vancouver Coastal", "Vancouver Island", "Northern"
    ],
    default="V",
    help='Specify a region. Defaults to Vancouver Island. Valid regions are '\
        'I (Interior), F (Fraser), C (Vancouver Coastal), V (Vancouver Island), '\
        'N (Northern).',
)
time_group = parser.add_mutually_exclusive_group()
time_group.add_argument(
    "-d",
    "--days",
    metavar="N",
    type=int,
    help="Print data for the past N days. Overridden by -t.",
)
time_group.add_argument(
    "-w",
    "--weeks",
    metavar="N",
    type=int,
    help="Print data for the past N weeks. Overridden by -t.",
)
time_group.add_argument(
    "-t",
    "--today",
    default=False,
    help="Only print today's data tally. Overrides -d/-w.",
    action="store_true",
)
verbosity_group = parser.add_mutually_exclusive_group()
verbosity_group.add_argument(
    "-v",
    "--verbose",
    default=False,
    help="Print all case details.",
    action="store_true",
)
parser.add_argument(
    "--version",
    default=False,
    help="Print covid-update version.",
    action="store_true",
)
parser.add_argument(
    "--testing",
    default=False,
    help="Read data from sample2.txt instead of BCCDC.",
    action="store_true",
)
parser.add_argument(
    "--no-hist",
    help="Don't print a histogram.",
    action="store_true",
)
args = parser.parse_args()

if args.version:
    print("0.2.0")
    exit()

# get BCCDC data
if args.testing:
    # use this for interface testing
    with open("sample2.txt") as file:
        splitting = file.read().splitlines()
else:
    r = requests.get(
        'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Case_Details.csv'
    )
    splitting = r.text.splitlines()

# strip metadata
splitting.pop(0)
# isolate dates as splitting[x][0]
for i in range(len(splitting)):
    splitting[i] = splitting[i].replace('"','').split(',')

#     ---Notes on datetime---
# datetime.datetime.strptime(date_string, "%Y-%m-%d")
# converts YYYY-MM-DD to date object
# datetime.datetime.strftime(date) makes a string

# datetime.today() returns today!

# date1 < date2 compares chronologically

# datetime.timedelta.days gives diff as int
# date.isoformat() returns "YYYY-MM-DD"
# or date.strftime(format) for custom format

# determine date format
ISO_FORMAT = "%Y-%m-%d"
MDY_FORMAT = "%m/%d/%Y"
if '/' in splitting[0][0]:
    date_format = MDY_FORMAT
else:
    date_format = ISO_FORMAT

# cases-per-day tally holder, limited to -d/-w
daily_dict = {}
today = datetime.date.today()
if args.days:
    earliest_date = today - datetime.timedelta(days=args.days-1)
elif args.weeks:
    earliest_date = today - datetime.timedelta(weeks=args.weeks, days=-1)
else:
    earliest_date = datetime.datetime.strptime(splitting[0][0], date_format).date()
delta = today - earliest_date
for i in range(delta.days + 1):
    daily_dict[earliest_date + datetime.timedelta(days=i)] = 0

if args.all_regions:
    args.region = "BC"
elif len(args.region) == 1:
    args.region = REGION_DICT[args.region]
for line in splitting:
    if args.region in line or args.all_regions:
        try:
            # tally cases by date
            date = datetime.datetime.strptime(line[0], date_format).date()
            if earliest_date <= date:
                daily_dict[date] += 1
                if args.verbose:
                    print(line)
        except ValueError:
            print(f"Bad date format, line {splitting.index(line)}.")
            print("("+line+")")

if not args.verbose:
    if args.today:
        if daily_dict[today] == 1:
            s = ""
        else:
            s = "s"
        print(
            f"{daily_dict[today]} new case{s} today in the " + args.region + " region."
        )
    else:
        for day in daily_dict:
            if daily_dict[day] == 1:
                s = ""
            else:
                s = "s"
            print(
                f"{day.isoformat()}: {daily_dict[day]} new case{s} in the " +
                args.region + " region."
            )
    if today.weekday() > 4:
        print("Note: This weekend's data will be posted on Monday.")


# for hists - use terminal_size.lines or .columns
if not args.no_hist:
    maxw = 150
    maxh = 30
    terminal_size = os.get_terminal_size()
    maxval = max(daily_dict.values())
    hheight = min(maxh, terminal_size[1] - 10)
    hwidth = min(maxw, terminal_size[0] - 10)
    xscale = 1
    yscale = max(1, (maxval // 10 + 1) * 10 / hheight)
    valchs = len(str(yscale * hheight))

    print()
    for row in range(hheight):
        dat = ""
        if row == hheight // 2 or row == 0:
            scalelabel = str(int(((hheight - row) * yscale)))
            dat += " " * (valchs - len(scalelabel)) + scalelabel + " |"
        else:
            dat += " " * (valchs) + " |"
        for col in range(hwidth):
            date = today - datetime.timedelta(days = hwidth - col)
            if daily_dict[date] >= (hheight - row) * yscale:
                dat += "O"
            else:
                dat += " "
        print(dat)
    print(" " * (valchs) + " +" + "-" * hwidth)

    # bottom scale labels
    bottom = " " * valchs + "  "
    for col in range(hwidth):
        date = today - datetime.timedelta(days = hwidth - col)
        if date.day == 1:
            bottom += date.strftime('%b')[0]
        else:
            bottom += " "
    print(bottom)

