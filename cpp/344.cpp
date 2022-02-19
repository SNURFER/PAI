#include <vector>
#include <iostream>

using namespace std;

void reverseString(string& input) {

    int n = input.size();
    for (int i = 0; i < n / 2; i++) {
        char temp;
        temp = input[i];
        input[i] = input[n - 1 - i];
        input[n - 1 - i] = temp;
    }
}

int main() {

    string input = "testttt";

    reverseString(input);
    cout << input << endl;


    return 0;
}
