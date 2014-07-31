#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/** @brief Main program entry point.
    @param[in] argc  Number of arguments in @c argv.
    @param[in] argv  Command-line arguments.
    @retval 0
        Success.
*/
bool
inArray(char val, char arr[], int size)
{
    int k;
    for (k = 0; k < size; k++)
    {
        if (arr[k] == val)
            return true;
    }
    return false;
}


int
main(void)
{
    char *string1 = "deadbeef";
    char *string2 = "badfoo";

    char matches[strlen(string1)];

    int i;
    int j;
    int count = 0;
    // O(n^2) implementation
    for (i = 0; i < strlen(string1); i++)
    {
        for (j = 0; j < strlen(string2); j++)
        {
            // compare each letter in "string1" with a single letter of
            // "string2" at a time
            if (inArray(string1[i], matches, count))
            {
                break;
            }

            if (string1[i] == string2[j])
            {
                matches[count] = string1[i];
                count++;
                break;
            }
        }
    }

    printf("Order n-squared implementation: ");
    for (i = 0; i < count; i++)
    {
        printf("%c, ", matches[i]);
    }
    printf("\n");

    return 0;
}
