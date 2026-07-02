# Calculate BMI

**Difficulty:** 8 kyu

## Problem Summary

Write a function that calculates a person's Body Mass Index (BMI) using their weight and height, then returns the corresponding weight category based on the calculated BMI.

## Examples

```text
Input: weight = 80, height = 1.80
Output: "Normal"

Input: weight = 95, height = 1.75
Output: "Obese"

Input: weight = 50, height = 1.75
Output: "Underweight"
```

## Approach

Calculate the BMI using the formula `weight / (height ** 2)`. Then, use conditional statements to compare the calculated BMI against the defined thresholds and return the appropriate category.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Arithmetic operations
* Exponents (`**`)
* Conditional statements
* Functions
* Floating-point numbers

## Notes

A good introductory kata for practicing mathematical calculations, conditional logic, and working with floating-point values in Python.
