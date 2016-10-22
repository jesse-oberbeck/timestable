#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    //Sets up arrays and default values.
    int vertical_array[100], horizontal_array[100];
    long int upper_bound = 10, lower_bound = 1;
    int width = 4;

    //Checks for command line args.
    if(argc == 2){
        upper_bound = strtol(argv[1], NULL, 10);
    }else if(argc == 3){
        upper_bound = strtol(argv[2], NULL, 10);
        lower_bound = strtol(argv[1], NULL, 10);
    }

    //Adjustment for longer or shorter numbers.
    if(upper_bound > 32){
        width = 5;
    }

    //Corrects for numbers in the wrong order, or a lone zero.
    if((lower_bound > upper_bound) && (argc > 2)){
        int temp_int = lower_bound;
        lower_bound = upper_bound;
        upper_bound = temp_int;
    }else if(upper_bound == 0){
         lower_bound = 0;
    }

    //Minor input validation.
    if((upper_bound < 0) || (lower_bound < 0)){
        puts("Invalid input. Positive integers only.\nProgram will now close.");
        return(1);
    }else if((upper_bound > 100) || (lower_bound > 100)){
        puts("Integers must be less than 101, but greater than zero.");
        return(1);
    }

    //Builds arrays within the default or user supplied limits.
    for(int i = 0; i <= upper_bound; i++){
        vertical_array[i] = i;
        horizontal_array[i] = i;
    }

    //Loop and inner loop multiply one factor by another based on index.
    for(int vert = lower_bound - 1; vert <= upper_bound; vert++){
        if(vert == lower_bound - 1){
            printf(" %*s", width,"     ");
            int index = vert+1;

            //Loop prints top factors.
            while(index <= upper_bound){
                printf("%*d", width + 1,horizontal_array[index]);
                index++;
            }

            //Generates quantity of bars for top border.
            int number_of_bars = ((upper_bound - lower_bound) * (width + 1) + width + 1);
            puts("");

            //Sets up the corner of the border.
            printf("%*s%s", width + 1, " ", "\u250F");

            //Prints top border.
            for(int count = 0; count < number_of_bars; count++){
                printf("%s", "\u2501");
            }
        }else{
            //prints side factors and border.
            printf(" %*d%s", width, vertical_array[vert], "\u2503");

            //Maths happen here.
            for(int horiz = lower_bound; horiz <= upper_bound; horiz++){
                printf(" %*d", width, vertical_array[vert] * horizontal_array[horiz]);
            }        
        }
    puts("");
    }
}
