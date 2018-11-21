// shell_asm.c
void foo()
{
   __asm__(
        "mov    $0x0,%edx   ;"
        "push   %edx        ;"
        "push   $0x0068732f ;"
        "push   $0x6e69622f ;"
        "mov    %esp,%ebx   ;"
        "push   %edx        ;"
        "push   %ebx        ;"
        "mov    %esp,%ecx   ;"
        "mov    $0xb,%eax   ;"
        "int    $0x80       ;"  //"sysenter   ;"
    );
}

int main(int argc, char * argv[])
{
    foo();    return 0;
}

