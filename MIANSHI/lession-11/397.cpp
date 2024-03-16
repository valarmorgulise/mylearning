#include <iostream>

using namespace std;

int n, m, t = 0;
int dir[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};
int mmap[105][105];

void dfs(int x, int y) {
  for (int i = 0; i < 4; ++i) {
    int xx = x + dir[i][0];
    int yy = y + dir[i][1];
    if (mmap[xx][yy] != 0) {
      mmap[xx][yy] = 0;
      dfs(xx, yy);
    }
  }
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      cin >> mmap[i][j];
    }
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      if (mmap[i][j] != 0) {
        t++;
        mmap[i][j] = 0;
        dfs(i, j);
      }
    }
  }
  cout << t << endl;
  return 0;
}
