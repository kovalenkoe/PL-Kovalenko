s=input()
n=len(s)
fh=s[:n//2]
fh=fh.replace('п','*')
sh=s[n//2:]
r=fh + sh
print(r)
