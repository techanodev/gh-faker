import sys
import argparse
import random
import git

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


def main():
    args = parser.parse_args()
    config = vars(args)
    commits_per_day = config['commits_per_day']
    is_random = config['random']
    delta = config['delta']
    repo_name = config['repo_name'][0]

    days = 10

    git.init(repo_name)

    for i in range(days):
        text = ''
        if is_random:
            commits_per_day = random.randint(
                    commits_per_day - delta, commits_per_day + delta
                    )

        file_name = 'file%d.txt' % i
        for commit_id in range(commits_per_day):
            text += str(commit_id)
            git.write_file(repo_name, file_name, text)
            git.add(repo_name, '.')
            git.commit(repo_name, 'commit %d for file %d' % (commit_id, i))
        print(text)
        
        

if __name__ == "__main__":
    main()
