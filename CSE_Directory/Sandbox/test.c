#include <stdio.h>

int main(int argc, char **argv) {
  char str[] = "Hello world";
  int len = sizeof(str)/sizeof(str[0]);

  for(int i=0;i<len;i++) {
    printf("%c", str[i]);
  }

  return 0;
}