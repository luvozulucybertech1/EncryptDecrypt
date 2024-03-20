#include <iostream>
#include <vector>

using namespace std;
using Array = vector<int>;

int main(){

    int userinput = -1;
    Array Store;

    cin>>userinput;
    while(userinput != -1){
        Store.push_back(userinput);
        cin>>userinput;
    }

    for(int m : Store){
        cout<<char(m);
    }
    cout<<endl;

    return 0;
}