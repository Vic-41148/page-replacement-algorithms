# Page Replacement Algorithms - OS Lab Assignment 3

## Student Details
- **Name:** Aditya Shibu
- **Roll Number:** 2401201047
- **Course:** BCA (AI & DS)
- **University:** K.R. Mangalam University, School of Engineering & Technology
- **Subject:** Operating System Lab (ENCA252)
- **Submitted To:** Dr. Jyoti Yadav

## Overview
Implementation of 5 key page replacement algorithms used in operating systems for memory management.

### Algorithms Included:
1. **FIFO (First-In, First-Out):** Replaces the oldest page in memory.
2. **LRU (Least Recently Used):** Replaces the page that has not been used for the longest period.
3. **Optimal:** Replaces the page that will not be used for the longest time in the future.
4. **MRU (Most Recently Used):** Replaces the page most recently accessed.
5. **Second Chance (Clock):** An improvement over FIFO that uses a reference bit to give active pages a "second chance".

## Usage
Run the script using Python 3:

```bash
python3 main.py
```

Follow the prompts to enter the page reference string (e.g., `7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1`) and the number of frames.

Alternatively, pass arguments:
```bash
python3 main.py "7 3 0 3 2 1 2 0 7 0 1 2" 3
```

## Sample Output
```text
--- FIFO Page Replacement ---
Step  1: Page 7 -> Frames: [7]             | Status: MISS
Step  2: Page 3 -> Frames: [7, 3]          | Status: MISS
...
========================================
Algorithm            | Page Faults
----------------------------------------
FIFO                 | 10        
LRU                  | 9         
Optimal              | 6         
MRU                  | 10        
Second Chance        | 9         
========================================
```
