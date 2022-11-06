#primePy 모듈 사용해보기
from primePy import primes

numto1000 = len(primes.upto(1000)) + 1
numto100 = len(primes.upto(100)) + 1

result = numto1000 - numto100

print("10~100까지의 소수의 개수는 ", result, "이다.")
