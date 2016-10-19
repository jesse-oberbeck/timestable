#include <stdio.h>
#include <math.h>

int main(void)
{
	int number = 20;
	while(number <= 60){
		if(number % 2 == 0){
			int square = pow(number,2);
			double root = sqrt(number);
			printf("%d\t%d\t%lf", number, square, root);
		}
		number++;
		puts("");
	}

}
