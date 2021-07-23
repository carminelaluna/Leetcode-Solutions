class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg =  []
        zero = []
        pos = []
        res = []
        for n in nums:
            if n < 0:
                neg.append(n)
            if n > 0:
                pos.append(n)
            if n == 0:
                zero.append(n)
        
        Positive = set(pos)
        Negative = set(neg)
        if zero:
            for n in Positive:
                if n*-1 in Negative:
                    res.append((-n,0,n))
        if len(zero) >= 3:
            res.append((0,0,0))
        
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                app = -1*(pos[i]+pos[j])
                if app in Negative:
                    res.append(tuple(sorted([pos[i],pos[j],app])))
                   
        for i in range(len(neg)):
            for j in range(i+1,len(neg)):
                app = -1*(neg[i]+neg[j])
                if app in Positive:
                    res.append(tuple(sorted([neg[i],neg[j],app])))
            
        return list(set(res))
