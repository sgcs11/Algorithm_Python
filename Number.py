# Catalan number
# 성립조건
# 1. λ in P (λ는 empty string)
# 2. a,b in  P then (a)b in P
# ex. 괄호쌍으로 만들 수 있는 조합의 수 1,1,2,4,14,42, ...
dic = {}
def Calc_Catalan(index):
    if index == 0:
        dic[0] = 1
        return 1
    elif index == 1:
        dic[1] = 1
        return 1
    else:
        result = 0
        for i in range(index):#O(N)
            if i in dic: #O(1)
                a = dic[i]
            else:
                a=Calc_Catalan(i)
            if index-i-1 in dic:#O(1)
                b = dic[index-i-1]
            else:
                b=Calc_Catalan(index-i-1)
            result+=a*b
            dic[i]=a
            dic[index-i-1]=b
        return result
print(Calc_Catalan(29))

# Newton's Method (f(x)=0의 해를 근사적으로 찾는 방법)
# (Xi,f(Xi))에서의 접선 y=f(Xi)+f'(Xi)*(X-Xi)
# 뉴턴 방법식: Xi+1 = Xi - f(Xi)/f'(Xi)

# f(x) = x**2 - a
# a값, n반복횟수
def Newtons_Method(a,n):
    x=1 #아무값이나 설정
    for i in range(n):
        x = (x+a/x)/2
        x = int(x*10**(2**i))/10**(2**i) #정확도는 2배씩 증가하는 quadratic convergence므로 정확한 자릿수만 곱해서 복잡도를 줄임
        print(x)
    return x

print(Newtons_Method(2,8))

# 곱셈 알고리즘
# 파이썬은 큰수에서 카라추바 알고리즘을 사용하여 곱셈 수행
# gmpy 라이브러리에 카라추바, Toom-Cook, Schononhage-Strassen(FFT-고속 푸리에 변환) 알고리즘 포함