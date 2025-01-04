#the purpose of this python code is to test multithreading. This can allow us to run two computentionally advanced programs at the same time; I would say a majority of the time you don't need to do this as keeping default will run just fine.

#first we call the threading library/module in python

import multiprocessing, random, time

#Now we build out the functions we will call first is a number generator, second is a binary search printer.
def ranintgen():
    x=10
    while x>0:
        randint = random.randint(1,100)
        print(randint)
        x-=1
        time.sleep(1)

def bst_printer():
    #creates the array
    arr1 = []
    while len(arr1)<50:
        randint2 = random.randint(1,100)
        if randint2 not in arr1:
            arr1.append(randint2)
        arr1.sort()
    print("the array is: ",arr1)
    time.sleep(1)


    #creaets the target to find
    tt = random.randint(0,len(arr1)-1)
    target = arr1[tt]
    print("target is {a}".format(a=target))

    #binary search time
    l,r = 0,len(arr1)-1
    while l<=r:
        half = int((l+r)/2)
        print("we are guessing the halfway point is {a}".format(a=arr1[half]))

        #logic for moving pointers
        if arr1[half]>target:
            r=half-1
        elif arr1[half]<target:
            l = half+1
        elif arr1[half]==target:
            print('Found the target({a}) at index point {b}'.format(a=target,b=half))
            return



#capture time
intim = time.time()

#test to see hte program works
# ranintgen()
# bst_printer()

#call the init_main. This is good practice and vital on windows for memory management
if __name__ == '__main__':


    #define what process will be used by the multi processing cores
    process1 = multiprocessing.Process(target=ranintgen())
    process2 = multiprocessing.Process(target=bst_printer())

    #Start the multiprocess
    process1.start()
    process2.start()

    #Join the multiprocesses back to main thread
    process1.join()
    process2.join()

#calculate time used
outtim = time.time()


#calc time
trutime = outtim-intim
print("time to run program is {a}".format(a=trutime))


