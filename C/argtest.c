
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	if(argc != 2) {
		// TODO: Should print to error
		printf("Usage: %s <value>\n", argv[0]);
		// TODO: Should return useful error code
		return 1;
	}

	printf("%s\n", argv[1]);

	printf("%ld\n", 5 + strtol(argv[1], NULL, 10));

	char input[5];

	fgets(input, sizeof(input), stdin);

	printf("%s\n", input);
}
