class Solution(object):
    def singleNumber(self, nums):
        f={}
        l=[]
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i in f:
            if f[i]==1:
                l.append(i)
        return l
        