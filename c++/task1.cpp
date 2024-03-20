#include <iostream>
#include <string>

using namespace std;


int main(){

    string input = "";

    getline(cin,input);
    

    int Array[50];
    for(int index = 0 ; index < input.size();index++){
        Array[index] = input[index];
    }

    for(int index = 0 ; index < input.size();index++){
        cout<<int(Array[index])<<" ";
    }
    cout<<endl;

    return 0;
}