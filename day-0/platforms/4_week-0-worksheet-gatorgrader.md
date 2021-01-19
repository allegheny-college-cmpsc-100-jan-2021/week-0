# Worksheet 0.0.4: GatorGrader

<div class="alert alert-block alert-warning">
    <p>This activity only works if we're in our JupyterLab environment. If you haven't finished the <a href = '1_week-0-worksheet-github-clone.md'>"Cloning" a repository</a> worksheet, please do so now.
</div>

## Table of contents

---

* [What is GatorGrader?](#What-is-GatorGrader?)
* [Checking your work](#Checking-your-work)
* [Finishing this activity](#Finishing-this-activity)

## What is GatorGrader?

---

GatorGrader is an Allegheny College-developed, student-written and maintained application that grades your work for you. The long and short of it, before and when you turn in your assignments, you can know what your approximate grade will be.

(It doesn't do _everything_ for us, but it gives us a good starting point for evaluating your work.)

You don't need to do anything to get it -- I will distribute all the files you need with every repository. You realize the following benefits:

* Complete grading transparency
* Grading criteria _never_ changes
* The criteria is very specific; you will know what changes you need to make

This application runs in your terminal tab, and can grade:

* The whole repository
* Just worksheets
* Just the lab

## Checking your work

---

No matter where you are in your repository, the command to start and run GatorGrader is always the same:

```
gradle grade
```

However, you need to be _in the right place_ to get the right result. We're going to walk through a grading scenario using our `platforms` directory.

<div class="alert alert-block alert-warning">
    <p>Today is a bit different than future days; given that today's lessons are split between <b>platforms</b> and <b>python-basics</b> each folder is graded <em>separately</em>.</p> 
    <p>In the future, simply grade the <b>day-{N}</b> directory directly. We'll walk through this a few times in the coming days.</p>
</div>

If you don't already have a terminal tab open, open one now.

### Grading worksheets

1. From your terminal, `cd` to the `worksheets` directory.
2. In your terminal, type `gradle grade`

The output of your command should look like the following:

```
✔  The file the_maltese_python! exists in the cage directory
✔  The 3a_week-0-worksheet-markdown.md in  has at least 3 of the 'heading' tag
✔  The file 2_week-0-worksheet-basic-terminal.ipynb exists in the  directory
✔  The command output has exactly 0 of the 'TODO' fragment
✔  The file f1_week-0-platforms-final-activity.ipynb exists in the  directory
✔  The 3a_week-0-worksheet-markdown.md in  has at least 1 of the 'image' tag
✔  The file 3a_week-0-worksheet-markdown.md exists in the  directory
✔  The command output has exactly 0 of the 'TODO' fragment
✔  The 3a_week-0-worksheet-markdown.md in  has at least 1 paragraph(s)
✔  The file id_rsa exists in the ssh directorylete!
✔  The 3a_week-0-worksheet-markdown.md in  has at least 2 of the 'list' tag


        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Passed 11/11 (100%) of checks for cmpsc-100-week-0-day-0! ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


BUILD SUCCESSFUL in 8s
3 actionable tasks: 3 executed
```

> (I'm a good student.)

## Finishing this activity

Did you see the result you expected or wanted? If so, great! If you have some things to fix, run back through the worksheets and lab sheets to zero-in on the areas you need work on.

If the above didn't happen the way you thought it might, depending on the output, you should [schedule office hours with me](https://www.cs.allegheny.edu/sites/dluman/) to troubleshoot!