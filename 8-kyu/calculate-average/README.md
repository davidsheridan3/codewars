# Calculate Average

**Difficulty:** 8 kyu

## Problem Summary

Write a function that calculates and returns the average of the numbers in a given array. If the array is empty, the function should return `0`.

## Examples

```text
Input: [1, 2, 3]
Output: 2.0

Input: [5, 10]
Output: 7.5

Input: []
Output: 0
```

## Approach

First, check whether the array is empty. If it is, return `0`. Otherwise, calculate the sum of all numbers using `sum()`, divide it by the number of elements using `len()`, and return the resulting average.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Concepts Practiced

* Lists
* Built-in functions (`sum()`, `len()`)
* Conditional statements
* Arithmetic operations
* Functions

## Notes

This kata is a good introduction to working with lists and Python's built-in functions. It also reinforces the importance of handling edge cases, such as an empty list, before performing calculations.
