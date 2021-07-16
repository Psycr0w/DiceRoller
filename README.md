# DiceRoller

Simple dice program to evaluate mutli-sided dice, fudge dice and exploding dice.

## Usage:

python roller.py

dicenumber = number of rolled dice.
mode = d, f, ! or s.

'd' will output the diceresults.

's' will output the sum of the dicerolls.

'!' will output exploding dice.

's!' will output the sum of exploding dice.

'f' is used for fudge dice. Since fudge dice are always the same, the input is <dicenumber>f.
number of sides = number of sides of the dice.


## example:


roller.exe 2s10 - will print the sum of two tensided dice.
  
roller.exe 3d6  - will print the output of 3 sixsided dice.
  
roller.exe 20!6 - will print the output of 20 6 sided exploding dice.
  
roller.exe 6f   - will print the output and sum of 6 fudge dice.
