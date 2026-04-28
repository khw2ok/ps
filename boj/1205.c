#include <stdio.h>

int main() {
  int n, new, p, rank = 1, i;
  int score[52];

  scanf("%d %d %d", &n, &new, &p);

  if (n == 0) {
    printf("1");
    return 0;
  }

  for (i=0; i<n; i++) {
    scanf("%d", score+i);
    if (new < *(score+i)) rank += 1;
  }

  if ((n == p && *(score+n-1) == new) || (rank > p)) printf("-1");
  else printf("%d", rank);

  return 0;
}
