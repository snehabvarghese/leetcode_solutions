#include <stdlib.h>
typedef struct{
    int key;
    int index;
    int used;
}Entry;

int hash(int key,int size){
    return (((key%size)+size)%size);
};
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int size=numsSize*2+1;
    Entry* table =calloc(size,sizeof(Entry));
    for (int i=0;i<numsSize;i++){
        int complement=target-nums[i];

        int pos=hash(complement,size);
        while(table[pos].used){
            if (table[pos].key==complement){
                int* result = malloc(2*sizeof(int));
                result[1]=i;
                result[0]=table[pos].index;
                *returnSize=2;
                free(table);

                return result;

            }
            pos=(pos+1)%size;
        }
        pos=hash(nums[i],size);
        while(table[pos].used){
            pos=(pos+1)%size;


        }
        table[pos].key=nums[i];
        table[pos].index=i;
        table[pos].used=1;

    }
    *returnSize=0;
    return NULL;
};