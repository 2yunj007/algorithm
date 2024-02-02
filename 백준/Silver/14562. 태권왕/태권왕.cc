#include <iostream>
#include <queue>

using namespace std;

struct Item {
	int s, t, cnt;
};

int main()
{
	int tc;
	cin >> tc;

	while (tc--)
	{
		int s, t;
		cin >> s >> t;

		queue<Item> q;
		q.push({ s, t, 0 });

		while (!q.empty())
		{
			Item now = q.front();
			q.pop();

			// 태균이의 점수가 상대 점수보다 더 높아지면 
			// 이후에 두 점수가 같아질 경우는 없음
			if (now.s > now.t) {	
				continue;
			}

			// 두 점수가 같아지는 경우
			if (now.s == now.t) {
				cout << now.cnt << endl;
				break;
			}

			// 1번 발차기
			Item next = { now.s * 2, now.t + 3, now.cnt + 1 };
			q.push(next);
			next = { now.s + 1, now.t, now.cnt + 1 };
			q.push(next);
		}
	}
	return 0;
}