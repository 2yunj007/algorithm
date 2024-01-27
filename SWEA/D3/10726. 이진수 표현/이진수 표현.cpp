#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; test_case++) {
        int N, M;
        cin >> N >> M;

        int lastNBit = (1 << N) - 1;  // 111...1 (길이 N)
        if (lastNBit == (M & lastNBit)) {   // M의 최하위 N개 비트가 모두 1로 설정되어 있는지 확인
            cout << "#" << test_case << " " << "ON" << endl;
        } else {
            cout << "#" << test_case << " " << "OFF" << endl;
        }
    }

    return 0;
}