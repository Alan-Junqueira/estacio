### Union

- É usado para combinar os resultados de duas ou mais consultas SELECT. Ele retorna todos os registros distintos que aparecem em qualquer uma das consultas. Se você quiser incluir duplicatas, use UNION ALL.

### Intersect

- É usado para combinar os resultados de duas ou mais consultas SELECT e retornar apenas os registros que estão presentes em todas as consultas. Em outras palavras, ele retorna a interseção dos conjuntos de resultados, mostrando apenas os registros comuns.

### Except

- É usado para retornar os registros que estão presentes na primeira consulta, mas não na segunda. Em outras palavras, ele subtrai o conjunto de resultados da segunda consulta do conjunto de resultados da primeira consulta.

### Distinct

- É usado para remover duplicatas dos resultados de uma consulta, retornando apenas valores distintos (ou únicos). Isso é útil quando você quer garantir que os resultados retornados não contenham registros duplicados.

## Join

### Inner Join (ou Join)

- Retorna apenas os registros que têm correspondências em ambas as tabelas.

### Left Join (ou Left outer Join)

- Retorna todos os registros da tabela à esquerda (tabela1), e os registros correspondentes da tabela à direita (tabela2). Se não houver correspondência, os resultados da tabela à direita serão NULL.

### Right Join

- Retorna todos os registros da tabela à direita (tabela2), e os registros correspondentes da tabela à esquerda (tabela1). Se não houver correspondência, os resultados da tabela à esquerda serão NULL.

### Full Join (ou Full outer join)

- Retorna todos os registros quando há uma correspondência em uma das tabelas. Se não houver correspondência, os resultados serão NULL em qualquer tabela que não tenha correspondência.

### Cross Join

- Retorna o produto cartesiano das duas tabelas, ou seja, cada registro da primeira tabela é combinado com todos os registros da segunda tabela.
