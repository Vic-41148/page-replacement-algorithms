"""
Student Details:
- Name: Aditya Shibu
- Roll Number: 2401201047
- Course: BCA (AI & DS)
- University: K.R. Mangalam University, School of Engineering & Technology
- Subject: Operating System Lab (ENCA252)
- Submitted To: Dr. Jyoti Yadav
"""

import sys

def print_frame_state(step, page, frames, fault):
    status = "MISS" if fault else "HIT"
    frame_str = str(frames) if frames else "[]"
    print(f"Step {step:2}: Page {page} -> Frames: {frame_str:15} | Status: {status}")

def fifo(pages, capacity):
    frames = []
    faults = 0
    print("\n--- FIFO Page Replacement ---")
    for i, page in enumerate(pages):
        fault = False
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            faults += 1
            fault = True
        print_frame_state(i + 1, page, frames, fault)
    return faults

def lru(pages, capacity):
    frames = []
    faults = 0
    print("\n--- LRU Page Replacement ---")
    for i, page in enumerate(pages):
        fault = False
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            faults += 1
            fault = True
        else:
            # Move accessed page to end (most recently used)
            frames.remove(page)
            frames.append(page)
        print_frame_state(i + 1, page, frames, fault)
    return faults

def optimal(pages, capacity):
    frames = []
    faults = 0
    print("\n--- Optimal Page Replacement ---")
    for i, page in enumerate(pages):
        fault = False
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Find page that won't be used for the longest time
                farthest = -1
                replace_idx = -1
                for j in range(len(frames)):
                    try:
                        next_use = pages[i + 1:].index(frames[j])
                    except ValueError:
                        next_use = float('inf')
                    
                    if next_use > farthest:
                        farthest = next_use
                        replace_idx = j
                
                frames[replace_idx] = page
            faults += 1
            fault = True
        print_frame_state(i + 1, page, frames, fault)
    return faults

def mru(pages, capacity):
    frames = []
    faults = 0
    last_used_idx = -1
    print("\n--- MRU Page Replacement ---")
    for i, page in enumerate(pages):
        fault = False
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
                last_used_idx = len(frames) - 1
            else:
                frames[last_used_idx] = page
            faults += 1
            fault = True
        else:
            last_used_idx = frames.index(page)
        print_frame_state(i + 1, page, frames, fault)
    return faults

def second_chance(pages, capacity):
    frames = []
    reference_bits = []
    faults = 0
    pointer = 0
    print("\n--- Second Chance (Clock) Page Replacement ---")
    for i, page in enumerate(pages):
        fault = False
        if page in frames:
            reference_bits[frames.index(page)] = 1
        else:
            if len(frames) < capacity:
                frames.append(page)
                reference_bits.append(0)
            else:
                while reference_bits[pointer] == 1:
                    reference_bits[pointer] = 0
                    pointer = (pointer + 1) % capacity
                
                frames[pointer] = page
                reference_bits[pointer] = 0
                pointer = (pointer + 1) % capacity
            faults += 1
            fault = True
        print_frame_state(i + 1, page, frames, fault)
    return faults

def main():
    try:
        # Check if arguments provided via CLI, else ask
        if len(sys.argv) > 1:
            page_str = sys.argv[1]
            capacity = int(sys.argv[2])
            pages = [int(x) for x in page_str.split()]
        else:
            page_str = input("Enter page reference string (space separated): ")
            pages = [int(x) for x in page_str.split()]
            capacity = int(input("Enter number of frames: "))
    except (ValueError, IndexError):
        print("Usage: python3 main.py \"7 3 0 3 2 1 2 0 7 0 1 2\" 3")
        return

    results = {}
    results["FIFO"] = fifo(pages, capacity)
    results["LRU"] = lru(pages, capacity)
    results["Optimal"] = optimal(pages, capacity)
    results["MRU"] = mru(pages, capacity)
    results["Second Chance"] = second_chance(pages, capacity)

    print("\n" + "="*40)
    print(f"{'Algorithm':<20} | {'Page Faults':<10}")
    print("-" * 40)
    for algo, faults in results.items():
        print(f"{algo:<20} | {faults:<10}")
    print("="*40)

if __name__ == "__main__":
    main()
