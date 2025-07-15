import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> getConcatenation(int[] nums) {
        List<Integer> ans = new ArrayList<>();

        
        for (int i = 0; i < nums.length; i++) {
            ans.add(nums[i]);
        }

        
        for (int i = 0; i < nums.length; i++) {
            ans.add(nums[i]);
        }

        return ans;
    }
}
