"""
The module is used for a variety of time-related tasks, including logging, timing operations, pausing program execution, processing timestamps, and formatting time for display to users.
"""
import time

current_time = time.time()  # epoch time ms since January 1, 1970
print(f"Current time: {current_time}")

print("Start of pausing program executing")
# time.sleep(5) # stop execution of program for seconds noted
print("End of pausing program executing")


current_time = time.time()  # 1749396247.5215323 => epoch time
print(f"Current time: {current_time}")

readable_time = time.ctime(current_time)  # Sun Jun  8 17:24:07 2025
print(f"Readable time: {readable_time}")


current_time = time.time()
print(f"Current time: {current_time}") #1749396307.4148195

local_time = time.localtime(
    current_time
)  # time.struct_time(tm_year=2025, tm_mon=6, tm_mday=8, tm_hour=17, tm_min=25, tm_sec=7, tm_wday=6, tm_yday=159, tm_isdst=1) => named tuple where:
"""
tm_year - year
tm_mon - month from 1 to 12
tm_mday - day of the month from 1 to 31
tm_hour - hour from 0 to 23
tm_min - minutes from 0 to 59
tm_sec - seconds from 0 to 59
tm_wday - day of the week from 0 to 6
tm_yday - day of the year from 1 to 366
tm_isdst - daylight saving time flag. 0 means that daylight saving time is not in effect, -1 - no information, 1 - daylight saving time is in effect
"""

print(f"Local time: {local_time}")


# the time.perf_counter() method, which provides access to a high-precision counter, and is ideal for measuring short time intervals. Used to measure time of program execution


# Record the time at the start of execution
start_time = time.perf_counter()


# Perform some operation
for _ in range(1_000_000):
    pass # Just loop a million times -> this is epmty instruction

# Record the time after the operation is performed
end_time = time.perf_counter()


# Calculate and output the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")



