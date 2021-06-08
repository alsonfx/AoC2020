test = False
if test:
    schedule = open('time_schedule_test.txt', 'r')
    earliest = 0
else:
    schedule = open('time_schedule.txt', 'r')
    earliest = 100000000000000

time = int(schedule.readline())
line2 = schedule.readline().strip()
departures = [(time, int(bus_id)) for (time, bus_id) in enumerate([bus for bus in line2.split(',')]) if bus_id != 'x']
busses = [int(bus) for bus in line2.split(',') if bus != 'x']
schedule.close()

arrivals = []
wait_times = []
for bus in busses:
    arrival_time = bus * (time // bus) + bus
    arrivals.append(arrival_time)
    wait_times.append(arrival_time - time)

shortest = wait_times.index(min(wait_times))
print(f"The earliest time is: {arrivals[shortest]}")
print(f"Wait time of: {wait_times[shortest]}")
print(f"Solution: {busses[shortest] * wait_times[shortest]}")


# while True:
#     valid = True
#     for time, bus_id in departures:
#         valid &= (earliest + time) % bus_id == 0
#         if not valid:
#             break
#
#     if valid:
#         print(f"The earliest timestamp is: {earliest}")
#         break
#     else:
#         earliest += departures[0][1]

def chinese_remainder_theorem(pairs):
    set_n = 1
    for _, number in pairs:
        set_n *= number
    total = 0
    for step, number in pairs:
        remainder = number - step
        subset_n = set_n // number
        inverse = pow(subset_n, number-2, number)
        total += remainder * subset_n * inverse
        total %= set_n
    return total


print(chinese_remainder_theorem(departures))
