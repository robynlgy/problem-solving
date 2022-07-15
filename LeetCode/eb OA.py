#Q1
a = ["I","have","a","nice","surprise"]

def concatEdgeLetters(a):
    res = []

    for i in range(len(a)):
        if i<len(a)-1:
            str = a[i][0]+a[i+1][-1]
        else:
            str = a[i][0]+a[0][-1]
        res.append(str)
    return res
concatEdgeLetters(a)

# Q2

number = "1111122222"
k = 3

def reduceTheNumber(number,k):
    while len(number) > k:
        list = []
        for i in range(0,len(number),k):
            sum = 0
            for j in range(i, min(i+k,len(number))):
                sum += int(number[j])
            list.append(str(sum))
        number = ''.join(list)
    return number

reduceTheNumber(number,k)

# #real bad code
# def reduceTheNumber(number,k):
#     def helper(number):
#         if len(number) <= k:
#             return number
#         #2
#         list = []
#         while len(number)>k:            
#             slice, rem = '', ''             # no reason to save it for later, when you can just get the sum from this using pointers
#             for i in range(k):
#                 slice += number[i]
#             for i in range(k,len(number)):
#                 rem += number[i]
#             number = rem
#             list.append(slice)
#         list.append(number)
#         #3
#         for i in range(len(list)):
#             sum = 0
#             for digit in list[i]:
#                 sum += int(digit)
#             list[i] = str(sum)
#         number = ''.join(list)
#         return helper(number)

#     return helper(number)







