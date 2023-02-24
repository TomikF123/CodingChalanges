class Solution(object):
    n = 33
    def climbStairs(self, n):
        smallSteps = n//1
        bigSteps = n//2
        output = 0
        if n in range(0,4):
            return n
        if n%2==0:
            output = 2
            c=2
            for i in range((n // 2) + 1, (n+1)):
                print(output)
                output += abs((i - c) * c)
                i = i-c

                c += 2
            print(output)

        else:
            output =1
            c=1
            for i in range((n // 2)+1,(n)):
                output += abs((i - c) *c)*(i-c)
                print(output)

                c += 2
        return output

    print(climbStairs(None,n))
