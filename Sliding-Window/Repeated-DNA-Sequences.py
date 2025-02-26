class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if len(s) < 10:
            return []

        # Mapping DNA characters to 2-bit values
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen = set()      # Stores hashes of sequences seen once
        repeated = set()  # Stores hashes of sequences seen more than once
        hash_value = 0
        BITMASK = (1 << 20) - 1  # Mask to keep last 20 bits (for 10 characters)

        # Compute initial hash for first 10-character sequence
        for i in range(10):
            hash_value = (hash_value << 2) | mapping[s[i]]
        
        seen.add(hash_value)

        # Rolling hash: slide the window across the string
        for i in range(10, len(s)):
            # Shift left by 2 to remove the leftmost character, apply BITMASK to keep 20 bits,
            # then add new character from the right
            hash_value = ((hash_value << 2) & BITMASK) | mapping[s[i]]

            if hash_value in seen:
                repeated.add(s[i-9:i+1])  # Extract the 10-letter sequence
            else:
                seen.add(hash_value)

        return list(repeated)
