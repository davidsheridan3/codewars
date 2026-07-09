# No Zeros for Heroes

**Difficulty:** 8 kyu

## Problem Summary

Write a function that removes all trailing zeros from an integer. Only zeros at the end of the number should be removed. If the input is `0`, it should remain unchanged.

## Examples

```text id="x8fz3n"
Input: 1450
Output: 145

Input: 960000
Output: 96

Input: -1050
Output: -105

Input: 0
Output: 0
```

## Approach

Check whether the input is `0`. If it is, return `0`. Otherwise, repeatedly remove trailing zeros by dividing the number by `10` while the last digit is `0`. Return the resulting integer once no trailing zeros remain.

## Complexity

* **Time:** O(k), where `k` is the number of trailing zeros.
* **Space:** O(1)

## Concepts Practiced

* Integers
* Modulo operator (`%`)
* Integer division (`//`)
* Loops
* Conditional statements

## Notes

This kata reinforces working with integer arithmetic rather than string manipulation. It is good practice for using the modulo operator to inspect digits and integer division to remove them efficiently.
