#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int vertical_array[100], horizontal_array[100];
    long int upper_bound = 10, lower_bound = 1;
    int width = 4;
    char * side_border = "\u2503";
    char * top_border = "\u2501";
    //Checks for command line args.
    if(argc == 2){
        upper_bound = strtol(argv[1], NULL, 10);
    }else if(argc == 3){
        upper_bound = strtol(argv[2], NULL, 10);
        lower_bound = strtol(argv[1], NULL, 10);
    }
    if(upper_bound > 39){
        width = 5; //Adjustment for longer numbers.
    }
    //Minor input validation.
    if((upper_bound < 0)||(lower_bound < 0)){
        puts("Invalid input. Positive integers only.\nProgram will now close.");
        return(1);
    }else if((upper_bound > 100)||(lower_bound > 100)){
        puts("Integers must be less than 101.");
        return(1);
    }
    //Builds arrays within the default or user supplied limits.
    for(int x = 0; x <= upper_bound; x++){
        vertical_array[x] = x;
        horizontal_array[x] = x;
    }
    //Loop and inner loop multiply one factor by another based on index.
    for(int vert = lower_bound - 1; vert <= upper_bound; vert++){
        if(vert == lower_bound - 1){
            printf(" %*s", width,"   * ");
            int index = vert+1;
            while(index <= upper_bound){ //loop prints factors and top border.
                printf(" %*d", width,horizontal_array[index]);
                index++;
            }
            int number_of_bars = ((upper_bound - lower_bound) * (width + 1) + width + 1);
            puts("");
            printf("%*s%s", width + 1, " ", "\u254B"); //Sets up the corner of the border.
            for(int count = 0; count < number_of_bars; count++){
                printf("%s", top_border);
            }
        }else{
            printf(" %*d%s", width, vertical_array[vert],side_border); //prints side factors.
            for(int horiz = lower_bound; horiz <= upper_bound; horiz++){
                printf(" %*d", width, vertical_array[vert] * horizontal_array[horiz]);
                }        
    }
    puts("");
    }
}
