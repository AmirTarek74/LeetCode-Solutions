class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        length = {}
        maxi = -1
        maxi_name = ''
        
        for idx,message in enumerate(messages):
            if senders[idx] not in list(length.keys()):
                length[senders[idx]] = 0
            length[senders[idx]] += len(message.split())
            if length[senders[idx]] > maxi:
                maxi = length[senders[idx]]
                maxi_name = senders[idx]
            elif length[senders[idx]] == maxi:
                temp = sorted([senders[idx], maxi_name], key=str, reverse=True)
                maxi_name = temp[0]
        return maxi_name