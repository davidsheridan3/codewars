# Triple Trouble

**Difficulty:** 8 kyu

## Problem Summary

Write a function that takes three strings of equal length and combines them by alternating their characters. For each position, append the corresponding character from the first, second, and third strings to build the final result.

## Examples

```text
Input: one = "aa", two = "bb", three = "cc"
Output: "abcabc"

Input: one = "ab", two = "12", three = "XY"
Output: "a1Xb2Y"

Input: one = "Hello", two = "12345", three = "ABCDE"
Output: "H1Ae2Bl3Cl4Do5E"
```

## Approach

Iterate through the indices of the strings and, for each position, concatenate the corresponding characters from all three strings. Append the combined characters to the result string and return it after processing every index.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

## Concepts Practiced

* Strings
* Indexing
* Loops
* String concatenation
* Functions

## Notes

This kata is good practice for working with multiple strings simultaneously. It reinforces string indexing, iterating over a sequence, and building a new string by combining characters from several inputs.
