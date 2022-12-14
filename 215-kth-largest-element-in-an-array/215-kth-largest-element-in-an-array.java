class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        int l = nums.length;
        if(l == 1) return nums[0];
        for(int i : nums){
            q.add(i);
        }
        if(l == k) return q.poll();
        for(int i = 0; i<l-k; i++) q.poll();
        return q.poll();
    }}