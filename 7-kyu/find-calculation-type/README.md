# Find the Operation

**Difficulty:** 7 kyu

## Problem Summary

Write a function that takes two operands and the result of an unknown arithmetic operation. Determine which operation—addition, subtraction, multiplication, or division—was used to produce the given result, and return its name.

## Examples

```text
Input: a = 1, b = 2, result = 3
Output: "addition"

Input: a = 5, b = 2, result = 2.5
Output: "division"

Input: a = 7, b = 3, result = 21
Output: "multiplication"
```

## Approach

Compare the given result against each possible arithmetic operation (`+`, `-`, `*`, and `/`) performed on the two operands. Return the name of the operation that matches the result.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Arithmetic operators
* Conditional statements
* Functions
* Comparison operators

## Notes

A straightforward kata for practicing arithmetic operations and conditional logic. It reinforces checking multiple conditions and returning the first matching result.
