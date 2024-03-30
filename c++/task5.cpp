#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;
using Array = vector<char>;
using Arrays = vector<string>;

pair<int, int> remainder(int base, int Number) {
    int wholeNumber = Number / base;
    int remainder = Number % base;
    return make_pair(remainder, wholeNumber);
}

string tobase(int decimal_num, int base) {
    string result = "";

    while (decimal_num > 0) {
        int remainder = decimal_num % base;
        if (remainder < 10) {
            result = to_string(remainder) + result;
        } else {
            result = static_cast<char>('A' + remainder - 10) + result;
        }
        decimal_num /= base;
    }

    return result;
}

void Encryption(int base, string userinput) {
    for (char c : userinput) {
        cout << tobase(static_cast<int>(c), base) << endl;
    }
}

int index(char character) {
    Array Array{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z'};

    for (int i = 0; i < Array.size(); ++i) {
        if (character == Array[i]) {
            return i;
        }
    }
    return -1;
}

int Encrypt(int base, string Number) {
    int output = 0;
    for (int i = 0; i < Number.length(); ++i) {
        output += index(Number[i]) * pow(base, i);
    }
    return output;
}

string Decrypt(int base, int Number) {
    Array Array{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z'};

    string output = "";
    int number = Number;
    while (number != 0) {
        output += Array[remainder(base, number).first];
        number = remainder(base, number).second;
    }
    reverse(output.begin(), output.end());
    return output;
}

int fromBase(string input_str, int base) {
    int value = 0;
    for (char digit : input_str) {
        value = base * value + stoi(string(1, digit), nullptr, base);
    }
    return value;
}

void Decryption(int base, Arrays userinput) {
    Array DecryptedArray;
    for (string input_str : userinput) {
        if (input_str == "-1") {
            break;
        }
        string decrypted_str = "";

        for (int i = 0; i < input_str.length(); i += 2) {
            decrypted_str += static_cast<char>(fromBase(input_str.substr(i, 2), base));
        }
        DecryptedArray.push_back(decrypted_str);
    }

    string output_str = "";
    for (string i : DecryptedArray) {
        output_str += i;
    }
    cout << output_str << endl;
}

int main() {
    string instruction;
    int baseinput;
    Arrays userinput;

    cin >> instruction;
    cin >> baseinput;

    if (instruction == "encrypt") {
        string input_str;
        while (cin >> input_str && input_str != "-1") {
            Encryption(baseinput, input_str);
        }
    } else {
        string input_str;
        while (cin >> input_str && input_str != "-1") {
            userinput.push_back(input_str);
        }
        Decryption(baseinput, userinput);
    }

    return 0;
}

