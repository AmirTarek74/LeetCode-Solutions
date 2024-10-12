class Solution:
    def closeStrings(self, password1: str, password2: str) -> bool:
        if len(password1) != len(password2):
            return False

        # Count the frequency of each character in both passwords
        freq1 = Counter(password1)
        freq2 = Counter(password2)

        # If the sets of characters are different, the passwords cannot be close
        if set(freq1.keys()) != set(freq2.keys()):
            return False

        # If the sorted frequencies are equal, the passwords are close
        return sorted(freq1.values()) == sorted(freq2.values())