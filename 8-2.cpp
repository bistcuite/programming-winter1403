#include <iostream>
using namespace std;

double f(double x, double x0, double lambda) {
    double denom = x0 - x;
    return lambda / (denom * denom);
}

double trapezoidal(double a, double b, int n, double x0, double lambda) {
    double h = (b - a) / n;
    double sum = (f(a, x0, lambda) + f(b, x0, lambda)) / 2.0;

    for (int i = 1; i < n; ++i) {
        sum += f(a + i * h, x0, lambda);
    }
    return sum * h;
}

int main() {
    double L, x0, lambda;
    int n;

    cout << "Enter length L of charged line: ";
    cin >> L;
    cout << "Enter point x0 > L to calculate E: ";
    cin >> x0;
    cout << "Enter linear charge density lambda: ";
    cin >> lambda;
    cout << "Enter number of intervals n for integration: ";
    cin >> n;

    double E = trapezoidal(0, L, n, x0, lambda);

    cout << "Electric field E at x0 = " << x0 << " is approximately: " << E << endl;

    return 0;
}
