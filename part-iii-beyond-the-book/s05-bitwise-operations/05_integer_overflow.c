#include <stdio.h>

int main() {
    // Overflow unsigned byte
    unsigned char ub = 255;
    ub++;
    printf("\nub = %i\n", ub);

    // Overflow signed byte
    char sb = 127;
    sb++;
    printf("\nsb = %i\n\n", sb);

    return 0;
}
