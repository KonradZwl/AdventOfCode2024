import time
from day3.part1.sol import process_input
from day3.part2.sol import process_input2

with open('input.txt', 'r', encoding='utf-8-sig') as file:
    lines = file.readlines()

# First part
start_time = time.perf_counter()
process_input(lines)
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.3f} ms")

#Second part
start_time = time.perf_counter()
process_input2(lines)
end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000
print(f"Execution time: {execution_time_ms:.3f} ms")