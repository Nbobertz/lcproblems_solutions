#Here we are given three variables. First is a target mile for track, second is an array of cars as their positions, third is an array of speeds where each car moves at a fixed amount. We have to see how many car fleets shw up at one time

class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position,speed), reverse = True)

        stack = []

        for pos,spd in cars:
            time = float(target - pos)/spd

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)