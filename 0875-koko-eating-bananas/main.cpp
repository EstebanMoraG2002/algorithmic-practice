class Solution {
public:
    bool canEat(vector<int>& piles, int h, int k) {
        long long hours = 0;
        for (int p : piles) {
            hours += (p + k - 1) / k;  // ceil(p/k)
        }
        return hours <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *max_element(piles.begin(), piles.end());

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (canEat(piles, h, mid)) {
                right = mid;           // try smaller speed
            } else {
                left = mid + 1;        // speed too slow
            }
        }
        return left;
    }
};
