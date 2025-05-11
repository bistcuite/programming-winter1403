#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Enter a positive integer: ";
    cin >> n;

    int sum = 0;
    for (int i = 0; i < n; i += 2) {
        sum += i;
    }

    cout << "Sum of even numbers less than " << n << " is: " << sum << endl;
    return 0;
}
