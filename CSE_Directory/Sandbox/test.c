#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <stdint.h>

// Function to print a number in binary format
void printBinary(unsigned long long num, int bits) {
    if (num == 0) {
        printf("0\n");
        return;
    }

    // Calculate the number of bits needed to represent the number
    int numBits = bits;

    // Loop through each bit and print it
    for (int i = numBits - 1; i >= 0; i--) {
        // Use bitwise AND to check if the bit is set
        int bit = (num >> i) & 1;
        printf("%d", bit);
    }
    printf("\n");
}

int main(int argc, char **argv) {
    uint64_t num = 1<<30;
    uint64_t res = 1<<30;
    float f = 1.0;

    clock_t start = clock();

    for(int i=0; i<100000000; i++) {
        res = (num*res + (uint64_t)(1<<29)) >> 30;
    }

    clock_t end = clock();
    printf("%d\n",end-start);

    return 0;
}
