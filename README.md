# Recursion and Backtracking

Recursion is one of the most fundamental concepts in computer science, it helps break complex problems into simple parts.

# Recursion

Functions that call themselves to solve problems are recursive in nature.

When a function calls itself, its called `recursion`

  - Powerful substitute for `iterations`. (`for loop`)
  - Well suited to solving certain types of problems.
  - Leads to elegant and simplistic short code.
  - Functional programming (`Haskell`) use recursion exclusively.

Occurs in many places in code and real world :

  - Nested structures (`trees`, `file folders`, `collections`) can be self similar.
  - Patterns can contain smaller versions of the same pattern.
  - Shell, plants, mountains, etc.


A `recursive function` invoke the same `function` with a different `input` until you reach the `base case`.


Every recursive algorithm involves at least 2 cases:

  - `Base case` : A simple occurrence that can be answered directly. Terminate the recursive process. (start `unwinding recursion`)


  - `Recursive case` : A more complex occurrence of the problem that cannot be directly answered, but can
  instead be described in terms of smaller occurrence of the same problem.


Number of Recursive calls : There is an upper limit to the number of recursive calls that can be made. To prevent this make sure that your base case is reached before `stack size limit` exceeds. (`stack overflow error`)

### Common Recursive Algorithms

  - Fibonacci, Factorial
  - Merge Sort, Quick Sort
  - Binary Search
  - Tree traversals (in-Order, pre-Order, post-Order)
  - Graph Traversals (Breadth First Search and Depth First Search)
  - Dynamic Programming
  - Divide and Conquer Algorithms
  - Backtracking Algorithms

### Easiest Way to Approach a Recursive Problem

  - Figure out the `base case`
  - Assume `subproblems` can be solved by `recursion` (automatically)
  - Using the `subproblems` write the answer for the current problem


## Call Stack

When you call a function, the system sets aside space in `memory` for that function to do its necessary works.

We frequently call such chunks of memory `stacks frames` or `function frames`.

These frames are arranged in a `stack`. The `frame` for the most recently called function is always on the top of the `stack`.

When a new function is called, a `new frame` is pushed onto the top of the `stack` and becomes the active `frame`.

When a function finishes its works, its `frame` is popped off of the `stack`, and the `frame` immediately below it becomes the new active function on the top of the `stack`. This function pick up immediately where it left off.


## Stages of a Recursive Algorithm

There are two stages to a recursive algorithm:

  - What happens `before` we reach the `base case`.
  - What happens `after` we reach the `base case`.

These stages are called `winding` and `unwinding`.

## Recursive Algorithm Complexity

### Time Complexity

To evaluate recursive algorithm `time complexity` we need to follow this steps:

  - Calculate the `time complexity` of a single call (single call complexity : cost 1)

  - Express the number of recursive calls through input parameters

  - Multiply the number of recursive calls by a single call complexity


To build the formula, you need to look at :

  - Single call complexity

  - The number of recursive calls

  - Levels number in the call tree

### Space Complexity

The maximum `space` consumed by a recursive program is proportional to the maximum `depth` of the `recursion tree`.

The maximum `depth` of the `recursion tre`e is defined as the `length` of the longest `path` in the `tree`.



# Backtracking

`Backtracking` is an effective technique for solving algorithmic problems. In `backtracking`, we search `depth-first` for solutions, `backtrack` to the last valid path as soon as we hit a dead end.

`Backtracking` reduces the search space since we no longer have to follow down any paths we know are invalid. This is called `pruning`. We must be able to test partial solutions.

If decisions doesn't work, step back and make another decision with different choice.

`Backtracking` is often much faster than `brute force` enumeration of all complete candidates, because it can eliminate a larger number of candidates with a single test.


## Backtracking Approach

  - Design a `recursive` function to return `success` or `failure`.
  - At each call, choose one option and go with it.
  - Recursively proceed and see what happens.
  - If it works out continue, otherwise unmake choice and try again.
  - If no option worked, return fail result which triggers backtracking.(un-making earlier decisions)

An algorithm `backtrack` when the current solution is invalid.

Most problems uses `backtracking`.

### Backtracking Problems:

  - Depth First search.
  - N Queens.
  - Sudoku
  - Knapsack problem. (depends on implementation)

### Non Backtracking Problems

  - Find all permutations.
  - Stairs case problem.


## Recursion vs Iteration

  - All recursive problem can be solved iteratively and vice versa.
  - If equal time complexity, iterative is usually faster.
  - Converting from recursive to iterative:
      - Not always easy to do.
      - Can you iteratively compute larger subproblems.
      - Can you emulate the recursive stack using other data structure.

## Uses of Recursion

  - Traversing hierarchical data structures, such as DOM tree, XML, file systems.
  - Data mining using web crawlers.
  - Used in compilers and linkers in the software build process.
  - Evaluation of arithmetic expressions.
  - Passing technical interviews.


## Handling Recursion Limit in Python

When `recursion` is called, frames containing data for each successive call are added to the `stack`.

Python has a limit for recursive call to avoid using up to much memory.

`maximum recursion depth exceeded error`

The `sys` module in Python provides a function called `setrecursionlimit()` to modify the recursion limit in Python.

It takes one parameter, the value of the new recursion limit. By default, this value is usually `10**4`.

```
import sys

sys.getrecursionLimit()

sys.setrecursionLimit(increase_the_number)


```
## Caching With @lru_cache

`functools` module comes with the `@lru_cache` decorator, which gives you the ability to cache the result of your functions using the Least Recently Used (LRU) strategy.

`@lru_cache` uses a dictionary behind the scenes. It caches the function’s result under a `key` that consists of the call to the function, including the supplied arguments. These arguments have to be `hashable` for the `decorator` to work.

```
from functools import lru_cache

@lru_cache(maxsize = 128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

```

## The Six Recursive Core Patterns

  - `Iteration` : Any problem that can be solved iteratively can be solved using recursion. Iterate over of variety of data-structure. (tree, linked list)

  - `Sub-problem`: If a problem can be break down into its sub-problems then we can use this to solve any recursive problems.

  - `Selection`: Use combination. It is the most common pattern to come up in recursion and dynamic programming. In this pattern, we are going through all the possible solutions and selecting the ones which match our condition. (0/1 Knapsack, N-Queens)

  - `Ordering` : Use permutations to solve many common recursive problems.(similar to selections except order matters)  By combining the selection and ordering pattern, you can cover a great number of recursive problems.

  - `Divide and Conquer` : Divide and conquer is the core of many algorithms such as merge sort, binary search.

  - `Depth First Search`:
