#include <iostream>

using namespace std;

void Ad(int n) {
	if (n > 0)
		cout << "do not advertise" << "\n";
	else if (n == 0)
		cout << "does not matter" << "\n";
	else
		cout << "advertise" << "\n";
}

int main() {
	int n;
	cin >> n;

	int* T_c = new int[n];

	int r, e, c;

	for (int i = 0; i < n; i++) {
		cin >> r >> e >> c;
		Ad(r - (e - c));
	}
}