"""def data(atuple):
    nums = ()
    words = ()
    for t in atuple:
        nums = nums + (t[0],)
        if t[1] in words:
            words = words + (t[1],)
        minm = min(nums)
        maxm = max(nums)
        leng = len(words)
    return (minm, maxm, leng)"""
import re
sub = re.sub("[^a-z]+","","AKH KB.242HKkjdk")
print(sub)

