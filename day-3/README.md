### CMPSC 100: G. Wiz and the Ballot Bonanza

![GO VOTE](https://cs.allegheny.edu/sites/dluman/cmpsc100/cmpsc-100-ballot-bonanza.png)

<div class="alert alert-block alert-warning" id = "warning">
The work this week also offers the opportunity to tie up the server in loopish operations. Should you be unable to run cells, simply locate the <b>Kernel</b> menu at the top of the screen and click <b>Interrupt Kernel</b>. This should jumpstart the kernel again and clear out the infinite loop behavior.</div>

At times in a Gator's life, it's important to consider whether on not to get involved in the political process beyond merely being a voter. Realizing that they might make a very good Pond Representative, G. Wiz recently confronted this democratic _raison d'etre_. In a fiercely fought campaign against several other reptile representative candidates, G. Wiz awaits the election results from a fancy new computerized system which promises extremely fast results. May the...most...voted...for reptile win?

The only problem is that _you_ have to write the machine. 

You've been given some test data, but the real votes will be counted when the `gradle grade` process runs.

## General guidelines for laboratory sessions

---

* Follow steps carefully. Laboratory sessions often get a bit more complicated than their preceeding course sessions. Especially for early sessions which expose you to platforms with which you may not be familiar, take notes on commands you run and their corresponding effects/outputs. If you find yourself stuck on a step, let a TL or the professor know! Laboratory sessions do not mean that we won't guide you in the same way we do during other sessions.
* Regularly ask and answer questions. Some of you may have more experience with the topics we're discussing than others. We can use this knowledge to our advantage. Let students try things for a while before offering help (always offer first). To ask questions, use your group's Slack channel or TL channels.
* Store and transfer files using GitHub. Various forms of file storage are more or less volatile. You are responsible for backing up and storing files. If you're unsure of files which have been changed, you can always type git status in the terminal for your working folder to determine what you need to back up.
* Keep all of your files. See above, but also remember that you're responsible for the files you create.
* Back up your files regularly. See above (and above-above).
* Review the Honor Code regularly when working. If you're taking a solution from another student or the Internet at-large (especially Stack Overflow), bear in mind that using these solutions can constitute a form of plagiarism that violates the Allegheny Honor Code. While it may seem easy and convenient to use these sources, it is equally easy and convenient to rely on them and create bad habits which include not attributing credit or relying exclusively on others to solve issues. Neither are productive uses of your intellect. Really.

## Requirements

---

### This notebook

Your program should:

* Create a `dict` called `ballot`
* Take input of a candidate names until `N` entered at prompt
  * Use the identifier `choice` to store and test this `input`
* Add one vote to the selected candidate's vote total
* Using a `for` loop, `print`, according to [sample output](#Sample-output) below:
  * vote totals for all candidates
  * the name of the winner
  
Note: your test data will not be as extensive as the data used by the grader; your work should satisfy both test and grader cases

#### Hint(s)

* Determining the winner may use an `if` statement

### `reflection.md`

* At least 300 words
* Responds to all questions
* Contains `0` `TODO` markers

### Test data

|Candidate | Votes |
|----------|-------|
|G. Wiz    | 6     |
|Frogger   | 3     |
|Slippy Toad | 4   |
|Lyle Crocodile| 5   |
|Yertle Turtle | 2   |

### Sample output

```
Enter a candidate's name ([N]o to quit):  Frogger
Enter a candidate's name ([N]o to quit):  Frogger
Enter a candidate's name ([N]o to quit):  G. Wiz
.
.
.
.
.
.
Enter a candidate's name ([N]o to quit):  N

Frogger received 2 votes.
G. Wiz received 1 votes.
The winner is: Frogger
```

## Notes

This work should be completed in the [week-0-lab.py](week-0-lab.py) file.