int ** pt2; /*ponteiro para ponteiro do tipo inteiro*/
int * pt1; /*ponteiro para o tipo inteiro*/
int x = 10;

pt2 = &pt1;
pt1 = &x;

*pt1 = 30;
**pt2 = 50;