import sys
import argparse
import random
from git import Git
from datetime import datetime, timedelta

parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('repo_name', nargs='+', help='Repository name')

parser.add_argument(
        '-c',
        '--commits-per-day',
        type=int,
        default=10,
        help='Number of commits per day.')

parser.add_argument(
        '-r',
        '--random',
        action="store_true",
        help='use random number in a range for commits per days'
)

parser.add_argument(
        '-d',
        '--delta',
        type=int,
        default=2,
        help='delta value for range commits per days'
)

parser.add_argument(
        '-s',
        '--start-date',
        type=str,
        help="Start date for commit (format yyyy-mm-dd)"
        )

parser.add_argument(
        '-e',
        '--end-date',
        type=str,
        help="end date for date range (format yyyy-mm-dd)"
        )


parser.add_argument(
        '--email',
        type=str,
        help="Email for commit"
        )


parser.add_argument(
        '--name',
        type=str,
        help="name for commit"
        )


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
    number_of_days = (end_date - start_date).days

    return [(start_date + timedelta(days = day)).isoformat() for day in range(number_of_days)]

def commit_day(git, day, days_list, commits_per_day, delta, is_random):
    i = days_list.index(day)

    text = ''
    if is_random:
        commits_per_day = random.randint(
            commits_per_day - delta, commits_per_day + delta
            )

    file_name = 'file%d.txt' % i
    for commit_id in range(commits_per_day):
        text += str(commit_id)
        git.write_file(file_name, text)
        git.add('.')
        git.commit('commit %d for file %d' % (commit_id, i), day)

def main():
    args = parser.parse_args()
    config = vars(args)
    commits_per_day = config['commits_per_day']
    is_random = config['random']
    delta = config['delta']
    repo_name = config['repo_name'][0]

    email = config['email']
    name = config['name']

    git = Git(repo_name)

    if email != None:
        git.config('user.email', email)
    if name != None:
        git.config('user.name', name)

    days_list = get_days()

    for day in days_list:
        commit_day(git, day, days_list, commits_per_day, delta, is_random)


if __name__ == "__main__":
    main()
