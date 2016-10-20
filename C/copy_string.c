#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void copy_string(char dst[], char src[], size_t sz)
{
	
	for(size_t n = 0; n < strlen(src); ++n){
		dst[n] = src[n];
	}
}
