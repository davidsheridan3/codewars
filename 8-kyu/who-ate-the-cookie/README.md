# Who Ate the Last Cookie?

**Difficulty:** 8 kyu

## Problem Summary

Write a function that determines who ate the last cookie based on the type of the input value. Return a formatted message naming the correct person.

* If the input is a string, return **Zach**.
* If the input is an integer or a float, return **Monica**.
* For any other type, return **the dog**.

## Examples

```text
Input: "hello"
Output: "Who ate the last cookie? It was Zach!"

Input: 42
Output: "Who ate the last cookie? It was Monica!"

Input: [1, 2, 3]
Output: "Who ate the last cookie? It was the dog!"
```

## Approach

Check the type of the input using Python's `isinstance()` function. Based on the detected type, assign the appropriate name and return the required formatted string.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Type checking
* `isinstance()`
* Conditional statements
* String formatting
* Functions

## Notes

A beginner-friendly kata for practicing type checking in Python. It reinforces using `isinstance()` to handle different input types and constructing formatted output strings.
