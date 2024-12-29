class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        word_len = len(words[0])
        target_len = len(target)
        char_freq = [[0]*26 for _ in range(word_len)]

        for word in words:
            for j in range(word_len):
                char_freq[j][ord(word[j])-ord("a")] +=1
        
        prev_count = [0] * (target_len + 1)
        curr_count = [0] * (target_len + 1)

        prev_count[0] = 1

        for curr_word in range(1,word_len + 1):
            curr_count = prev_count.copy()

            for curr_target in range(1, target_len + 1):
                curr_pos = ord(target[curr_target-1]) - ord("a")

                curr_count[curr_target] += (
                    char_freq[curr_word-1][curr_pos] * prev_count[curr_target-1]
                ) % MOD
                curr_count[curr_target] %= MOD
            
            prev_count = curr_count.copy()
        
        return curr_count[-1]
        