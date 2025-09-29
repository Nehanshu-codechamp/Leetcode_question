class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        num = abs(x)
        answer = 0

        while num > 0:
            last_digit = num % 10
            answer = (answer * 10) + last_digit
            num //= 10

        if is_negative:
            answer = -answer

        # handle 32-bit signed integer overflow
        if answer < -2**31 or answer > 2**31 - 1:
            return 0

        return answer
