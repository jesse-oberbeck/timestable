#include <stdio.h>

int iterator(void);

int main(int argc, char *argv[])
{
	int value = iterator();

	printf("%d\n", value);

	value = iterator();
	printf("%d\n", value);

	value = iterator();
	printf("%d\n", value);
}

int iterator(void)
{
	static int x = 0;
	x += 1;

	return x;
}
