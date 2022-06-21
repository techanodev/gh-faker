import os
import subprocess

def _get_repo_path(repo_name: str):
    return 'repositories/%s' % repo_name

def _get_file_path(repo_name: str, file_path: str) -> str:
    dir_path = _get_repo_path(repo_name)
    return '%s/%s' % (dir_path, file_path)


def init(repo_name: str):
    """
    Open or init a git repository

    Args
        repo_name: The name of the repository to open
    """

    dir_path = _get_repo_path(repo_name)

    if not os.path.isdir(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    if not os.path.isdir(dir_path + '/.git'):
        init_commnad = ['git', 'init']
        subprocess.Popen(init_commnad, cwd=dir_path).wait()

    return repo_name

def commit(repo_name: str, msg: str, date):
    """
    Commit command
    """

    dir_path = _get_repo_path(repo_name)
    date = '--date="%s"' % date
    commit_command = ['git', 'commit', date, '-m', msg]
    subprocess.Popen(commit_command, cwd=dir_path).wait()

def add(repo_name: str, path: str):
    """
    Add file or file list
    """
    dir_path = _get_repo_path(repo_name)
    add_command = ['git', 'add', path]
    subprocess.Popen(add_command, cwd=dir_path).wait()


def write_file(repo_name: str, file_name: str, text: str):
    file_path = _get_file_path(repo_name, file_name)
    with open(file_path, 'w') as file:
        file.write(text)
