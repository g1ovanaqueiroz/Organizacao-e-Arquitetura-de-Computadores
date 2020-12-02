#include <stdio.h>
void main() {

  // letra a
  float x = 0.1;
	float y = 0;
  for (int i = 0; i < 99; i++	) {
    y += x;
  }
  printf("%f\n", y);
}