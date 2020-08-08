#include <iostream>
#include<sstream>
#include<time.h> //added for the random number generator seed
#include<cstdlib> //added to use the rand function

using namespace std;
int main()
{
    //declare all the values
    int target, int_test;
    int guess = -1;
    string decision;
    string userString;
    srand(time(NULL)); //set the seed for the random number generator
redo_game:
    target = rand() %100 + 1; //generate the 'random' number
    do{
re_input:
    cout<<"Guess a number between 0 and 100(If you want to quit this game, please input 'q') : ";
    getline(cin, userString);
    //If there is "q" to quit a game
    if(userString == "q"){
	cout << "You want to quit this game."<< endl;
	cout << "The number was " << target << ".\n";
	break;
    }
    //convert string to an int
    if((stringstream(userString) >> guess)){
	cout << guess << "\n";
    }
    else{
	    cout << "You input unrecognized something. Try again!"<<endl;
	    goto re_input;
    }

    if(guess > target){
        cout << "The guess is high!" << endl;
    }
    else if(guess < target){
        cout << "The guess is low!" << endl;
    }
    else {
        cout << "You entered the correct guess." << endl;
	redecision:
	cout << "Do you want to continue this game? (y/n)" << endl;
	getline(cin, decision);
	if(decision == "y") {
	cout << "Okay. Restart this game!" << endl;
		    guess = -1;
		    goto redo_game; //keep going to this game!
	}
	else if(decision == "n") {
		cout<< "Thank you!" << endl;
		goto escape_thisloop;
		}
	else{
		cout<< "Please input your decision correctly!" << endl;
		goto redecision;
	}
	
    }
    }while(true);
escape_thisloop:
    cout <<"Program ended!" << endl;        
    return 0;
}
