import os
import subprocess

from contextlib import contextmanager
import sys, os

class Git:
    def run_command(self, command):
        subprocess.Popen(
                command,
                cwd=self.dir_path,
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.STDOUT
            ).wait()

    def __init__(self, repo_name):
        """
        Open or init a git repository

        Args
        repo_name: The name of the repository to open
        """

        self.dir_path = 'repositories/%s' % repo_name

        if not os.path.isdir(self.dir_path):
            os.makedirs(self.dir_path, exist_ok=True)
        if not os.path.isdir(self.dir_path + '/.git'):
            init_commnad = ['git', 'init']
            self.run_command(init_commnad)


    def commit(self, msg: str, date):
        """
        Commit command
        """

        date = '--date="%s"' % date
        commit_command = ['git', 'commit', date, '-m', msg]
        self.run_command(commit_command)


    def config(self, key: str, value: str):
        """
        set config
        """

        config_command = ['git', 'config', key, value]
        self.run_command(config_command)


    def add(self, path: str):
        """
        Add file or file list
        """
        add_command = ['git', 'add', path]
        self.run_command(add_command)


    def append_file(self, file_name: str, text: str):
        file_path = "%s/%s" % (self.dir_path, file_name)
        with open(file_path, 'a') as file:
            file.write(text)
