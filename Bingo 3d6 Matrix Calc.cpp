// James Taddei
// Bingo 3d6 Matrix Calculator
// 10/4/21

#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
using namespace std;

void rowCreator();
int threeDSixRoll();

int main() {
    srand(time(0));
    cout << "The (3d6) roll matrix is:" << endl;
    for (int i = 0; i < 6; i++) {
        rowCreator();
    }

    return 0;
}

void rowCreator() {
    for (int i = 0; i < 6; i++) {
        cout << setw(4) << threeDSixRoll();
    }
    cout << endl;
}

int threeDSixRoll() {
    int roll1 = rand() % 6 + 1, roll2 = rand() % 6 + 1, roll3 = rand() % 6 + 1;
    
    return roll1 + roll2 + roll3;
}