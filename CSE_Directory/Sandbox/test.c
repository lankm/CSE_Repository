#include <stdio.h>
#include <limits.h>
#include <time.h>
#include <stdint.h>
#include <math.h>

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
    double arr[1<<16];
    double res;

    clock_t start = clock();

    for(int i=0; i<10000000; i++) {
        res = arr[1<<16];
    }

    clock_t end = clock();
    printf("%d\n",end-start);

    return 0;
}
