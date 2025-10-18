class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # n = len(numbers)
        # # for i in range(0,n):
        #     for j in range(i+1,n):
        #         if numbers[i] + numbers[j] == target:
                    
        #              return[i+1,j+1]

    #    optimal approch two pointer
         
        n = len(numbers)
        start , end = 0,n-1
        while start<=end :
            if numbers[start] + numbers[end]== target:
                return[start+1,end+1]
            elif numbers[start] + numbers[end] < target:
                 start+=1
            else:
                end-=1
        return[-1,-1]
            