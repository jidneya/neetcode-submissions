class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            keyArray = [0] * 26
            for char in word:
                ascii = ord(char)
                keyArray[ascii - 97] += 1
            dictionary[tuple(keyArray)] = dictionary.get(tuple(keyArray), []) + [word]

        result = []
        for value in dictionary.values():
            result.append(value)
        return result
            


            