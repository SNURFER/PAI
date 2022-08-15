#include <iostream>
#include <vector>
#include <algorithm>

void solution() {
    int n, temp;
    std::vector<int> divisor;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> temp;
        divisor.push_back(temp);
    }

    sort(divisor.begin(), divisor.end());

    if (n % 2 == 1) std::cout << divisor[(int)(n / 2)] * divisor[(int)(n / 2)] << std::endl;

    else std::cout << divisor.front() * divisor.back() << std::endl;
}


int main() {
    solution();
    return 0;
}