class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> frequency;
        for (int num:nums){
            ++frequency[num];
        }

        vector<vector<int>> buckets(nums.size()+1);
        for(const auto& [num, count] : frequency){
            buckets[count].push_back(num);
        }

        vector<int> result;
        result.reserve(k);

        for(int count=static_cast<int>(buckets.size())-1; count>=0 && static_cast<int>(result.size())<k; --count){
            for(int num:buckets[count]){
                result.push_back(num);
                if (static_cast<int>(result.size())==k){
                    break;
                }
            }
        }
        return result;
    }
};
