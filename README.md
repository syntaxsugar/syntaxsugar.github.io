syntaxsugar.github.io
=====================

    $ git checkout source
    $ git add content/my-new-awesome-blogpost.md
    $ git commit -m 'Added My new awesome blogpost'
    $ make publish
    $ make github

## Add new post

-   Create a new feature branch on *source*

        $ git checkout -b feature-xyz source

-   Add new content and commit changes to feature branch.

        $ git status
        $ git add <content/my-new-post.md>
        $ git commit

-   Merge changes into source branch

    Make sure the *source* branch is up to date

        $ git pull origin source

    Merge feature branch and delete it.
     
        $ git checkout source
        $ git merge feature-xyz
        $ git push
        $ git branch -d feature-xyz

    

