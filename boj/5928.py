d, h, m = map(int, input().split())

start = 11*24*60+11*60+11
end = d*24*60+h*60+m

print(-1 if end-start<0 else end-start)
