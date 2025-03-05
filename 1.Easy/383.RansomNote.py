class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}

        # Count characters in ransomNote
        for ch in ransomNote:
            if ch in hmap:
                hmap[ch] += 1
            else:
                hmap[ch] = 1
        
        # Process magazine and reduce counts
        for ch in magazine:
            if ch in hmap:
                hmap[ch] -= 1
                if hmap[ch] == 0:  # Remove when count becomes zero
                    del hmap[ch]
            
            # If hmap is empty, we found all letters needed
            if not hmap:
                return True

        return not hmap  # If hmap still has missing letters, return False
