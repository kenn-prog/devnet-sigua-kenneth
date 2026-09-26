# Module 1 — Git & GitHub

**Student:** Sigua, Kenneth
**Date:** 9/26/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]
Git is a tool that we used a command that help us during when we are coding. It help us to track our code changes. Example in a real life scenario, we are making a school project then we need to save it, we use git to save our code by using command like git add, git commit, and git push. The question is why not we use save in our computer instead git, the best thing that git have is that whether we change and save our code we can go back to the saved file we commit by using git pull. Its help us to go back when we got encounter error in our code. On the other hand, Github is a hub where it store all the data we push. All the code we commit and push goes here, and we can look all the commit changes.

---

## Key vocabulary (in your own words)

- repository: Its like a folder that stored in github. This contain all of our code in this repository.
- commit: It use to saved a file when we change our code and able to go back to the commit you saved. This is like a log or history where we can track what are changes of our code amd go back to that specific commit.
- branch: Its uses to code without affecting the main version of the project. This is like going to other room to prevent messing your bedroom. Another thing about branch is that we can collaborate by working in each branches to without conflict when we save at the same time.
- push / pull: This is used to push or upload the saved/commit code to the github. Then pull is used to pull or fetch the code of the updated version of the file that been push from the github.
- pull request: Its is request to merge the changes of the current branch to the other branch. This is used when fellow groupmates or collaborator done its part and want to merge changes to the main branch.
- merge conflict: Its a conflict where there a different changes were made in the same part of the same file and git doenst know which changes should kept.

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]
First, I created a new branch to code without messing the main branch when we are making a system. After make a changes in my branch. I add the changes to the staging area. Then i commited the changes with a message that describe what was change. After that i push my branch to the github. In my github, i created a pull request from my kenneth branch to the main branch. After reviewed the changes and I submitted the pull request so that the changes could be checked before being merged.
```
git check -b kenneth

git add .
git commit -m"added new function"
git push -u origin kenneth


```

---

## A mistake I made (or one I want to avoid)

The mistake i made was making a changes in a wrong branch. I learned that I always to use git branch to know what branch I currently using and avoid making chnages in wrong branch. 

---

## How this connects to something else

Git connects to teamwork because git command branches allow collaborators to code and make changes in a seperated branches to avoid changing the main branch. This is also allow members pull request to review what changes before merging it to the main branch.
