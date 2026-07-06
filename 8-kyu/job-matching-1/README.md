# Job Matching #1

**Difficulty:** 8 kyu

## Problem Summary

Write a function that determines whether a job is a suitable match for a candidate based on salary expectations.

A candidate specifies a minimum acceptable salary, while a job specifies a maximum available salary. A match is considered valid if the job's maximum salary meets at least **90%** of the candidate's minimum salary. If either salary value is missing, the function should raise an error.

## Examples

```text id="0l29xg"
Input:
candidate = {"min_salary": 120000}
job = {"max_salary": 140000}

Output:
True

Input:
candidate = {"min_salary": 120000}
job = {"max_salary": 100000}

Output:
False
```

## Approach

First, verify that both the candidate and job dictionaries contain the required salary fields. Then, calculate 90% of the candidate's minimum salary to account for the allowed flexibility. Finally, compare this value with the job's maximum salary and return the result of the comparison.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Dictionaries
* Dictionary key access
* Input validation
* Conditional statements
* Arithmetic operations
* Boolean expressions

## Notes

This kata introduces working with dictionaries and validating input before processing it. It also demonstrates that comparison expressions in Python evaluate directly to boolean values, allowing them to be returned without an explicit `if` statement.
