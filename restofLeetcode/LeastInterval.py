#here we are going to be given a cpu array and the maximum number of space you can have between elements.
#you can easily sort this via math but it's complex

tasks = ["A","A","A","B","B","B"]
n = 2

def solution():
    map = {}
    for task in tasks:
        if task in map:
            map[task] += 1
        else:
            map[task] = 1

    # scenario one: if most freq not enough to force idle states
    scenario1 = len(tasks)

    # FORMULA : (f_max - 1) * (n+1)  + task_count
    # Scenario two: if most freq enough to force idle states
    last = sorted(map.values(), reverse=True)  # sort by most freq to least freq
    f_max = last[0]  # number of occurences of most freq tasks
    task_count = last.count(f_max)  # how many tasks we have with max freq
    scenario2 = (f_max - 1) * (n + 1) + task_count

    return max(scenario1, scenario2)

print(solution())