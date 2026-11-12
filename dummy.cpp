#include <cstdio>
#include <cstring>
// Dummy: answers nothing useful; used only to see the judge's report format.
int main() {
    char s[1 << 16];
    int T;
    if (scanf("%d", &T) != 1) return 0;
    int t, ne, nq;
    while (scanf("%s", s) == 1) {
        if (strcmp(s, "TICK")) continue;
        scanf("%d %d %d", &t, &ne, &nq);
        // skip: we cannot know how many lines; read until next TICK lazily
        printf("ANS");
        for (int i = 0; i < nq; i++) printf(" 0");
        printf("\nEND\n");
        fflush(stdout);
        if (t == T) break;
    }
}
