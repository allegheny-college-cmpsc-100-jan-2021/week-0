# Worksheet 0.0.1: "Cloning" a repository
 
In this activity, we'll download this week's entire packet of files. 

## Table of contents
---

* [What is "cloning"?](#What-is-"cloning"?)
* [`clone` your repository](#Clone-your-repository)

## What is "cloning"?
 
---

While it may be tempting or convenient to think of this as _downloading_ something, that's not quite what "cloning" is. More accurately, a `clone` operation creates a _copy_ or _version_ of the group of files in a [repository](../README.md#"Repositories").

For any given repository, anyone with the permission to perform a `clone` creates a version of it. This version can then `commit` and `push` back to GitHub to update the original. We'll `commit` and `push` our work later.

## `clone` your repository

---

For this part of the activity:

* head over to our [course GitHub organization](https://github.com/allegheny-college-cmpsc-100-fall-2020) in a web browser
* Be sure to have a [terminal open in JupyterHub](../README.md/#Using-our-terminal)

1. Locate and click the repository with the name `cmpsc-100-jan-2021-week-0-YOUR GITHUB USERNAME`
  * This is the page for _your copy_ of my main repository
2. On the page, locate and click the green `Code` button in the upper(ish)-right
3. In the resulting popover, click the `Use SSH` link option
  * This allows us to `clone` these files using your SSH key
4. Copy the link beginning `git@`
  * For example, mine would look like:
    ```
    git@github.com:allegheny-college-cmpsc-100-jan-2021/cmpsc-100-jan-2021-week-0-dluman
    ```
5. In your terminal, be sure that you're in your home directory (`~`)
  * If unsure, type `cd` or `cd ~` and press `Enter`
  * Check where you are by typing `pwd` and pressing `Enter`
  * If the result looks like `/home/YOUR GITHUB USERNAME`, you're in the right place
6. When at the correct location, type `git clone THE LINK YOU COPIED IN STEP 4` and press `Enter`

## Finishing this activity

---

This operation should `clone` your copy of my repository to your JupyterLab. Verify by looking in the file tree at the left. Do you see a new folder named `cmpsc-100-jan-2021-week-0-YOUR GITHUB USERNAME`? If so, you're done.
