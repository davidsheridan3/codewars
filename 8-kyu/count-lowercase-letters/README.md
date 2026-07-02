# Count Lowercase Letters

**Difficulty:** 8 kyu

## Problem Summary

Write a function that counts and returns the total number of lowercase letters in a given string. All other characters, including uppercase letters, numbers, symbols, and whitespace, should be ignored.

## Examples

```text
Input: "abc"
Output: 3

Input: "abcABC123"
Output: 3

Input: ""
Output: 0
```

## Approach

Iterate through each character in the string and check whether it is a lowercase letter using Python's `islower()` string method. Count each lowercase character and return the total.

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Concepts Practiced

* Strings
* Iteration
* String methods (`islower()`)
* Functions
* Counting values

## Notes

A simple kata for practicing string traversal and Python's built-in character checking methods. It reinforces iterating over strings and maintaining a running count.
