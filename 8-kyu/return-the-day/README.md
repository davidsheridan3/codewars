# Return the Day

**Difficulty:** 8 kyu

## Problem Summary

Create a function that takes an integer between 1 and 7 and returns the corresponding day of the week. If the input is outside this range, return an error message indicating that the number must be between 1 and 7.

## Examples

```text
Input: 1
Output: "Sunday"

Input: 5
Output: "Thursday"

Input: 9
Output: "Wrong, please enter a number between 1 and 7"
```

## Approach

Store the weekdays in a list (or dictionary) and use the input number to retrieve the correct value. Before accessing the collection, validate that the input is within the accepted range.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Lists (or dictionaries)
* Indexing
* Conditional statements
* Functions
* Input validation

## Notes

A good introductory kata for practicing Python collections, indexing, and basic control flow.
