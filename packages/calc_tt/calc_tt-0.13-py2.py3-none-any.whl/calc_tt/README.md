Hello!

My calculator can do these actions:
* Adding
* Subtracting
* Multiplication
* Division
* n-th root

It is failsafed against zero division, entering wrong input.

The algebra action count is capped at 6.

How to run:

pip3 install calc_tt

from calc_tt import Calculator

instance = Calculator.Calculator()

instance.run()