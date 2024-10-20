class Solution:

    def encode(self, strs: List[str]) -> str:
        terminator = '\0'
        lengths = ""
        res = ""
        for word in strs:
            n = len(word)
            res = res + word
            if n >= 0 and n <= 9:
                lengths += ("00"+str(n))
            elif n >= 10 and n <= 99:
                lengths += ("0"+str(n))
            else:
                lengths += (str(n))

        return res + terminator + lengths

    def decode(self, res: str) -> List[str]:
        null = '\0'
        loc = 0
        for i in range(0,len(res)):
            if res[i] is null:
                loc = i
                break

        merged = res[:loc]
        lengths = res[loc+1:]

        k = 3
        lengths = [int(lengths[i:i+k]) for i in range(0, len(lengths), k)]

        res = []
        start = 0
        for length in lengths:
            res.append(merged[start:start+length])
            start += length

        return res
