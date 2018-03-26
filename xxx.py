
# pip install Gitpython

import git
import os

cwd = os.getcwd()
repo = git.Repo(cwd)
print repo.git.status()

repo.git.pull()

f=open(cwd + '/test.md', 'w')
f.write("blabla")
f.close()

print repo.git.status()
# print repo.git.add("test.md")
# repo.git.add("test.md")
print repo.git.add(".")

print repo.git.status()
# print repo.git.commit(m = "from Gitpython")
repo.git.commit(m = "from Gitpython")
# print repo.git.status()
# print repo.git.push()
repo.git.push()


