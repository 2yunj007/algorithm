#include <iostream>

using namespace std;

int main() {
	double a, b;
	double c;

	cin >> a >> b;
	
	cout.precision(10);
	cout << fixed;

	c = a / b;

	cout << c;
}