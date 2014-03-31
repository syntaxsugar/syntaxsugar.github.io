Title: How to import existing code to GitHub
Date: 2014-03-31
Category: How to
Tags: GIT
Author: Jaromir Fojtu
Summary: Example, How to local source code add to a new remote git repository without 'cloning'

## Create the remote repository on [GitHub](http://github.com/)
![GitHub Create Repository]({filename}/images/github_create_repository.png)

## Locally, at the root directory of source code initialize repository

	:::bash
	git init

## Locally, add and commit what I want in my initial repo

	:::bash
	git add .
	git commit -m 'initial commit'

## Atach remote repository with the name *origin*

	:::bash
	git remote add origin [repo URL]

## Pull the remote branch

	:::bash
	git pull origin master

## Push up master branch

	:::bash
	git push origin master

	
