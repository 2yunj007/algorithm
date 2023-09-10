#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int n;
  int x, y;
  int max_x = -10001, max_y = -10000, min_x = 10001, min_y = 10001;
  
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> x >> y;
    min_x = min(x, min_x);
    max_x = max(x, max_x);
    min_y = min(y, min_y);
    max_y = max(y, max_y);
  }
  cout << (max_x - min_x) * (max_y - min_y);
  return 0;
}