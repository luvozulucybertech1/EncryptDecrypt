#include <iostream>
#include <windows.h>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;
using Array = vector<int>;
using Arrays = vector<string>;

string FindBase(int Base, int Number);

int main(){

    Array Input;
    Arrays Output;

    int BaseInput = -1;
    int UserInput = -1;

    cin >> BaseInput;
    cin >> UserInput;

    while (UserInput != -1){
        Input.push_back(UserInput);
        cin >> UserInput;
    }
    
    for(int index : Input){
        Output.push_back(FindBase(BaseInput, index)); // Changed UserInput to index
    }

    for(string output : Output){
        cout << output << "\n";
    }
    
    return EXIT_SUCCESS;
}


string FindBase(int Base, int Number){

    Array Bases = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z'};

    int Zero = Number;
    int index = -1;
    string Output = "";

    do
    {
        Zero = Zero/Base;
        index = Zero%Base;
        Output += Bases[index];
    } while (Zero != 0);

    return Output;
}