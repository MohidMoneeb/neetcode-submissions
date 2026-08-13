class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Word1 = []
        Word2 = []

        for char in s:
            Word1.append(char)

        for char in t:
            Word2.append(char)

        Word1.sort()
        Word2.sort()

        if Word1 == Word2:
            return True
        return False
