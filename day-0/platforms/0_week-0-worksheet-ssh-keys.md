# Worksheet 0.0.0: Securing your GitHub account

In this activity, we'll secure your GitHub account using an SSH key.

## Table of contents

---

* [Overview](#Overview)
* [Steps to create an SSH key](#Steps-to-create-an-SSH-key)
* [Adding the key to GitHub](#Adding-your-key-to-GitHub)
* [Finishing this activity](#Finishing-this-activity)

## Overview

---

This may seem like an extra step -- and it is. But, it's an important one. Completing this activity will allow you to retrieve course content in a more secure way than logging into GitHub _and_ will streamline the process of working with repositories.

Big promises, but -- trust me -- they're true.

Now that you have some familiarity with a terminal, I'm going outsource explaining how to generate a key to...myself. 

Click the image below to watch a short video about creating SSH keys. There's an activity in the video that you can follow to generate your own key on this server (in your terminal).

A step-by-step outline follows the video, if you're into the tl;dr.

(But watch the video; it appeals to my vanity.)

[![YouTube thumbnail](https://i3.ytimg.com/vi/qEPjUGQFmzQ/hqdefault.jpg)](https://www.youtube.com/watch?v=qEPjUGQFmzQ)

## Steps to create an SSH key

1. Open a [terminal](../README.md#Using-our-terminal)
2. At the prompt, type (or copy and paste): `ssh-keygen -t rsa -b 4096 -C "YOUR ALLEGHENY EMAIL"`
3. When asked for a location at which to save the key, leave it blank to accept the default value and press `Enter`
4. Provide a password for the key when the system asks
  * When typing characters at the prompt, no text will appear -- this is normal
  * `ssh-keygen` will request your password twice to ensure you've got it right

Your key files (private/public) live at the following location: `~/.ssh/`.

## Adding your key to GitHub

1. In the terminal, type (or copy and paste): `cat ~/.ssh/id_rsa.pub`
  * This should print something that looks like gibberish to your screen
2. Copy the output starting at `ssh-rsa` to the end (your Allegheny email address)
3. Head over to [GitHub](https://www.github.com)
4. Locate and click your profile picture in the upper right corner of the screen
5. Select `Settings` from the resulting menu
6. On the next page, locate and click the `SSH and GPG keys` menu item
7. Click the `New SSH key` button (it's green)
8. Title your key something descriptive
  * I'll offer: `Allegheny CS JupyterLab`
  * Copy and paste that, if you like
9. Paste the gibberish in the `Key Field`

## Finishing this activity

---

We'll also know you've successfully completed this step if you can complete the rest of the activities in this week's packet.