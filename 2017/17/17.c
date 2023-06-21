#include<stdio.h>

// PART 1

// void add_number(int number, int pos, int curr_size, int array[]){
//     int i;
//     for(i = curr_size-1; i > pos; i = i - 1){
//         array[i + 1] = array[i];
//     }
//     array[pos + 1] = number;

// }

// int main(void)
// {
//     int steps = 337;
//     // int steps = 3;
//     const int max_num = 2017;
//     // const int max_num = 9;

//     int curr_size = 1;
//     int state[max_num];

//     // initialize all values of array to 0
//     int i;
//     for(i = 0; i < sizeof(state)/sizeof(state[0]); i = i + 1) {
//         state[i] = 0;
//     }


//     int number = 1;
//     int pos = 0;

//     for(i = 0; i < max_num; i++){
//         pos = (pos + steps) % curr_size;
//         add_number(number, pos, curr_size, state);
//         pos += 1;
//         number += 1;
//         curr_size += 1;

//         // print all values of array

//         // int k;
//         // for(k = 0; k < curr_size; k = k + 1) {
//         //     printf("%d  ", state[k]);
//         // }
//         // printf("\n");
//     }
//     // 483
//     printf("%d\n", state[1]);
//     return 0;
// }

// PART 2
int main(void)
{
    int steps = 337;
    // int steps = 3;
    const int max_num = 50000000;
    // const int max_num = 9;

    int curr_size = 1;
    int i;


    int number = 1;
    int pos = 0;

    int first_number = 0;

    for(i = 0; i < max_num; i++){
        pos = (pos + steps) % curr_size;
        if(pos == 0){
            first_number = number;
        }
        pos += 1;
        number += 1;
        curr_size += 1;

        // print all values of array

        // int k;
        // for(k = 0; k < curr_size; k = k + 1) {
        //     printf("%d  ", state[k]);
        // }
        // printf("\n");
    }
    // 483
    printf("%d\n", first_number);
    return 0;
}
