#include <iostream>
#include <vector>

using namespace std;
using Array = vector<int>;

int main(){

    int UserInput = -1;
    Array Store;

    cin>>UserInput;
    while(UserInput != -1){
        Store.push_back(UserInput);
        cin>>UserInput;
    }

    for(int m : Store){
        cout<<char(m);
    }
    cout<<endl;

    return 0;
}