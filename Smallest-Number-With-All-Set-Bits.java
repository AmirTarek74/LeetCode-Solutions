class Solution {
    public int smallestNumber(int n) {
        int cnt = 0;
        while(n!=0)
        {
            n/=2;
            cnt++;
        }
        return ((int)Math.pow(2, cnt)-1);
    }
}