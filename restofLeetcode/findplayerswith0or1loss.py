#did this one on my own!

#Essentially we are given an array of subarrays. We will have to iterate through them and find winner's /losers. A [0,1] means that player 0 won against player 1. We have to build a program to find the list of unstopable winners and players that only lost one game.

#https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

#here is test case

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]

def solution():
    # here we are going to use a hashmap to count the number of times a player has lost a match
    losers = {}
    winners = set()

    # Captures all -1 index losers to hashmap and adds winner to set.
    for match in matches:
        winners.add(match[0])
        if match[-1] not in losers:
            losers.update({match[-1]: 1})
        elif match[-1] in losers:
            losers[match[-1]] += 1

    # now we construct our two arrays, first is for players that have not lost a match; second is for players that lost exactly one match
    runnerup = []
    for player in losers:
        if player in winners:
            # remove player from winners
            winners.remove(player)
        if losers[player] == 1:
            runnerup.append(player)

    # change winner to arr and sort both
    winar = list(winners)
    winar.sort()
    runnerup.sort()
    return winar, runnerup


print(solution())