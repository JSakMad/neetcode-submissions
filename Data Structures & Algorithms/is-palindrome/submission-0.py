class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make two pointers, one at the end and one at the start and look through characters until they are the same

        start = 0
        end = len(s) - 1

        while start < end:
            # Three cases where we move the pointers
            # First case is just moving the start where it is not a alnum
            # Second case is just moving the end where it is not an alnum
            # Third case is moving both when they are equal to eachother
            # The third case should be engaged when the first two fail since only move both when the characters are actually equal
            if s[start].isalnum() == False:
                start += 1
            elif s[end].isalnum() == False:
                end -= 1
            elif s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            else:
                return False

        return True
