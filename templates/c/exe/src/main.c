#include <stdio.h>

#include "add.h"
#include "multiply.h"

#include "debug/export/file.h"

int main(void)
{
    printf("C Executable Project Template\n");

    printf("add(1,2) = %d\n", add(1, 2));
    printf("multiplier(3,2) = %d\n", multiply(3, 2));

    to_file();
}