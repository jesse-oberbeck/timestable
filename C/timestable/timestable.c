#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int vertical_array[11];
	int horizontal_array[11];
	long int number = 10;
	if(argc > 1){
		number = strtol(argv[1], NULL, 10);
	}
	//printf("%ld\n",number);
	for(int x = 0; x < number; x++){
		vertical_array[x] = x + 1;
		horizontal_array[x] = x + 1;
		//printf("%d   ",x);
	}
	
	int vertical_index = 0;
	int horizontal_index = 0;
	for(int vert = 0; vert < number; vert++){
		vertical_index = vert;
		for(int horiz = 0; horiz < number; horiz++){
			horizontal_index = horiz;
			printf("%d   ", vertical_array[vertical_index] * horizontal_array[horizontal_index]);
		}
	puts("");
	}
}
