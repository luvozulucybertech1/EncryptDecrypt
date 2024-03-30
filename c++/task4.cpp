#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;
using Arrays = vector<int>;

int BaseTen(int Base, string Number);

int main() {
    int UserInput;
    int BaseInput;
    Arrays Output;

    cin >> BaseInput;
    cin >> UserInput;
    
    while(UserInput != -1)
      Output.push_back(BaseTen(BaseInput, to_string(UserInput)));
      cin >> UserInput;
    }
    
    for(int i : Output){
        cout<<i<<"\n";
    }
    
    return 0;
}

int BaseTen(int Base, string Number) {
    int Num = 0;

    for (int index = Number.length() - 1; index > -1; index--) {
        int digit = Number[index] - '0';
        Num +=  digit * pow(Base, Number.length() - index - 1);
    }
    return Num;
}

