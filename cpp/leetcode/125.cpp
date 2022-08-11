#include <vector>
#include <iostream>

using namespace std;

bool checkPalindrome(string str) {
    //preprocessing the string
    string modifiedStr = "";
    for (char ch : str) {
        if (isalnum(ch) == true) {
            char modifiedChar = tolower(ch);
            modifiedStr.push_back(modifiedChar);
        }
    }

    for (int i = 0; i < modifiedStr.size() / 2; i++) {
        if (modifiedStr[i] != modifiedStr[modifiedStr.size() - 1 - i]) {
            return false;
        }
    }

    return true;

}

int main() {

    string input = "a man A plAn a cAnaL : panama!";
    string input2 = "race a car";

    cout << checkPalindrome(input) << endl;;
    cout << checkPalindrome(input2) << endl;;

    

    return 0;
}