n = int(input())
s = set(map(int, input().split()))
nq=int(input())
for _ in range(nq):
    q=list(input().split())
    if('remove' == q[0]):
        s.remove(int(q[1]))
    elif('discard' == q[0]):
        s.discard(int(q[1]))
    elif('pop' == q[0]):
        s.pop()
    else:
        continue
print(sum(s))
