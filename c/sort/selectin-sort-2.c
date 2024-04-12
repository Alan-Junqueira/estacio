void selectionSort (int *v)
{
    int i,j,aux, min, pos_min;
    for (i=0; i < TAMANHO-1; i++)
    {
        min = v[i];
        pos_min = i;
        for (j=i+1; j < TAMANHO; j++) // Passo 1
        {
            if (min > v[j])
            {
                min = v[j];
                pos_min = j;
            }
        }
        if (pos_min != i)  // Passo 2
        {
            aux = v[pos_min];
            v[pos_min] = v[i];
            v[i] = aux;
        }
    }
}