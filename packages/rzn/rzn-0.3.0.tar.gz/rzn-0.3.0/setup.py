# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rzn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rzn',
    'version': '0.3.0',
    'description': 'rzn - rsync/rclone git like push/pull wrapper',
    'long_description': "# Introduction\n\nI created rzn because I'm used to running `git push / pull` for synchronizing my files. But for some use cases, like\nsynchronizing my pictures / music etc, git would be an overkill in used storage and speed.\n\nRzn leverages rsync or rclone to synchronize your files. It searches for the configuration file `.rzn` in the current or\nparent directories like git so you can run `rzn push / pull` from any (sub)directory.\n\n## Install\n\n```\n$ pip install git+https://github.com/meeuw/rzn\n```\n\nor download `rzn.py` and place it in your path.\n\n\n## Usage\n\nYou can use the `--backup` argument of rsync / rclone to make sure rzn never overrides / deletes your files. You're\nfree to use any directory but I use the following directory structure (local and remote):\n\n```\n$ find bluh\nbluh/current/file1\nbluh/current/dir1/file1\nbluh/2019-03-03T07:31:09.015242/dir1/file1\nbluh/2019-03-04T09:10:08.023142/file2\n```\n\nAs rzn doesn't do any versioning you'll have to be really cautious with cleaning your backups. As rsync also\nsynchronizes your timestamps a tool like `fdupes` might be usefull to cleanup duplicate files. Before removing\nchanged files I'd recommend to always compare the current and backupped files.\n\nYou can use `sparsefilters` to generate `--filter` arguments for rsync for sparse synchronisation. Sparse filters\nmake it possible to only synchronize specific files / directories with a remote location.\n\nThe only required configuation item in the `[main]` section is `remote`. The local location of the synchronisation\narguments is determined by the location of your `.rzn` file.\n\nSample `.rzn` file:\n\n```\n[main]\nremote = /home/meeuw/tmp/remote\nappend = /current/\nsparsefilters =\n   /bluh\n   /dir***\nargs = -Pa\n  --backup\n  --backup-dir={target}../{datetimeisoformat}\n  --delete\n  --delete-excluded\n```\n\nI recommend to always run `rzn pull` before making any changes to your files and `rzn push` as soon as possible.\n\n```\n$ rzn pull\n\n$ vi file1\n\n$ rzn push\n```\n\n## FAQ\n\nQ: Why isn't the file which I've pushed shared anymore?\n\nA: When using rclone you might not want to use a remote backup directory if your files are shared with other users, if\nyou push changes to an existing file it will be replaced and your shared file will be moved to the backup directory. As\n(most) cloud remotes have their own versioning / recycle bin you don't need a backup dir. You can use the\nconfiguration item `pull_args` to use the `--backup-dir` argument only for your local files.\n\nQ: Why should I use this tool instead of using automatic synchronisation?\n\nA: Rzn gives you full control about when and how your files are synchronized.\n\nQ: I've found a bug or limitation of rzn\n\nA: Use the issue tracker (on GitHub) to report your issue and if you can, fix it yourself and submit a pull request.\n",
    'author': 'Dick Marinus',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
