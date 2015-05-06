**Q1: What is the set of points at equal Manhattan distance to some point?**

![image](https://cloud.githubusercontent.com/assets/1147451/7485877/dac2f8d4-f3ce-11e4-9990-86fb53c4033a.png)

It is exactly a **circle** to point `p`, which the center is on the point `p`.

**Q2: How can the distance between two line segments be realized?**

Find the minimum distance between two points that are part of each line.

see #1.

**Q3: How many intersection points can a line and a circle have?**

0, 1 or 2.

**Q4: What are the possible outcomes of the intersection of a rectangle and a quadrant?**

nothing, rectangle or polygon.

**Q5:  What is the maximum number of intersection points of a line and a simple polygon with 10 vertices (trick question)?**

don't know.

**Q6: What is the maximum number of intersection points of a
line and a simple polygon boundary with 10 vertices (still a trick question)?**

don't know.

**Q7: What is the maximum number of edges of a simple polygon boundary with 10 vertices that a line can intersect?**

don't know.

**Q8: Suppose that a simple polygon with n vertices is given; the vertices are given in counterclockwise order along the boundary. Give an efficient algorithm to determine all edges that are intersected by a given line.**

**Q9: Which of the following shapes are convex? Point, line segment, line, circle, disk, quadrant?**

All, in addition to Point.

> For any subset of the plane (set of points, rectangle, simple polygon), its **convex hull** is the smallest convex set that contains that subset.

-----

**Give an algorithm that computes the convex hull of any given set of n points in the plane efficiently**

see [pseudo code](convex-hull-pseudo-code.pdf)

-----

Reference: [Introduction and convex hulls](CG1-Introduction-convex-hulls.pdf)
