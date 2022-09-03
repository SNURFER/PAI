#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int binarySearch(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;

    while (left <= right) {
        int mid = right + (left - right) / 2;
        if (nums[mid] < target) {
            left = mid + 1;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else {
            return mid;
        }
    }

    return -1;
}

bool hasNum(vector<int>& nums, int target) {
    int idx = binarySearch(nums, target);
    if (idx != -1) return true;
    return false;
}

void solution() {
    cin.tie(NULL);
    cout.tie(NULL);
    std::ios::sync_with_stdio(false);
    int n, m;
    cin >> n;

    vector<int> nums;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        nums.push_back(num);
    }
    sort(nums.begin(), nums.end());

    int input;
    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> input;
        if (hasNum(nums, input) == true) {
            cout << 1 << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
}


int main() {
    solution();
    return 0;
}