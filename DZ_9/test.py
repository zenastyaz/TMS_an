def func():
    s = "loveleetcode"
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    print(-1)


func()
