#here we are seeing if a car can complete a circute around a track.

total_gain = 0
curr_gain = 0
answer = 0

for i in range(len(gas)):
    # gain[i] = gas[i] - cost[i]
    total_gain += gas[i] - cost[i]
    curr_gain += gas[i] - cost[i]

    # If we meet a "valley", start over from the next station
    # with 0 initial gas.
    if curr_gain < 0:
        curr_gain = 0
        answer = i + 1

return answer if total_gain >= 0 else -1