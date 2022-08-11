#include <vector>
#include <iostream>

using namespace std;

vector<string> splitBySpace(string input) {
    string delimiter = " ";
    vector<string> splitVec;

    size_t pos = 0;
    while ((pos = input.find(delimiter)) != string::npos) {
        splitVec.push_back(input.substr(0, pos));
        input.erase(0, pos + delimiter.length());
    }

    return splitVec;
}

vector<string> reorderLogFiles(vector<string> &logs) {
    vector<string> letters;
    vector<string> digits;

    for (auto log : logs) {
        if (isdigit(splitBySpace(log)[1][0])) digits.push_back(log);
        else letters.push_back(log);
    }

    sort(letters.begin(),
         letters.end(),
         [](string leftLog, string rightLog) {
             string delimiter = " ";
             size_t pos = leftLog.find(delimiter);
             string leftStrIdentifier = leftLog.substr(0, pos);
             string leftStrWOIdentifier = leftLog.substr(pos + 1, string::npos);
             pos = rightLog.find(delimiter);
             string rightStrIdentifier = rightLog.substr(0, pos);
             string rightStrWOIdentifier = rightLog.substr(pos + 1, string::npos);

             return (leftStrWOIdentifier == rightStrWOIdentifier ? leftStrIdentifier < rightStrIdentifier : leftStrWOIdentifier < rightStrWOIdentifier);
         });

    vector<string> output;
    for (auto str : letters) {
        output.push_back(str);
    }

    for (auto str : digits) {
        output.push_back(str);
    }

    return output;
}

int main() {

    // vector<string> logs = {"dig1 8 1 5 1","let1 art zero","dig2 3 6","let2 own kit dig","let3 art zero"};
    vector<string> logs = {"2 A","1 B","4 C","1 A"};

    vector<string> output = reorderLogFiles(logs);
    for (auto str : output) {
        cout << str << endl;
    }

    return 0;
}