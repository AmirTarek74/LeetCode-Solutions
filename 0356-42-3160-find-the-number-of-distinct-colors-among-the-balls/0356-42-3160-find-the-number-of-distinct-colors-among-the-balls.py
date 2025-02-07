class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = {}
        
        res = []
        for q in queries:
            ball = q[0]
            color = q[1]
            prev_color = balls[ball] if ball in balls else -1
            if prev_color != color and prev_color == -1:
                colors[color] = colors.get(color, 0) + 1
                balls[ball] = color
            elif prev_color != color and prev_color != -1:
                colors[prev_color] = colors.get(prev_color, 0) -  1
                if colors[prev_color] == 0:
                    del colors[prev_color]
                colors[color] = colors.get(color, 0) + 1
                balls[ball] = color

            res.append(len(colors))
        
        return res
