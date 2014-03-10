__author__ = 'yiqingj'

def test(b, c=[]):
    c.append(b)
    print c

def printPar(l, r, str, count):
    if l < 0 or r < l:
        return
    if l == 0 and r == 0:
        print "".join(str)
    else:
        if l > 0:
            str[count] = '('
            printPar(l-1, r, str, count+1)
        if r > l:
            str[count] = ')'
            printPar(l, r-1, str, count+1)

def check_unique(str):
    mark = {}
    s = list(str)
    for i, c in enumerate(s):
        if mark.has_key(c):
            return False
        mark[c] = True
    return True

def remove_dup(str):
    s = list(str)
    l = len(str)  # length of string
    tail = 1
    for i in range(1, l):
        has_dup = False
        for j in range(0,i):
            if s[i] == s[j]:
                has_dup = True
                break
        if not has_dup:
            s[tail] = s[i]
            tail += 1
    return "".join(s[:tail])

def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def reverse(str):
    str2 = ''
    for i in range(len(str)-1, -1, -1):
        str2 += str[i]
    print str2

def reverse2(str):
    if len(str) <= 1:
        return str
    return reverse2(str[1:])+str[0]



if __name__ == "__main__":
    c=[]
    dic = {}
    test('a',c)
    count = 4
    str = [None]*count*2
    printPar(count,count, str, 0)
    for i,s in enumerate('hello'):
        print i,s
    print check_unique('abcde')
    print remove_dup('abababa')
    print anagram('abcdef', 'defcba')
    reverse('abcde')
    print reverse2('abcde')

