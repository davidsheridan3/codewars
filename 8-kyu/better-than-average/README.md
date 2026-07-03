# Better Than Average

**Difficulty:** 8 kyu

## Problem Summary

Write a function that compares your test score against the average score of your classmates. Return `True` if your score is higher than the class average; otherwise, return `False`.

## Examples

```text
Input: class_points = [2, 3], your_points = 5
Output: True

Input: class_points = [100, 90, 80], your_points = 85
Output: False
```

## Approach

Calculate the average of the class scores by summing all values in the list and dividing by the number of students. Compare your score with the calculated average and return the appropriate boolean value.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Concepts Practiced

* Lists
* Built-in functions (`sum()`, `len()`)
* Arithmetic operations
* Conditional statements
* Functions

## Notes

A good beginner kata for working with lists and Python's built-in functions. It reinforces calculating averages and returning boolean values based on a comparison.
