#include <iostream>
#include <vector>
#include <string>

using namespace std;


int main(){

    string userinput = "";

    getline(cin,userinput);
    

    vector<int>Array;
    for(int index = 0 ; index < userinput.size();index++){
        Array.push_back(userinput[index]);
    }

    for(int index = 0 ; index < userinput.size();index++){
        cout<<int(Array[index])<<" ";
    }
    cout<<endl;

    return 0;
}