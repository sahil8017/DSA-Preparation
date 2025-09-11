# 🔀 The "Valid Palindrome" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Valid Palindrome"** problem — a challenge in string manipulation and validation. Multiple solutions are implemented in Python with a focus on efficiency, clarity, and readability.

---

## 🎯 Problem Statement

Given a string `s`, determine if it is a **valid palindrome**, considering only alphanumeric characters and ignoring case sensitivity.

A **palindrome** is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

**Return `true` if `s` is a palindrome, and `false` otherwise.**

### Constraints:
- The string `s` can be of any length from 0 to \(10^5\).
- The string contains only printable ASCII characters.

### Example:
- **Input:**  
  `s = "A man, a plan, a canal: Panama"`  
- **Output:**  
  `true`

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach – Optimal Solution

This solution uses two pointers to compare characters from the beginning and end of the string, moving towards the center.

**Algorithm:**
- Initialize two pointers, `left` at the beginning (`0`) and `right` at the end (`len(s) - 1`).
- While `left < right`:  
  - If `s[left]` is not alphanumeric, increment `left`.  
  - If `s[right]` is not alphanumeric, decrement `right`.  
  - If `s[left]` and `s[right]` (in lowercase) are not equal, return `false`.  
  - Otherwise, increment `left` and decrement `right`.
- If no mismatches are found, return `true`.

**Time Complexity:** O(n), where `n` is the length of the string.  
**Space Complexity:** O(1), as only a few variables are used.

🔗 Code: [`TwoPointer_Optimal.py`](./TwoPointer_Optimal.cpp)

---

### 2. Brute Force with String Filtering (Educational Only)

A simpler approach that involves filtering and then comparing the string.

**Algorithm:**
- Filter out non-alphanumeric characters and convert the string to lowercase.
- Compare the filtered string with its reverse.

**Time Complexity:** O(n), where `n` is the length of the string.  
**Space Complexity:** O(n) due to the creation of the filtered string.

🔗 Code: [`BruteForce_Filter.py`](./BruteForce_Filter.cpp)

---

## 🧪 Edge Cases to Consider

- An empty string: `""` should return `true`.
- A string with only non-alphanumeric characters (e.g., `"!"`) should return `true` since it's technically a palindrome.
- Case sensitivity: The solution should ignore letter casing (`"A"` and `"a"` should be treated as the same).
- Strings with spaces and punctuation (e.g., `" "`, `"race car"`) should be considered palindromes after filtering out non-alphanumeric characters.

---

## 📚 Additional Resources

- [LeetCode: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [GeeksforGeeks: Check if a string is palindrome](https://www.geeksforgeeks.org/check-if-a-string-is-palindrome-or-not/)
- [Palindrome Explanation (Stack Overflow)](https://stackoverflow.com/questions/35242023/check-if-a-string-is-palindrome-in-python)
