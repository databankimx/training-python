#include <stdio.h>

int main() {
    unsigned char x, b;

    // Overflow
    x = 64;
    b = x << 3;
    printf("%d << 3 = %d\n", x, b);

    // Underflow
    x = 4;
    b = x >> 3;
    printf("%d >> 3 = %d\n", x, b);

    return 0;
}