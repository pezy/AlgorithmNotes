##Solutions of Exercises

### 1.1-1
> Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

such as [the problem](convex-hulls) that computes the convex hull of any given set of n points in the plane efficiently. we need sort the sort the points by x-coordinate, and then computes the convex hull's set.

### 1.1-2
> Other than speed, what other measures of efficiency might one use in a real-world setting?

space size.

### 1.1-3
> Select a data structure that you have seen previously, and discuss its strengths and limitations.

Array

- Strengths:
	- Easier to use and access.
	- Faster access to the elements

- Limitations:
	- Fixed size
	- One block allocation
	- Complex position-based insertion

### 1.1-4
> How are the shortest-path and traveling-salesman problems given above similar? How are they different?

- similar: Both of them are seeking the lowest overall distance.
- different: shortest-path is the problem of finding a path between two vertices(or nodes); traveling-salesman is the problem of finding the shortest possible route that visits each city exactly once.(and TSP is NP-hard)

### 1.1-5
> Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is "approximately" the best is good enough.

Given a set of integers, finding the maximum one is only the best solution will do, but finding any non-empty subset of them add up to zero is "approximately" the best is good enough.

### 1.2-1
> Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

Routing in network, finding next node, would request Dijkstra algorithm. It could find the shortest paths between nodes.

### 1.2-2
> Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in 8n2 steps, while merge sort runs in 64n lg n steps. For which values of n does insertion sort beat merge sort?

from `2` to `43`.

```py
import math

for n in range(2, 100):
	if 8 * n * n >= 64 * n * math.log(n, 2):
		print(n)
		break
```

### 1.2-3
> What is the smallest value of n such that an algorithm whose running time is 100*n^2 runs faster than an algorithm whose running time is 2^n on the same machine?

n == 15

```py
import math

for n in range(1, 100):
	if 100 * n * n < math.pow(2, n):
		print n
		break
```

### Problems 1-1
> For each function `f(n)` and time `t` in the following table, determine the largest size `n` of a problem that can be solved in time `t`, assuming that the algorithm to solve the problem takes `f(n)` microseconds.

check and run [calc.py](calc.py)
see [P1-1.pdf](P1-1.pdf)

### 2.1-1
> Using Figure 2.2 as a model, illustrate the operation of `INSERTION-SORT` on the array `A = <31, 41, 59, 26, 41, 58>.`

```
31 [41] 59 26 41 58
31 41 [59] 26 41 58
31 41 59 [26] 41 58
26 31 41 59 [41] 58
26 31 41 41 59 [58]
26 31 41 41 58 59
```

### 2.1-2
> Rewrite the `INSERTION-SORT` procedure to sort into nonincreasing instead of non- decreasing order.

[procedure](nonincreasing-insertion-sort.pdf) |
[code](insertion_sort.py) |
[unittest](insertion_sort_unittest.py)

### 2.1-3
> Consider the searching problem:

> **Input**: A sequence of n numbers `A = <a1, a2,...,an>` and a value v􏰁.

> **Output**: An index i such that `v = A[i]` or the special value NIL if 􏰁v does not
appear in A.

> Write pseudocode for linear search, which scans through the sequence, looking for 􏰁v. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

**loop invariant**: At the start of each iteration `for` loop, the `v` does not appear in the subarray `A[1,...,j-1]`.

**Initialization**: We start by showing that the loop invariant holds before the first loop iteration, when `j` == 1. The subarray is empty. therefore, we can't find `v` in an empty array, which shows that the loop invariant holds prior to the first iteration of the loop.

**Maintenance**: Next, we tackle the second property: showing that each iteration maintains the loop invariant. Informally, the body of the `for` loop works by comparing `A[1]` with `v`, if they are equal, we return index `j`, which is the result we want. Otherwise, we move to next element of the array, then preserves the loop invariant.

**Termination**: Finally, we examine what happens when the loop terminates. The loop terminates when `j` equal to the `A.length`, we have that the subarray A[1..n] consists of the elements originally in A[1..n], but `v` does not appear. Observing that the subarray A[1..n] is the entire array, we conclude that `v` does not appear in A. Hence, the algorithm is correct.

[pseudocode](linear-search.pdf) | [code](insertion_sort.py) |
[unittest](insertion_sort_unittest.py)

### 2.1-4
Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n+1)-element array `C`. State the problem formally and write pseudocode for adding the two integers.

**Input**: Two n-bit binary integers, `A=<a1,...,an>` and `B=<b1,...,bn>`.
**Output**: An (n+1)-element array, `C=<c1,...,cn>` which is the sum of the two input integers.

[pseudocode](add-binary.pdf) | [code](insertion_sort.py) |
[unittest](insertion_sort_unittest.py)
