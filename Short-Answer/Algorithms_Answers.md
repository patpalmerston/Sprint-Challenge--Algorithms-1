#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
a is a constant of O(1)
n is changed n times so O(n3) is still O(n)
a equal to a plus the n's has n changing O(n) times

so I would believe this to be O(n)

b)
the sum is constant O(1)
the loop changes n times making it O(n)
j equal to one is constant O(1)
j changes in the inside loop depending on n so O(n^2)
sum changes by one O(1)

so I would believe this to be O(n^2)

c)
out base case is O(1)
our return takes an O(1) and adds it to a single recursive function O(n)

so I would guess this to be O(n)

## Exercise II

-for this excersize I would use a divide and conquer technique.
-find the mid point point of the building by adding a min variable equal to the starting index
-and a max variable equal to the length of the array
-run a loop while min is less or equal to max
-create a variable of mid equal to min + max divided by two and rounded down
-if we drop the egg from mid and it breaks then mid becomes the new top
-if we drop the egg and it does not break then mid becomes the new floor
-then we split again and continue doing so until we find the max floor from which the egg can drop but not break
-that is the 'f' floor

we would be using O(log n) run time complexity
