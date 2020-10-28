# progress-bar

https://ironcladinfosec.com/ansi-escape-codes/


Colored progress bar using ANSI escape codes in python

The trick here is to move the cursor to the far left (using the D code), clearing the screen then re-printing the whole bar adding the progress to it.
The default bar length is set to 100, which can be changed using -b switch

usage: load_progress.py [-h] [-b] [-e] [-c] [-s]

Custom loading bar.

optional arguments

  -h, --help        show this help message and exit
  
  -b , --bar        desired length of bar
  
  -e , --elements   number of elements
  
  -c , --color      Color of bar (red, yellow, green
  
  -s , --symbol     Symbol to use in a bar
