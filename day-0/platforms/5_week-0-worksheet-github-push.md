# Worksheet 0.0.f2: G. Wiz and the lousy lottery

![Paper chase](https://raw.githubusercontent.com/allegheny-college-sandbox/cmpsc-100-spring-2020-lab-04/media/media/g-wiz-lousy-lottery.png)

## Overview

---

G. Wiz is a wizard. A gator wizard, but still a wizard. And, they're a wizard who likes fancy wizard hats (like many). To fund their hat obsession, they play the Gator Kingdom Lottery frequently. And, after losing for many, many weeks, they decided to do someting slightly less-than-ethical. They dug out their crystal ball and predicted the lottery numbers.

Needless to say, they won this week. However, they didn't take a look at the prize pool and won substantially less than hoped for: only $1000; still a non-trivial sum (to be fair).

But, to add to their list of woes: G. Wiz isn't so good with money. They forgot that the Gator Kingdom charges a 9% tax on lottery winnings, so they take home just a bit less than the advertised number. Regardless, G. Wiz took a trip to the office to claim their prize and was still feeling a bit excited to be so flush with cash on the way home.

Braving the soon-to-be autumnal cold, some CrocScouts outside a magazine stand were advertising cookies for $10.00 a box. Being expert marketers, the CrocScouts drove a hard bargain with our gator friend and managed to sell them 5 boxes.

Having paid the scouts, the latest edition of the gossip magazine _The Clawparazzi_ caught G. Wiz's eye from the far side of the magazine rack. Ever a conaisseur of the latest celebrity gossip, they bought an issue for the $5.00 cover price, and had to pay the same 9% sales tax on top of that.

Just minutes after arriving home, they heard a knock at the door -- a few of G. Wiz's friends (Slippy Toad, Frogger, and Chompers) stopped by to honor an old promise that if any one of them ever won the Gator Kingdom lottery, they'd split it 4 ways. (In the Gator Kingdom, the lottery winner's name is published the day of the drawing, and G. Wiz's friends are avid players.)

Finally settling down to count what was left over, G. Wiz needs to determine if they can afford a $215.00 hat (don't forget the tax!).

And where do you come in? You can help G. Wiz account for everything they've paid out by making a ledger that lists each of their transactions and comes to the final conclusion as to whether or not they can afford their hat. Such a ledger looks like the following, with each of the `######` replaced by the actual expenditures plus a last line printing the amount that they have left.

### Required output

```
How G. Wiz spent their lottery money
Initial amount: 1000.0
Taxes paid: ######
CrocScout cookies: ######
Latest Clawparazzi: ######
Owed to friends: ######
Amount remaining: ######
```

### tl;dr

* G. Wiz is a wizard.
  * Very important
* They predicted the winning lottery numbers this week.
* They won `$1000`.
* The lottery charges a `9%` tax on all winnings
* After getting their winnings, they bought `5` boxes of CrocScout cookies at `$10.00` each (no tax -- it's for a good cause, after all)
* G. Wiz loves Gator Kingdom gossip; buys a _Clawparazzi_ for `$5.00` (don't forget `9%` tax!)
* 3 friends came over, reminded G. Wiz of their obligation to split the winnings equally

Bottom line: can G. Wiz afford a `$215.00` hat?

Your job is to write a program that keeps track of all these transations in variables and poses the question is some _total amount_ left over _greater than_ `215.00`?

### Evaluation

This work will be evaluated on completeness and correctness. This means:

* `0` `TODO` markers
* At least `7` `print` statements
* At least `6` `str` statements (to print calculation results)
* Correct output -- given in the grader readout

## Notes

---

This work should be completed in the [f2_week-0-worksheet-lousy-lottery.py](f2_week-0-worksheet-lousy-lottery.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in `*.py` files.

There's already some code in the file to get you started.