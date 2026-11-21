class Solution {
    public boolean hasDuplicate(int[] nums) {
     Set<Integer> numset=new HashSet<>();
     for(int i:nums){
     numset.add(i);   
     }
     int x=nums.length;
     int y=numset.size();
     return x>y;

    }
}