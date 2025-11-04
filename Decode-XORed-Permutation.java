class Solution {
    public int[] decode(int[] encoded) {
        int n = encoded.length + 1;
        int[] res = new int[n];
        int x = 0;
        for(int i =1 ; i<=n; i++)
        {
            x = x^i;
        }
        for(int i = 1; i< n; i= i+ 2)
        {
            x = x ^ encoded[i];
        }
        res[0] = x;
        for(int i =1; i<n;i++)
        {
            res[i] = res[i-1] ^ encoded[i-1];
        }
        return res;
    }
}