# Get the Floor Number

**Difficulty:** 8 kyu

## Problem Summary

Write a function that converts a floor number from the American numbering system to the European numbering system.

* The American **1st floor** becomes the European **ground floor (0)**.
* There is **no 13th floor** in the American system, so floors above 13 are shifted down by two.
* Basement floors (negative numbers) remain unchanged.

## Examples

```text
Input: 1
Output: 0

Input: 5
Output: 4

Input: 15
Output: 13

Input: -3
Output: -3
```

## Approach

Use conditional statements to handle the different cases:

* If the floor is less than or equal to `0`, return it unchanged.
* If the floor is between `1` and `12`, subtract `1`.
* If the floor is `13` or higher, subtract `2` to account for both the missing ground floor numbering and the omitted 13th floor.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Conditional statements
* Integer arithmetic
* Functions
* Problem decomposition

## Notes

This kata is good practice for breaking a problem into distinct cases and applying the correct transformation for each one. It reinforces thinking through edge cases before writing the implementation.
