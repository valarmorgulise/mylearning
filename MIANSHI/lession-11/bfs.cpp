#include <iostream>
#include <queue>

using namespace std;

struct Node {
  int x, y, step;
};

int n, m, sx, sy;
int dir[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};
char mmap[105][105];

void print() {
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      cout << mmap[i][j];
    }
    cout << endl;
  }
}

int main() {
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= m; ++j) {
      cin >> mmap[i][j];
      if (mmap[i][j] == 'S') {
        sx = i, sy = j;
      }
    }
  }
  queue<Node> que;
  que.push((Node){sx, sy, 0});
  while (!que.empty()) {
    Node temp = que.front();
    que.pop();
    for (int i = 0; i < 4; ++i) {
      int x = temp.x + dir[i][0];
      int y = temp.y + dir[i][1];
      if (mmap[x][y] == 'T') {
        cout << temp.step + 1 << endl;
        print();
        return 0;
      }
      if (mmap[x][y] == '.') {
        que.push((Node){x, y, temp.step + 1});
        mmap[x][y] = '@';
      }
    }
  }
  cout << "NO" << endl;
  print();
  return 0;
}
