# 🔍 The "Find the Index of the First Occurrence in a String" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Find the Index of the First Occurrence in a String"** problem — a foundational problem in string search algorithms. Multiple solutions are implemented in C++ with a focus on efficiency, clarity, and practical applications.

---

## 🎯 Problem Statement

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

### Constraints:
- The strings consist of only lowercase English letters.
- `1 <= haystack.length <= 10^4`
- `1 <= needle.length <= 100`

### Example:
- **Input:**  
  `haystack = "sadbutsad", needle = "sad"`  
- **Output:**  
  `0`  
  **Explanation:** `needle` "sad" appears at index 0 in `haystack` "sadbutsad".

- **Input:**  
  `haystack = "leetcode", needle = "leeto"`  
- **Output:**  
  `-1`  
  **Explanation:** `needle` "leeto" does not appear in `haystack` "leetcode".

---

## 🛠️ Approaches & Solutions

### 1. Brute Force Approach (Naive Solution)

This solution checks every possible substring of `haystack` that has the same length as `needle`. This approach is simple but not optimal for large inputs.

**Algorithm:**
- Loop through `haystack` from index `0` to `n - m`, where `n` is the length of `haystack` and `m` is the length of `needle`.
- For each starting index, check if the substring matches `needle`.
- If a match is found, return the index. If no match is found by the end of the loop, return `-1`.

**Time Complexity:** O(n * m)  
**Space Complexity:** O(1)

---

### 2. Using `std::string::find` (Built-in Function)

The simplest and most efficient solution leverages C++'s built-in `find()` function, which returns the index of the first occurrence of `needle` in `haystack`. If `needle` is not found, it returns `string::npos`.

**Algorithm:**
- Use the `find()` function to check if `needle` exists in `haystack`.
- If found, return the index; otherwise, return `-1`.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## 🧪 Edge Cases to Consider

- The `needle` is empty — should return `0` because an empty string is trivially found at the beginning of any string.
- `needle` is longer than `haystack` — should return `-1` immediately as there’s no way for `needle` to fit inside `haystack`.
- The `needle` is at the beginning, middle, or end of `haystack`.
- Strings with repeated characters or when `needle` is a substring that occurs multiple times in `haystack`.

---

## 📚 Additional Resources

- [LeetCode: Implement strStr()](https://leetcode.com/problems/implement-strstr/)
- [C++ Reference: std::string::find](https://en.cppreference.com/w/cpp/string/basic_string/find)
