##Solutions of Exercises

> 1.1-1
Give a real-world example that requires sorting or a real-world example that requires computing a convex hull.

such as [the problem](convex-hulls) that computes the convex hull of any given set of n points in the plane efficiently. we need sort the sort the points by x-coordinate, and then computes the convex hull's set.

> 1.1-2
Other than speed, what other measures of efficiency might one use in a real-world setting?

space size.

> 1.1-3
Select a data structure that you have seen previously, and discuss its strengths and limitations.

Array

- Strengths:
	- Easier to use and access.
	- Faster access to the elements

- Limitations:
	- Fixed size
	- One block allocation
	- Complex position-based insertion

> 1.1-4
How are the shortest-path and traveling-salesman problems given above similar? How are they different?

- similar: Both of them are seeking the lowest overall distance.
- different: shortest-path is the problem of finding a path between two vertices(or nodes); traveling-salesman is the problem of finding the shortest possible route that visits each city exactly once.(and TSP is NP-hard)

> 1.1-5
Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is "approximately" the best is good enough.

Given a set of integers, finding the maximum one is only the best solution will do, but finding any non-empty subset of them add up to zero is "approximately" the best is good enough.
