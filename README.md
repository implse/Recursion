# Recursion and Backtracking

# Recursion

Functions that call themselves to solve problems that are recursive in nature.

When a function calls itself, its called Recursion

  - Powerful substitute for iterations.(for loop)
  - Well suited to solving certain types of problems.
  - Leads to elegant and simplistic short code.
  - Functional programming (Haskell) use recursion exclusively.

Occurs in many places in code and real world :

  - Nested structures (trees, file folders, collections) can be self similar.
  - Patterns can contain smaller versions of the same pattern.
  - Shell, plants, mountains, etc.

Every recursive algorithm involves at least 2 cases:

  - Base case : A simple occurrence that can be answered directly. Terminate the recursive process.


  - Recursive case : A more complex occurrence of the problem that cannot be directly answered, but can
  instead be described in terms of smaller occurrence of the same problem.


Number of Recursive calls : There is an upper limit to the number of recursive calls that can be made. To prevent this make sure that your base case is reached before stack size limit exceeds. (stack overflow error)

## Call Stack

When you call a function, the system sets aside space in memory for that function to do its necessary works.

We frequently call such chunks of memory stacks frames or function frames.

These frames are arranged in a stack. The frame for the most recently called function is always on the top of the stack.

When a new function is called, a new frame is pushed onto the top of the stack and becomes the active frame.

When a function finishes its works, its frame is popped off of the stack, and the frame immediately below it becomes the new active function on the top of the stack. This function pick up immediately where it left off.
