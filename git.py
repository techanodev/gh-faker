import os
import subprocess

class Git:
    def __init__(self, repo_name):
        """
        Open or init a git repository

        Args
        repo_name: The name of the repository to open
        """

        self.dir_path = 'repositories/%s' % repo_name

        if not os.path.isdir(self.dir_path):
            os.makedirs(dir_path, exist_ok=True)
        if not os.path.isdir(self.dir_path + '/.git'):
            init_commnad = ['git', 'init']
            subprocess.Popen(init_commnad, cwd=dir_path).wait()



    def commit(self, msg: str, date):
        """
        Commit command
        """

        date = '--date="%s"' % date
        commit_command = ['git', 'commit', date, '-m', msg]
        subprocess.Popen(commit_command, cwd=self.dir_path).wait()


    def config(self, key: str, value: str):
        """
        set config
        """

        config_command = ['git', 'config', key, value]
        subprocess.Popen(config_command, cwd=self.dir_path).wait()


    def add(self, path: str):
        """
        Add file or file list
        """
        add_command = ['git', 'add', path]
        subprocess.Popen(add_command, cwd=self.dir_path).wait()


    def write_file(self, file_name: str, text: str):
        file_path = "%s/%s" % (self.dir_path, file_name)
        with open(file_path, 'w') as file:
            file.write(text)
