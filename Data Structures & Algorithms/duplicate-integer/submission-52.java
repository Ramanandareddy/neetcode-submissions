class Solution {
    public boolean hasDuplicate(int[] nums) {
     Set<Integer> numset=new HashSet<>();
     for(int i:nums){
        if(numset.contains(i)){
            return true;
        }
        numset.add(i);
     }
     return false;

    }
}