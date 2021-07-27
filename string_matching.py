# Simple algorithm
s="hello"
t="test simple algorithm hello my world"
# t에 s가 있으면 True 아니면 False
# O(s*t)
any(s==t[i:i+len(s)] for i in range(len(t)-len(s)))

# Karp Rabin Using Rolling hash ADT
rs=[]
rt=[]
rs_hash_val=""
rt_hash_val=""
skip_val = 0
new_val = 0

# 공식: h(r) = a*k^0 + b*k^1+...+z*k^(n-1), 적절한 a와 k를 넣어준 후 결과값을 큰 소수(m bucket 크기)로 mod해준다
# 처음 rolling_hash를 만드는 함수
def rolling_hash_first(r):
    result=0
    for i in range(len(r)):
        result*=7
        result+=ord(r[i])
    return result%2147483647
#이후 rolling_hash 함수
#1. 기존 값에 7을 곱해줌, 2. 새로운 값을 더함, 3. 첫번째 값을 뺌
def rolling_hash():
    return rt_hash_val*7+new_val-skip_val*7**(len(s))

def comparison(i):
    if rs_hash_val == rt_hash_val:
        if rs == rt:
            print(f"found index is {i}")
            return True
    return False
    
#찾을 문자열
for c in s: rs.append(c)
rs_hash_val=rolling_hash_first(rs)
#비교할 문자열
for c in t[:len(s)]:rt.append(c)
rt_hash_val=rolling_hash_first(rt)

if not comparison(len(s)-1):
    for i in range(len(s),len(t)):
        skip_val = ord(rt.pop(0))
        rt.append(t[i])
        new_val = ord(t[i])
        rt_hash_val = rolling_hash()
        if comparison(i):
            break


