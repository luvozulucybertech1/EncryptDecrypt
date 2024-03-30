#include <iostream>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>

using namespace std;
using Arrays = vector<char>;
using Array = vector<string>;

string FindBase(int Base, int Number);

int main(){
	Array output;

	int UserInput;
	int BaseInput;
	
	cin>>BaseInput;
	cin>>UserInput;

	while(UserInput != -1){
		output.push_back(FindBase(BaseInput,UserInput));
		cin>>UserInput;
	}

	for(string i:output){
		cout<<i<<"\n";
	
	}

	return 0;
}


string FindBase(int Base,int Number){

	Arrays Bases = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
         'U', 'V', 'W', 'X', 'Y', 'Z'};


	int Num(Number),modulo;
	string output;
	
	while(Num != 0){
		modulo = Num%Base;
		Num = Num/Base;
		output += Bases[modulo];
	}
	reverse(output.begin(), output.end());
	return output;
}
