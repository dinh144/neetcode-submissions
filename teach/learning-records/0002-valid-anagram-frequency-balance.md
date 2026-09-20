# Valid Anagram: Guarded Frequency Decrement Pattern

Captured the foundational invariant of Valid Anagram: combining the O(1) length guard (`len(s) == len(t)`) with a single-pass frequency count or dictionary allows early termination on mismatch (`c not in dic or dic[c] == 0`) and guarantees zero leftover frequency without an extra O(k) cleanup scan. Differentiates ASCII fixed array (26 slots, zero hash overhead) from general Unicode hash map.
