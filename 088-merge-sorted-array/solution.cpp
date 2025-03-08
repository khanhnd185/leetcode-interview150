#include <vector>

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int r = m + n - 1;
        m--;
        n--;

        while (r > -1) {
            if (n < 0) {
                for (int i = m; i>-1;) nums1[r--] = nums1[i--];
                break;
            }
            if (m < 0) {
                for (int i = n; i>-1;) nums1[r--] = nums2[i--];
                break;
            }
            if (nums1[m] > nums2[n])   nums1[r--] = nums1[m--];
            else                       nums1[r--] = nums2[n--];
        }
    }
};