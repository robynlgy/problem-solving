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