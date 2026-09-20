# DSA & NeetCode Patterns Glossary

Core terminology and mental models for NeetCode Blind 75 practice.

## Arrays & Hashing

**Hash Set**:
A data structure offering average O(1) membership testing and insertion by hashing keys into bucket slots.
_Avoid_: List searching, linear scan for uniqueness

**Hash Map / Dictionary**:
A key-value mapping offering average O(1) retrieval, used to trade O(n) auxiliary space for O(1) lookup time.
_Avoid_: Nested loop pair lookup

**Complement Lookup**:
The technique of calculating the required matching value (`target - current`) and querying the Hash Map in O(1) rather than scanning the remaining elements in O(n).
_Avoid_: Brute-force pairwise sum

**Frequency Counting**:
Aggregating element occurrences using a fixed-size array (e.g. 26 integers for lowercase ASCII) or hash map.
_Avoid_: Repeated substring or array counting

**Bucket Sort (by frequency)**:
Grouping elements into array indices matching their occurrence count, achieving O(n) time for Top-K queries without a heap.
_Avoid_: Full O(n log n) sorting when frequency bound is known

**Prefix and Suffix Accumulation**:
Precomputing running products or sums from both boundaries of an array to answer range queries in O(1) without division.
_Avoid_: Nested product loops, floating point division

**Guarded Decrement Pattern**:
The technique of combining an O(1) length pre-check (`len(s) == len(t)`) with decrementing frequency counts during the second pass. Mismatch or zero count immediately aborts, guaranteeing that successfully completing the pass results in an exact zero balance without requiring an extra dictionary scan.
_Avoid_: Second-pass dictionary scan or two separate frequency maps when lengths are already verified equal.
