class Solution:
    def isPalindrome(self, x: int) -> bool:
     if x < 0:
       return False
    #  upar wale statement ki jarurt nahi hai QUki neeche wala while loop negative numbers to samabl lega (but still i mentiond it explicitley)
        
     result =0 
     original = x
     while x > 0:
        
        last_digit = x%10
        result = result*10 + last_digit
        x = x//10
     return original == result   