#include <iostream>
#include <cmath>
using namespace std;

double f(double x) {
    return exp(-x) * cos(x) * sin(x);
}

double integral(double a, double b, int n) {
    double h = (b - a) / n;
    double sum = (f(a) + f(b)) / 2.0;
    
    for (int i = 1; i < n; ++i) {
        sum += f(a + i * h);
    }

    return sum * h;
}

int main() {
    double a = 0, b = M_PI;
    int n = 1000;

    double result = integral(a, b, n);
    cout << "Approximate integral: " << result << endl;

    return 0;
}
