class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int[] res = new int[2];
        int idx = 0;
        Set<Integer> seen = new HashSet<>();
        for(int n: nums)
        {
            if(seen.contains(n)) res[idx++] = n;
            seen.add(n);
        }
        return res;
    }
}