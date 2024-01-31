# Git Guidance

## git commands

```sh
git init
git clone /path/to/repository
git clone username@host:/path/to/repository
```

```sh
# remote server https://github.com/<account_name>/<project_name>.git
# fetch and local-merge using FETCH_HEAD revision expression
# ~/.gitconfig
```

```sh
git config --global user.name "mekatronik-achmadi"
git config --global user.email "mekatronik.achmadi@gmail.com"
git config --global http.proxy http://achmadi10%40mhs.ep.its.ac.id:password@proxy.its.ac.id:8080
git config --global https.proxy https://achmadi10%40mhs.ep.its.ac.id:password@proxy.its.ac.id:8080

git config --global gui.editor pluma
git config --global gui.spellingdictionary none
git config --global cola.spellcheck false
git config --global color.ui 'auto'
```

## commiting patch

```sh
git status
git diff <file>
git diff <source_branch> <target_branch>
git add .
git add *
git add -u
git add <filename>
git rm --cached [file_name]
git commit -m "Commit message"
```

## undo last commit

```sh
git reset --soft HEAD~1
```

## add a remote server

```sh
git remote add gitlocal https://10.124.4.150/git/project.git
git remote add github https://github.com/username/project.git
git remote -v
```

## push to remote server

```sh
git branch
git push <remote> <branch>
git push github master
git push -u github master
git push github branch:branch
git push github branch:refs/heads/branch
```

## pull from remote server

```sh
git pull
git fetch origin
git merge master
git reset --hard origin/master
```

## show log

```sh
git log
git show <hash_commit_hex_number>
```

```sh
tig
```

## github access token

```sh
xdg-open 'https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token'
echo 'ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' > ~/GithubToken
echo '
export GITHUBTOKEN=$(cat ~/GithubToken)
' >> ~/.bashrc
echo $GITHUBTOKEN
```
