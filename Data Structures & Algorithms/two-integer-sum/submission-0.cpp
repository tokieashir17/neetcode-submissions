class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> numMap;
        int n = nums.size();
        for(int i = 0; i < n; i++) {
            int match = target - nums[i];

             if(numMap.find(match) != numMap.end()) {
                return {numMap[match], i};
            }
            numMap[nums[i]] = i;

        }
        return {};
    }
};
