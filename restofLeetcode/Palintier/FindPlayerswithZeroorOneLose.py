#here we are given an array of subarrays. Each subarray represetns a match and the 0th index is the winner and the 1st index is the loser of that match.

#write a program that can go through and pritn out to answer lists. First, a list of players who never lost, second a list of players who lost only one game.

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def solution():
    # so we need to loop thorugh the matches array, use two data structures hashmap and set.
    hm = {}
    winners = set()

    # answer arrays
    nolose = []
    onelose = []

    # loop through and put all winers into set if they have not lost, losers into set with number of losses as key, winnner as value.
    for p1 in range(0, len(matches)):
        winner = matches[p1][0]
        loser = matches[p1][1]
        winners.add(winner)
        if loser not in hm:
            hm[loser] = 1
        elif loser in hm:
            hm[loser] += 1

    for player in hm:
        if player in winners:
            winners.remove(player)
        if hm[player] == 1:
            onelose.append(player)

    nolose = list(winners)

    # sort arrays
    nolose.sort()
    onelose.sort()

    return [[nolose], [onelose]]


print(solution)