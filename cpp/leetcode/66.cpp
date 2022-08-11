#include <vector>
#include <iostream>
#include <map>

using namespace std;
vector<int> plusOne(vector<int> &digits) {
    vector<int> output;
    int prevDigitVal = 1;

    for (int i = digits.size() - 1; i >= 0; i--) {
        if (digits[i] + prevDigitVal == 10) {
            output.insert(output.begin(), 0);
            prevDigitVal = 1;
        } else {
            output.insert(output.begin(), digits[i] + prevDigitVal);
            prevDigitVal = 0;
        }
    }

    if (prevDigitVal > 0) output.insert(output.begin(), 1);

    return output;

}

int main() {
    vector<int> input = {1, 2, 3, 5, 7, 9};

    vector<int> output = plusOne(input);

    for (auto itr : output) {
        cout << itr << endl;
    }

    

    return 0;
}