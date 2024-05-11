#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class NQueens {
private:
    int gsize;
    vector<int> gpos;

public:
    NQueens(int size) : gsize(size), gpos(size, -1) {}

    bool isSafe(int row, int col) {
        for (int i = 0; i < row; ++i) {
            if (gpos[i] == col || abs(gpos[i] - col) == abs(i - row))
                return false;
        }
        return true;
    }

    bool btrack(int row) {
        if (row == gsize) {
            display();
            return true;
        }
        for (int col = 0; col < gsize; ++col) {
            if (isSafe(row, col)) {
                gpos[row] = col;
                if (btrack(row + 1))
                    return true;
                gpos[row] = -1;
            }
        }
        return false;
    }

    void display() {
        cout << "Solution:" << endl;
        for (int i = 0; i < gsize; ++i) {
            for (int j = 0; j < gsize; ++j) {
                if (gpos[i] == j)
                    cout << "Q ";
                else
                    cout << ". ";
            }
            cout << endl;
        }
        cout << endl;
    }

    void branchbound(int row) {
        if (row == gsize) {
            display();
            return;
        }
        for (int col = 0; col < gsize; ++col) {
            if (isSafe(row, col)) {
                gpos[row] = col;
                branchbound(row + 1);
            }
        }
    }
};

int main() {

    int size;
    // Prompt the user to enter the size of the chessboard (grid size)
    cout << "Enter the size of the chessboard (grid size): ";
    // Read the input size
    cin >> size;
    // Check if the input size is within the range [1, 8]
    while (size < 1 || size > 8) {
        cout << "Invalid input! Please enter a size between 1 and 8: ";
        cin >> size;
    }
    // Create instances of NQueens with the valid input size
    NQueens q1(size);
    NQueens q2(size);

    // Proceed with the rest of the code
    cout << "\nBacktracking Solution:\n";
    if (!q1.btrack(0)) {
        cout << "No solution exists.\n";
    }
    cout << "\nBranch and Bound Solution:\n";
    q2.branchbound(0);
    return 0;
}
