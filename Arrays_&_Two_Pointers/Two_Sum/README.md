# ⚔️ The "Two Sum" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Two Sum"** coding problem, providing a detailed breakdown of various algorithmic approaches to solve it. Each solution is implemented in C++ and is organized for clarity and learning.

---

## 🎯 Problem Statement

Given an array of integers `nums` and an integer `target`, the goal is to find the indices of the two numbers in the array that add up to the target.

### Constraints:
- Each input will have exactly one solution.
- You may not use the same element twice.
- The order of the returned indices does not matter.

### Example:
- Input: nums = [2, 7, 11, 15], target = 9
- Output: [0, 1]

---
  
## 🛠️ Approaches & Solutions

### 1. Brute Force Approach
Checks every possible pair.

**Algorithm:**
- Loop through each element `nums[i]`.
- Loop through the remaining elements `nums[j]` where `j > i`.
- If `nums[i] + nums[j] == target`, return `[i, j]`.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

🔗 Code: [`With_Brute_Force.cpp`](./With_Brute_Force.cpp)

---

### 2. Hashing (Unordered Map) Approach
Uses a hash map to find complements in one pass.

**Algorithm:**
- Use a hash map to store `(value, index)` pairs.
- For each number, calculate its complement (`target - num`).
- If the complement exists in the map, return both indices.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

🔗 Code: [`With_Hashing.cpp`](./With_Hashing.cpp)

---

### 3. Two-Pointer Approach
Requires sorting while preserving original indices.

**Algorithm:**
- Store `(value, index)` pairs in a vector.
- Sort the vector by value.
- Use two pointers (`left` and `right`) to find the sum.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

🔗 Code: [`With_Two_Pointer.cpp`](./With_Two_Pointer.cpp)


---

## 📖 Additional Resources

- [LeetCode: Two Sum](https://leetcode.com/problems/two-sum/)
- [GeeksforGeeks: Find a Pair with Given Sum](https://www.geeksforgeeks.org/find-a-pair-with-the-given-sum-in-an-array/)
