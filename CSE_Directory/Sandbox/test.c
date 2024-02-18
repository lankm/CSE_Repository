#include <stdio.h>
#include <limits.h>

typedef struct Pose {
    long pos[4]; // x y z time
    long pos_vel[3]; // x y z

    long rot[4]; // yaw pitch roll time
    long rot_vel[3]; // yaw pitch roll
} Pose;

// Function to print a number in binary format
void printBinary(unsigned long long num) {
    if (num == 0) {
        printf("0\n");
        return;
    }

    // Calculate the number of bits needed to represent the number
    int numBits = sizeof(num) * 8; // Assuming an unsigned int is 32 bits

    // Loop through each bit and print it
    for (int i = numBits - 1; i >= 0; i--) {
        // Use bitwise AND to check if the bit is set
        int bit = (num >> i) & 1;
        printf("%d", bit);
    }
    printf("\n");
}

int main(int argc, char **argv) {
    unsigned long long a = ULONG_MAX;
    unsigned long long b = a >> (sizeof(a)*8/2);
    printBinary(a*a);
    printBinary(b*b);

    return 0;
}
