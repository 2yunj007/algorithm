#include <iostream>
using namespace std;

bool chk[205][205];

int main() {
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		chk[a][b] = chk[b][a] = true;
	}

	int cnt = 0;

	for (int i = 1; i < n - 1; i++) {
		for (int j = i + 1; j < n; j++) {
			if (chk[i][j]) {
				continue;
			}
			for (int k = j + 1; k < n + 1; k++) {
				if (chk[i][k] || chk[j][k]) {
					continue;
				}
				++cnt;
			}
		}
	}

	cout << cnt;

	return 0;
}