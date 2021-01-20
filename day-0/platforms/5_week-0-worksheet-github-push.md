# Worksheet 0.0.5: "Committing" to a repository

<div class="alert alert-block alert-warning">
    <p>This activity only works if we're in our JupyterLab environment. If you haven't finished the <a href = '1_week-0-worksheet-github-clone.md'>"Cloning" a repository</a> worksheet, please do so now.
</div>
 
We'll learn about the final steps we will take on a weekly basis to turn in or save work.

## Table of contents
---

* [Revisiting "repositories"](#Revisiting-"repositories")
* [Configuring your `git` settings](#Configuring-your-git-settings)
* ["Committing" to a repository](#"Committing"-to-a-repository)
* [Finishing this activity](#Finishing-this-activity)

## Revisiting "repositories"

---

Recall how we talked about repositories as "snapshots" of files at a given time? We're going to make a snapshot in this activity.

One thing I want to make clear first: you make as many of these "snapshots" of a repository as you want. I will only ever evaluate the latest one submitted before the deadline. Create them early and often. To make sure you see my red-boxed warning at the bottom of the [README](../README.md):

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll have the ability to restore up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>

So, use GitHub as a backup service for all of your work. This worksheet covers how you'll do that.

## Configuring your `git` settings

---

GitHub will let you `clone` repositories without really knowing who you are. To assign your name to the work you've done, though, it's is a different story.

In your terminal tab run the following commands (they are separate):

### To set your email address/identity
```
git config --global user.email "YOUR ALLEGHENY EMAIL"
```

### To set the name to display
```
git config --global user.name "YOUR GITHUB USERNAME"
```

## "Committing" to a repository

To be up-front: we use the word "commit" to describe a multi-step process of which the `commit` command is one part. However, we call the whole process `committing`.

There are three (3) parts in this process:

1. Adding files to "stage" a `commit`
2. Packaging a `commit` and labeling it with a descriptive message
3. `push`ing a `commit` to GitHub

<div class="alert alert-block alert-warning">
To perform this process, you must be in the main folder of your repository. For this exercise that means your <b>cmpsc-100-jan-2020-week-0...</b> main folder. If you use the <b>pwd</b> command, the output should reflect this.
</div>

### `add`ing files to "stage" a `commit`

In your terminal tab, type `git add .`

This command reads:

* `git` (program)
* `add` (command)
* `.` (all files)

Here, insofar as output goes, no news is good news: you shouldn't see anything.

### Packaging a `commit` and labeling it with a descriptive message

In your terminal, type:

```
git commit -m "DESCRIPTIVE COMMIT MESSAGE"
```

This command reads:

* `git` (program)
* `commit` (command)
* `-m` (flag, for `message`)
* `"YOUR DESCRIPTIVE MESSAGE"` (a message to display on GitHub)

<div class="alert alert-block alert-info">
    <b>Tip:</b> Please, please, please, always replace <b>DESCRIPTIVE COMMIT MESSAGE</b> with something different and...erm...actually <em>descriptive</em>.
</div>

The output of this message should look something like this:

```
dluman@jupyter-cs-allegheny-edu:~/week-0$ git commit -m "Updating files"
[main ed903d9] Updating files
 1 file changed, 10 insertions(+), 13 deletions(-)
```

That show that you put in some real #work.

This packages and "stages" the `commit` for transmission to GitHub -- the last step.

### `push`ing a `commit` to GitHub

Once you've staged it, type `git push`. The result should resemble:

```
Enter passphrase for key '/home/_faculty/dluman/.ssh/id_rsa': 
Enumerating objects: 31, done.
Counting objects: 100% (31/31), done.
Delta compression using up to 4 threads
Compressing objects: 100% (15/15), done.
Writing objects: 100% (18/18), 3.70 KiB | 1.23 MiB/s, done.
Total 18 (delta 10), reused 0 (delta 0)
remote: Resolving deltas: 100% (10/10), completed with 10 local objects.
To github.com:allegheny-college-sandbox/cmpsc-100-jan-2021-week-0.git
   e11834b..6064554  main -> main
```

The process will ask you to provide the password for your SSH key, and once that's done -- your work is on its way!

## Finishing this activity

Verify that your changes made it to your repository by visiting GitHub and clicking on your `cmpsc-100-fall-2020-week-00...` repository. You should see your name _and_ your message! If that's what you see -- you're done!