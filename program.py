import sys
import random
from git import Git
from datetime import datetime, timedelta
from tqdm import tqdm

from args import parser

import signal
import sys

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def init_config():
    email = config['email']
    name = config['name']

    if email != None:
        git.config('user.email', email)
        print("Email: %s" % email)
    if name != None:
        git.config('user.name', name)
        print("Name: %s" % name)


def get_days():
    args = parser.parse_args()
    config = vars(args)

    start_date_str = config['start_date']
    end_date_str = config['end_date']

    if start_date_str != None:
        start_date = datetime.strptime(start_date_str, '%y-%m-%d')
    else:
        start_date = datetime.today()
    if end_date_str != None:
        end_date = datetime.strptime(end_date_str, '%y-%m-%d')
    else:
        end_date = datetime.today()
    print("Start date: %s\tEnd Date: %s" % (str(start_date).split(" ")[0], str(end_date).split(" ")[0]))
    number_of_days = (end_date - start_date).days

    return [(start_date + timedelta(days = day)).isoformat() for day in range(number_of_days)]


def commit_day(git, day, days_list, commits_per_day, delta, is_random):
    i = days_list.index(day)

    text = ''
    if is_random:
        commits_per_day = random.randint(
            commits_per_day - delta, commits_per_day + delta
            )

    file_name = 'file.txt'
    for commit_id in range(commits_per_day):
        text += str(commit_id)
        git.append_file(file_name, text)
        git.add('.')
        git.commit('commit %d for file %d' % (commit_id, i), day)


def main():
    args = parser.parse_args()
    config = vars(args)
    commits_per_day = config['commits_per_day']
    is_random = config['random']
    delta = config['delta']
    repo_name = config['repo_name'][0]
    
    print("Repository name: %s" % repo_name)
    print("Is Random: %s \t Delta: %d" % (is_random, delta))
    print("commits per day: %d" % commits_per_day)

    git = Git(repo_name)

    days_list = get_days()

    pbar = tqdm(days_list)
    for day in pbar:
        pbar.set_description("Processing on %s" % day.split('T')[0])
        commit_day(git, day, days_list, commits_per_day, delta, is_random)


if __name__ == "__main__":
    main()
