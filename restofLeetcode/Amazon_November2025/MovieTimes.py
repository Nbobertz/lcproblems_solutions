"""
Question:
You are on a flight and wanna watch two movies during this flight.
You are given List<Integer> movieDurations which includes all the movie durations.
You are also given the duration of the flight which is d in minutes.
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).

Find the pair of movies with the longest total duration and return they indexes. If multiple found, return the pair with the longest movie.
"""

#I found this problem online so I am going to do it

movieDurations = [90, 85, 75, 60, 120, 150, 125]

d = 250

def solution(movieDurations,d):
    #I could sort and then return but that would be o(logn)
    movies = sorted(movieDurations)
    print(movies)

    l,r = 0,len(movieDurations)-1

    target = d-30

    longest_pair = None
    absolute = d

    while l<=r:
        #logic to see
        if movies[l]+movies[r] <= target:
            if longest_pair == None:
                longest_pair = [movies[l],movies[r]]
                absolute = abs(d-(movies[l]-movies[r]))
            elif longest_pair != None:
                if abs(d-(movies[l]-movies[r])) < absolute:
                    #update longest pair
                    longest_pair = [movies[l],movies[r]]

            #since we are below target let's see if we can get closer
            l+=1


        #if we are greater
        if movies[l]+movies[r] > target:
            r-=1

    return longest_pair
print(movieDurations)
print(solution(movieDurations=movieDurations,d=d))


