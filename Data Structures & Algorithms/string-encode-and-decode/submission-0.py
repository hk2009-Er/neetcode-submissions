class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str=""

        for s in strs:
            encoded_str += str( len(s))
            encoded_str += '#'
            encoded_str += s 
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Find the '#'
            j = i
            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the string
            word = s[j:j + length] 

            result.append(word)

            # Move to the next encoded string
            i = j + length

        return result


