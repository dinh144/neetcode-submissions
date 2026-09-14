# Hàng đợi ôn

Luật giai đoạn + lệnh `due` / `review <slug>`: xem `CLAUDE.md`. Giải lại từ trắng, không nhìn submission cũ.

| # | Bài (slug) | Pattern | Dấu hiệu | Hint? | Giai đoạn | Hạn ôn |
|---|---|---|---|---|---|---|
| 03 | two-integer-sum | Hash map | cặp có tổng = target → lưu phần bù đã thấy | ? | ôn | 2026-09-15 |
| 09 | is-palindrome | Two pointers | so hai đầu, bỏ ký tự không alnum | ? | ôn | 2026-09-15 |
| 12 | buy-and-sell-crypto | Sliding window | mua trước bán sau → giữ đáy bên trái | ? | ôn | 2026-09-15 |
| 04 | anagram-groups | Hash map | nhóm cùng ký tự → key = đếm 26 hoặc chuỗi sort | ? | ôn | 2026-09-16 |
| 10 | three-integer-sum | Sort + two pointers | bộ ba tổng 0 không trùng → sort, cố định i, bỏ trùng | ? | ôn | 2026-09-16 |
| 49 | climbing-stairs | 1-D DP | số cách tới bậc n = f(n-1) + f(n-2) | ? | ôn | 2026-09-16 |
| 05 | top-k-elements-in-list | Bucket sort / heap | k phần tử tần suất cao nhất → bucket theo tần suất O(n) | ? | ôn | 2026-09-17 |
| 11 | max-water-container | Two pointers | diện tích chặn bởi cột thấp → dời con trỏ thấp | ? | ôn | 2026-09-17 |
| 13 | longest-substring-without-duplicates | Sliding window + set | chuỗi con không lặp → co trái khi trùng | ? | ôn | 2026-09-17 |
| 06 | string-encode-and-decode | Length prefix | ghép list chuỗi an toàn → `len#chuỗi` | ? | ôn | 2026-09-18 |
| 07 | products-of-array-discluding-self | Prefix / suffix | tích trừ chính nó, cấm chia → prefix × suffix | ? | ôn | 2026-09-18 |
| 01 | duplicate-integer | Hash set | có phần tử lặp → set | ? | ôn | 2026-09-18 |
| 08 | longest-consecutive-sequence | Hash set | dãy liên tiếp O(n) → chỉ đếm từ số không có n-1 | ? | ôn | 2026-09-19 |
| 02 | is-anagram | Đếm tần suất | cùng ký tự cùng số lần → đếm 26 | ? | ôn | 2026-09-19 |

## Thứ tự Blind 75

Arrays & Hashing: 01 Contains Duplicate · 02 Valid Anagram · 03 Two Sum · 04 Group Anagrams · 05 Top K Frequent Elements · 06 Encode and Decode Strings · 07 Product of Array Except Self · 08 Longest Consecutive Sequence
Two Pointers: 09 Valid Palindrome · 10 3Sum · 11 Container With Most Water
Sliding Window: 12 Best Time to Buy And Sell Stock · 13 Longest Substring Without Repeating Characters · 14 Longest Repeating Character Replacement · 15 Minimum Window Substring
Stack: 16 Valid Parentheses
Binary Search: 17 Find Minimum In Rotated Sorted Array · 18 Search In Rotated Sorted Array
Linked List: 19 Reverse Linked List · 20 Merge Two Sorted Lists · 21 Linked List Cycle · 22 Reorder List · 23 Remove Nth Node From End of List · 24 Merge K Sorted Lists
Trees: 25 Invert Binary Tree · 26 Maximum Depth of Binary Tree · 27 Same Tree · 28 Subtree of Another Tree · 29 Lowest Common Ancestor of a BST · 30 Binary Tree Level Order Traversal · 31 Validate BST · 32 Kth Smallest Element In a BST · 33 Construct Binary Tree From Preorder And Inorder · 34 Binary Tree Maximum Path Sum · 35 Serialize And Deserialize Binary Tree
Heap: 36 Find Median From Data Stream
Backtracking: 37 Combination Sum · 38 Word Search
Tries: 39 Implement Trie · 40 Design Add And Search Words · 41 Word Search II
Graphs: 42 Number of Islands · 43 Clone Graph · 44 Pacific Atlantic Water Flow · 45 Course Schedule · 46 Graph Valid Tree · 47 Number of Connected Components · 48 Alien Dictionary
1-D DP: 49 Climbing Stairs · 50 House Robber · 51 House Robber II · 52 Longest Palindromic Substring · 53 Palindromic Substrings · 54 Decode Ways · 55 Coin Change · 56 Maximum Product Subarray · 57 Word Break · 58 Longest Increasing Subsequence
2-D DP: 59 Unique Paths · 60 Longest Common Subsequence
Greedy: 61 Maximum Subarray · 62 Jump Game
Intervals: 63 Insert Interval · 64 Merge Intervals · 65 Non Overlapping Intervals · 66 Meeting Rooms · 67 Meeting Rooms II
Math & Geometry: 68 Rotate Image · 69 Spiral Matrix · 70 Set Matrix Zeroes
Bit Manipulation: 71 Number of 1 Bits · 72 Counting Bits · 73 Reverse Bits · 74 Missing Number · 75 Sum of Two Integers
