
#include <iostream>
#include <vector>

using namespace std;

int solution() {

    long long min, max;
    cin >> min >> max;

    // numbers[0] is min
    // numbers[max - min] is max
    vector<bool> numbersSquared(max - min + 1, false);

    int count = 0;

    for (long long i = 2; i * i <= max; i++) {
        long long n = min / (i * i);

        if (min % (i * i) != 0)
            n += 1;

        while (n * i * i <= max) {
            numbersSquared[n * i * i - min] = true;
            n += 1;
        }
    }

    for (auto item : numbersSquared) {
        if (item == false) count += 1;
    }

    return count;
}

int main() {

    cout << solution() << endl;

    return 0;
}