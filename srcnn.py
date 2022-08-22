from collections import defaultdict
def count(N, s):
 
    mp = defaultdict(lambda: 0)
    ans = 0
 
    for i in range(N):
        a = [0] * 26
        for j in range(len(s[i])):
            a[ord(s[i][j]) - ord('a')] += 1
        for j in range(26):
            a[j] = a[j] % 2
        ans += mp[tuple(a)]
        for j in range(26):
            newCount = a[:]
            if (a[j] == 0):
                newCount[j] = 1
            else:
                newCount[j] = 0
            ans += mp[tuple(newCount)]
 
        mp[tuple(a)] += 1
    return ans
    

     
N = 4
A = [ "abc", "abcd" , "bc" , "adc"]

print(count(N, A))