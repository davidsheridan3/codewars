# Check Same Case

**Difficulty:** 8 kyu

## Problem Summary

Write a function that determines whether two given characters are letters of the same case.

* Return `1` if both characters are letters and have the same case.
* Return `0` if both characters are letters but have different cases.
* Return `-1` if either character is not a letter.

## Examples

```text
Input: 'a', 'g'
Output: 1

Input: 'A', 'C'
Output: 1

Input: 'b', 'G'
Output: 0

Input: 'B', 'g'
Output: 0

Input: '0', '?'
Output: -1
```

## Approach

First, verify that both characters are alphabetic using Python's `isalpha()` method. If either character is not a letter, return `-1`. Otherwise, compare their cases using `islower()` or `isupper()`. Return `1` if both characters share the same case, or `0` if they differ.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* String methods (`isalpha()`, `islower()`, `isupper()`)
* Conditional statements
* Boolean expressions
* Functions

## Notes

This kata is a good introduction to Python's built-in string methods for working with characters. It reinforces input validation before applying additional logic and demonstrates how boolean expressions can simplify conditional checks.
