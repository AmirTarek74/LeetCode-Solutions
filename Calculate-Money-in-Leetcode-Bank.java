class Solution {
    public int totalMoney(int n) {
        int res = 0;
        int prevWeek = 1;
        int prevDay = 1;
        int cnt = 0;
        while(n > 0)
        {
            if(cnt == 7) 
            {
                prevWeek++;
                res += prevWeek;
                prevDay = prevWeek+1;
                cnt = 0;
            }else
            {
                res += prevDay;
                prevDay++;
            }
            cnt++;
            n--;
        }
        return res;
    }
}