#include <iostream>
#include <queue>

using namespace std;

int n, m, sx, sy;
int dir[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};
char mmap[505][505];

struct Node {
  int x, y, step;
};

void bfs(queue<Node> &que) {
  while (!que.empty()) {
    Node temp = que.front();
    que.pop();
    for (int i = 0; i < 4; ++i) {
      int x = temp.x + dir[i][0];
      int y = temp.y + dir[i][1];
      if (mmap[x][y] == '3') {
        cout << temp.step + 1 << endl;
        return;
      }
      if (mmap[x][y] == '.') {
        que.push((Node){x, y, temp.step + 1});
        mmap[x][y] = '@';
      }
    }
  }
  cout << -1 << endl;
}

int main() {
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cin >> mmap[i][j];
      if (mmap[i][j] == '2') {
        sx = i, sy = j;
      }
    }
  }
  queue<Node> que;
  que.push((Node){sx, sy, 0});
  bfs(que);
  return 0;
}
