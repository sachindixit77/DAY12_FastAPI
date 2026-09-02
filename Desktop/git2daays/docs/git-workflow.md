# Git Workflow Explanation

Git is a version control system used to track changes in source code. GitHub is used to store the repository remotely and support collaboration and code review.

## 1. Clone

The repository is first cloned from GitHub to the local system using `git clone`. This creates a local copy of the project.

## 2. Branch

A separate feature branch is created using `git switch -c feature/day2-profile`. Development is performed on this branch instead of directly changing the main branch.

## 3. Add

After making changes, `git add` is used to move the required files to the staging area.

## 4. Commit

The staged changes are saved using `git commit`. Each commit has a meaningful message describing the change.

Example:

`feat: add intern profile data model`

## 5. Push

The feature branch is uploaded to GitHub using `git push`. This makes the changes available to other team members.

## 6. Pull

`git pull` downloads the latest changes from the remote repository and updates the local branch.

## 7. Fetch

`git fetch` downloads information about changes from the remote repository without immediately modifying the working files.

## 8. Pull Request

A Pull Request is created on GitHub to request that the feature branch be merged into the main branch.

## 9. Code Review

Team members review the code, check its quality, correctness, tests and coding standards. Changes can be requested before approval.

## 10. Merge

After successful code review, the Pull Request is merged into the main branch.

## 11. Merge Conflict

A merge conflict occurs when Git cannot automatically combine changes made to the same part of a file. The developer must manually resolve the conflict and then commit the resolved changes.

## 12. .gitignore

The `.gitignore` file tells Git which files or folders should not be tracked, such as Python cache files, virtual environments and environment variables.

## 13. README

The README provides basic information about the project, its structure, purpose and instructions for using it.

## Conclusion

The complete workflow followed in this assignment is:

Clone → Branch → Add → Commit → Push → Pull Request → Code Review → Merge → Pull

This workflow helps maintain clean source code, track changes and support team collaboration.
