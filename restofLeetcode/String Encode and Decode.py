#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

#We will be given an array of substrings. We will take this array and combine all strings (encode) then break apart the strings again into the proper format.

#constraints
#does the order of the output strings count? Yes. Are there only going to be lowercase letters? Yes. Will there always be a string in the input array? No, sometimes it will be null.

strs = ["neet","code","love","you"]

#I think the best case secenario right here is to create a hashmap and add each string as the key with the index as the value. This will allow us to call it after we combine all strings into an giant string.


#below is the hashmap solution
def encode():
    hmap = {}
    encode = ''
    for p1 in range(0,len(strs)):
        hmap.update({strs[p1]:p1})
        encode+='{a}'.format(a=strs[p1])
    return hmap

def decode():
    decode = []
    sortedhmap = dict(hmap.items(),key=lambda item:item[1])
    for p1 in sortedhmap:
        decode.append(p1)
    decode.pop()
    print(decode)

def encode2():
    encode = ''
    for p1 in strs:
        encode+=p1+'+'
    encode_final = encode[:-1]
    return encode_final

#now we split the return via taking out all of the + signs and then splitting the string via the slot

def decode2(self,strs):
    decode=encode_final.split('+')
    return decode

#did not understand that the string was supposed to be statfulle and nothing else was allowed outside the string. My function returns would not have worked for this problem. As such neetcode's solution was to create an integer and character combo to mark the len of the string that is added. Solution is below.

def encode3(self,strs):
    res = ''
    for s in strs:
        res+=str(len(s))+'#'+s
    return res
def decode3(self,str):
    res,i = [],0
    while i<len(str):
        j=i
        while str[j]!='#':
            j+=1
        length = int(str[i:j])
        res.append(str[j+1:j+1+length])
        i=j+1+length
    return res
str = encode3()
answer = decode3()
print(answer)