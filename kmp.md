# Knuth-Morris-Pratt (KMP) Algorithm 

## Overview
KMP is a string-matching algorithm that improves on the naive approach by avoiding redundant character comparisons. It uses information from the pattern itself to skip sections of the text.

## How it Works
1.  **LPS Array (Longest Proper Prefix which is also a Suffix):**
    *   Precompute an array `lps[]` where `lps[i]` is the length of the longest proper prefix of `pattern[0...i]` that is also a suffix of `pattern[0...i]`.
2.  **Searching:**
    *   Maintain two pointers: `i` for text and `j` for pattern.
    *   If characters match, move both pointers.
    *   If a mismatch occurs after `j` matches:
        *   Instead of resetting `i` to the start, we use `lps[j-1]` to set the new `j`.
        *   This allows us to keep the `i` pointer moving forward (or staying put), never backtracking in the text.

## Complexity
*   **Preprocessing:** $O(m)$.
*   **Matching:** $O(n)$.
*   **Total:** $O(n + m)$.

## Why KMP?
Unlike the naive $O(n \cdot m)$ algorithm, KMP guarantees linear time matching even in the worst case (e.g., matching "AAAAA" in "AAAAAAAAAB").
