import argparse

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



