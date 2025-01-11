
class Solution {
public:
    // CHECK FUNCTION
    bool check(vector<int>& day, int m, int k, int mid) {
        int bouquetCount = 0, flowerCount = 0;
        for (int i = 0; i < day.size(); i++) {
            if (day[i] <= mid) {
                flowerCount++;
                if (flowerCount == k) {  // found k continuous flowers
                    bouquetCount++;
                    flowerCount = 0;    // reset it to 0,(bouquet complete)
                }
            } else {    
                flowerCount = 0;    
            }
            if (bouquetCount >= m) {
                return true;
            }
        }
        return false;
    }
    // MAIN FUNCTION
    int minDays(vector<int>& day, int m, int k) {

        if (((long)m * k) > day.size())
            return -1;
        int low = *min_element(day.begin(), day.end());
        int high = *max_element(day.begin(), day.end());
        // BINARY SEARCH
        while (low < high) {    
            int mid = (long(low + high)) / 2;
            if (check(day, m, k, mid)) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        return low;
    }
};