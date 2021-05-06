	#### git commands

~~~
git init
git clone /path/to/repository
git clone username@host:/path/to/repository
~~~

~~~
# remote server https://github.com/<account_name>/<project_name>.git
# fetch and local-merge using FETCH_HEAD revision expression
# ~/.gitconfig
~~~

~~~
git config --global http.proxy http://achmadi10%40mhs.ep.its.ac.id:wearesalafy@proxy.its.ac.id:8080
git config --global https.proxy https://achmadi10%40mhs.ep.its.ac.id:wearesalafy@proxy.its.ac.id:8080
git config --global user.name "mekatronik-achmadi"
git config --global user.email "mekatronik.achmadi@gmail.com"
git config --global gui.editor pluma
git config --global gui.spellingdictionary none
git config --global cola.spellcheck false
git config --global color.ui 'auto'
~~~

#### git ssh password prompt

~~~
export SSH_ASKPASS=/usr/bin/x11-ssh-askpass
export SSH_ASKPASS=/usr/lib/git-core/git-gui--askpass
export GIT_ASKPASS=/usr/bin/x11-ssh-askpass
export GIT_ASKPASS=/usr/lib/git-core/git-gui--askpass
git config --global core.askPass /usr/bin/x11-ssh-askpass
git config --global core.askPass /usr/lib/git-core/git-gui--askpass
~~~

#### commiting patch

~~~
git status
git diff <file>
git diff <source_branch> <target_branch>
git add .
git add *
git add -u
git add <filename>
git rm --cached [file_name]
git commit -m "Commit message"
~~~

#### undo last commit

~~~
git reset --soft HEAD~1
~~~

#### add a remote server

~~~
git remote add gitlocal https://10.124.4.150/git/project.git
git remote add github https://github.com/username/project.git
git remote -v
~~~

#### push to remote server

~~~
git branch
git push <remote> <branch>
git push github master
git push -u github master
git push github branch:branch
git push github branch:refs/heads/branch
~~~

#### pull from remote server

~~~
git pull
git fetch origin
git merge master
git reset --hard origin/master
~~~

#### show log

~~~
git log
git show <hash_commit_hex_number>
~~~

