void bubbleSort (int *v)
{
	int troca=1;
	int i=0;
	int aux;
	while (troca)
	{
		troca = 0;
		while (i < SIZE - 1)
		{
			if (v[i] > v[i+1])
			{
				aux = v[i];
				v[i] = v[i+1];
				v[i+1] = aux;
				troca = 1;
			}
			i++;
		}
		i = 0;
	}
}
