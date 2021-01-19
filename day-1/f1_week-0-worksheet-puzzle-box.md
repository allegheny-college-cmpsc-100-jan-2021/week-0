# Worksheet 0.1.f1: The puzzle box

Of course, G. Wiz has a brand new puzzle box with `3` buttons, each of which has two-states ("pressed" -- `True`, "unpressed" -- `False`). Largely because gators lack thumbs, partly because G. Wiz is _very_ impatient, we need to figure out how to open it.

Our goal is to demonstrate how to open the puzzle box using the correct combinations of buttons. We need to combine our knowledge of these buttons (`booleans`) and what we've learned about `list`s with our new power of the `if` statement to figure out how to express the solution combination.


|Combination number |`buttons[0]` |`buttons[1]` |`buttons[2]` |
|-------------------|-------------|-------------|---------------|
|1|`True` |`False` |`True`|
|2|`True` |`False` |`False`|
|3|`True` |`True` |`False`|
|4|`False` |`False` |`False`|
|5|`True` |`True` |`True`|
|6|`False` |`False` |`True`|
|7|`False` |`False` |`False`|
|8|`True` |`True` |`True`|
|9|`False`|`True` |`False`|

One of these combinations is the "winner." Which is it?

## Notes

---

This work should be completed in the [f1_week-0-worksheet-puzzle-box.py](f1_week-0-worksheet-puzzle-box.py) file. Recall that, during class, this is the way Python development is largely done. While we will still use notebooks like worksheets, when it comes to to real programming jobs, we're going to start getting the habit of programming real programs in `*.py` files.

There's already some code in the file to get you started.