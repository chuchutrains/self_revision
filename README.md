# ICT1008 Algorithm Revision

Personal Google Docs notes, click [here](https://docs.google.com/document/d/1jHo6pdvPq40JYFj7vGQz_DkDH__BKGhOP9z6V3x3l9s/edit?usp=sharing).

# Git Repository
1. Download Git for Windows, click [here](https://git-scm.com/download/win).
2. Open command prompt.
3. Change directory to project folder `cd <project folder>`.
4. Clone the repository `git clone https://github.com/chuchutrains/self_revision.git`.

### Branch Out From A Branch
1. Check which branch are you in `git branch -a`.
2. `git checkout -b <source> <destination>`, eg branching out from master and name branch as feature/abc `git checkout -b master feature/abc`.

### Delete Branch
1. `git push -d <remote> <branch>`, eg `git push -d origin feature/abc`.
2. @TODO: --prune.

### Git Push
1. Add all the files changes to staging `git add .`, "." is to add all.
2. Check which files are being staged `git status`.
3. Commit with messages `git commit -m "<branch - messages>"`.
4. Push the changes `git push origin branch`.

### Git Stash
1. Store your local changes to somewhere else `git stash`.
2. See the list of stashes `git stash list`.
3. Remove all stashes `git stash drop`.

### Git Revert
Revert to that commit, make sure to `git stash` your changes first. `git revert <commit id>`, eg `git revert c4aeda5a7ad198ca43558679b49f4b15e5843ce2`.

### Git Pull
To pull changes from the remote to your local `git pull <remote> <branch>`, eg `git pull remote feature/abc`.\
`git pull` is a combination of `git fetch` and `git merge`, might have to resolve the conflict.

# Markdown (.md) Preview
https://markdownlivepreview.com/