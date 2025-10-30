class Solution {
    public boolean canMakeEqual(int[] nums, int k) {
        int[] copy = Arrays.copyOf(nums, nums.length);
        int cnt = 0;
        for(int i = 0; i< nums.length -1; i++)
        {
            if(copy[i] != 1)
            {
                copy[i] *= -1;
                copy[i+1] *= -1;
                cnt++;
            }
        }
        if(cnt <= k && copy[nums.length - 1] == 1) return true;
        copy = Arrays.copyOf(nums, nums.length);
        cnt = 0;
        for(int i = 0; i< nums.length -1; i++)
        {
            if(copy[i] != -1)
            {
                copy[i] *= -1;
                copy[i+1] *= -1;
                cnt++;
            }
        }
        return cnt <= k && copy[nums.length - 1] == -1;
    }
}