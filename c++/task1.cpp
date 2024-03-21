#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(){

    string UserInput = "";

    getline(cin,UserInput);
    

    vector<int>Array;
    for(int index = 0 ; index < UserInput.size();index++){
        Array.push_back(UserInput[index]);
    }

    for(int index = 0 ; index < UserInput.size();index++){
        cout<<int(Array[index])<<" ";
    }
    cout<<endl;

    return 0;
}