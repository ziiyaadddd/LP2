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
    cout << "Enter the size of the chessboard (grid size): ";
    cin >> size;
    NQueens q1(size);
    NQueens q2(size);
    cout << "\nBranch and Bound Solution:\n";
    if (!q1.btrack(0)){
        cout << "No solution exists.\n";
    }
    cout << "\nBackTracking Solution:\n";
    q2.branchbound(0);
    return 0;
}
