// Brute Force Code & Optimal Code
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        // start first segment element can be swapped only when they have the same number of set bits therefore consecutive element with the same number of set bits from one segment  store the number of sets bits in the current segment 
        int numOfSetBits = __builtin_popcount(nums[0]);
        // store the largest value in the current segment since element inside the same segment can be rearranged need to know the maximum value that this segment can produce 
        int maxOfSegment = nums[0];
        // store the smallest value in the current segement need to this to check whether this segment can come after the previous segement 
        int minOfSegment = nums[0];
        // store the maximum value of the previous segement intially there is no previous segement so use negative infinity 
        int maxOfPrevSegment = INT_MIN;
        // process the remaining element 
        for (int i = 1; i < nums.size(); i++) {
            // check whehter nums[i] has the same number of set bits are as the current segments 
            if (__builtin_popcount(nums[i]) == numOfSetBits) {
                // nums[i] belongs to the current segment update the maximum values of the segment  
                maxOfSegment = max(maxOfSegment, nums[i]);
                // nums[i] belongs to the current segment update the minimum values of the segment  
                minOfSegment = min(minOfSegment, nums[i]); 
            } else {
                // nums[i] has a different number of set bits so it starts a new segment before moving to the new segment check whether the current segment can come after the previous segment in sorted order for the final array to be sorted : minimum value of current segment must be >= maximum value of previous segment if : minofsegment < maxofprevsegment then some value in the current segment would need to move before a larger value from the previous segment impossible because elements from different bit-count segments cannot be swapped   
                if (minOfSegment < maxOfPrevSegment) { 
                    return false;
                }
                // current segment is valid so save its maximum value that the next segment can be checked against it 
                maxOfPrevSegment = maxOfSegment;
                // start the new segment current element is the first element of the new segment 
                maxOfSegment = nums[i];
                minOfSegment = nums[i];
                numOfSetBits = __builtin_popcount(nums[i]);
            }
        }
        // check the final segment so loop checks a segment only when encounter a new segment threfore the final segment still needs to be compared with the previous segment it means minimum values must be >= maximum value of the previous segment 
        if (minOfSegment < maxOfPrevSegment) {
            return false;
        }
        // every segment can be arranged so that the complete array becomes sorted 
        return true;
    }
};

// Time Complexity : O(N)
// Space Complexity : O(N)