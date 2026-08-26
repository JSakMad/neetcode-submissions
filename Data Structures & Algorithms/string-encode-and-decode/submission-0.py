class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for s in strs:
            final += str(len(s)) + "$" + s
        return final

    def decode(self, s: str) -> List[str]:
        final = []
        i = 0 # pointer

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            final.append(s[j+1 : j+1 + length])
            i = j + 1 + length
        return final