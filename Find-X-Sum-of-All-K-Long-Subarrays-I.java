class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] res = new int[n - k + 1];

        for(int i =0; i<= n- k; i++)
        {
            Map<Integer, Integer> count = new HashMap<>();
            for(int j = i; j< i + k ; j++)
            {
                count.put(nums[j], count.getOrDefault(nums[j], 0) + 1);
            }
            List<int[]> freq = new ArrayList<>();
            for(Map.Entry<Integer, Integer> e: count.entrySet())
            {
                freq.add(new int[] {e.getValue(), e.getKey()});
            }
            freq.sort((a, b) -> b[0]!= a[0] ? b[0]-a[0]:b[1]-a[1]);
            int sum = 0;
            for(int w = 0; w< x && w<freq.size(); w++)
            {
                sum += freq.get(w)[0] * freq.get(w)[1];
            }
            res[i] = sum;
        }
        return res;
    }
}