# from https://github.com/jonathanpaulson
import argparse
import subprocess
import sys
import requests
YEAR = 2024

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5f4ce0ea365552e6a16b95183522331fa238e9f64c3e3817ae39a728703fb25c8087669ba90e81ee1b07ef62ad6c1863d8715acdfc9509e593'

useragent = 'https://github.com/ErikLundb3rg/AOC-2024/blob/main/get-input.py by erik.lundberg32@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2024)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()
cmd = f'curl https://adventofcode.com/{args.year}/day/{
    args.day}/input --cookie "session={SESSION}" -A \"{useragent}\"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
