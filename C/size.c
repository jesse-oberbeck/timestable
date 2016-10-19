#include <stdio.h>

int main(void)
{
	puts("type\tsize");

	printf("char\t%zd\n", sizeof(char));
	printf("short\t%zd\n", sizeof(short));
	printf("int\t%zd\n", sizeof(int));
	printf("long\t%zd\n", sizeof(long));
	printf("long long\t%zd\n", sizeof(long long));

	printf("size_t\t%zd\n", sizeof(size_t));
	printf("void *\t%zd\n", sizeof(void *));
	printf("func *\t%zd\n", sizeof(void(*)()));
}
