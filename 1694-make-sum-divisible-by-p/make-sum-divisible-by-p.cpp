// Brute Force Code & Optimal Code
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        // number of element in the array
        int n = nums.size();
        // calculate the total sum of the array modulo p
        int sum = 0;
        // calculate total sum % p
        for(int &num : nums) {
            sum = (sum + num) % p;
        }
        // remove a subarray whose sum % p is equal to the remainder of the total sum
        int target = sum % p;
        // if the total sum is alredy divisible by p no subarray needs to tbe removed
        if(target == 0) {
            return 0;
        }
        // dictionary to store : prefix_sum_remainder -> latest index
        unordered_map<int, int> mp; 
        // store the current prefix sum modulo p
        int current = 0;
        // before the array starts the prefix sum is 0 , index = -1 represents the position before the first element this help us handle subarray that start from index 0
        mp[0] = -1;
        // store the minimum length of valid subarray found so far intially use n because n is the maximum possible subarray length
        int result = n;
        // traverse the arary from left to right
        for(int j = 0; j < n; j++) {
            // update the prefix sum modulo p, current represents : (nums[0] + nums[1] + ..........+ nums[j]) % p
            current = (current + nums[j]) % p;
            // suppose : previous prefix remainder = previous and current prefix remainder = current so the sum of subarray between previous index and j is (current - previous) % p threfore : (current - previous) % p = target
            int remain = (current - target + p) % p;
            // check the whether have already seen this required prefix remainder
            if(mp.find(remain) != mp.end()) {
                // if remainder was previously found at index: mp[remainder] than the subarray from mp[remainder] + 1 to j has sum % p == target its length is j - mp[remainder] keep the shortest valid subarray
                result = min(result, j - mp[remain]);
            }
            // store the current prefix remainder with the current index store the lastest index so that when the same remainder appears again the shoretest possible subarray
            mp[current] = j;
        }
        // if result is still n never found a valid subarray in that case return -1 otherwise return the minimum length found
        return result == n ? -1 : result;
    }
};


// Time Complexity : O(N)
// Space Complexity : O(N)