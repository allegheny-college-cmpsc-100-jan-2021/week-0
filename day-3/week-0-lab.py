#!/usr/bin/env python3

ballot = {}

# TODO: Complete the "voting algorithm" to
#       1. Accept inputs one and a time, either:
#          a. Incrementing candidate's vote count by 1 in ballot
#          b. Setting the candidate's vote count to 1 in ballot for the first vote
#       2. Stop accepting inpus if the N character entered

winner = None
max_votes = 0

# TODO: Iterate over the ballot dictionary
#       1. Get a each candidate's vote count one by one
#       2. Print the amount of votes that candidate received anf their name
#       3. Check to see if this candidate has a new vote maxiumum


print(f"The winner is {winner} -- with {max_votes} votes.")