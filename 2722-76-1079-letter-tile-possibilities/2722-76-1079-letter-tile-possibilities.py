class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seq = set()
        used = [False] * len(tiles)
        self.generate_seq(tiles, "", used, seq)

        return len(seq) - 1
    
    def generate_seq(self, tiles, s, used, seq):

        seq.add(s)
        for pos, c in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self.generate_seq(tiles, s+c, used, seq)
                used[pos] = False