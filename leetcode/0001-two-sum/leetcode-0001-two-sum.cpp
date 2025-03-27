class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> seen;
        
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];
            if (seen.count(diff)) {  
                return {seen[diff], i};
            } else {
                seen[nums[i]] = i;
            }
        }

        // No solution, which is not allowed by the problem definition
        return {0};
    }
};
