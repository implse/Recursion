# Write a recursive function diceRoll that accepts an integer representing a number of 6 sided dice to roll, and output all possible combinations of values that could appear on the dice.

def diceRoll(dice):
  def diceRoll_helper(dice, chosen=[]):
    # Base case
    if dice == 0:
      print(chosen)
    else:
      # Recursive case
      for i in range(1, 6+1):
        # choose
        chosen.append(i)
        # explore
        diceRoll_helper(dice-1, chosen)
        # unchoose
        chosen.pop()
  return diceRoll_helper(dice, chosen=[])

# Test
diceRoll(2)
