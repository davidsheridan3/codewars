# The Database

**Difficulty:** 8 kyu

## Problem Summary

Write a function that looks up an IP address in a database and returns the corresponding country or language value. If the input is invalid, missing, or not found, return the appropriate error message.

## Examples

```text id="m9r2aa"
Input: "192.168.0.1"
Output: "Welcome"

Input: "256.1.1.1"
Output: "IP_ADDRESS_INVALID"

Input: "8.8.8.8"
Output: "IP_ADDRESS_NOT_FOUND"

Input: ""
Output: "IP_ADDRESS_REQUIRED"
```

## Approach

Validate the input first. If no IP address is provided, return `IP_ADDRESS_REQUIRED`. If the input is not a valid IPv4 or IPv6 address, return `IP_ADDRESS_INVALID`. Otherwise, check whether the address exists in the database and return the stored value, or `IP_ADDRESS_NOT_FOUND` if it is missing.

## Complexity

* **Time:** O(1)
* **Space:** O(1)

## Concepts Practiced

* Input validation
* Conditionals
* Dictionaries / lookup tables
* String handling
* Functions

## Notes

A good kata for practicing validation logic and controlled return values. The main challenge is handling the different failure cases in the correct order before performing the lookup.
