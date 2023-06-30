/* GRUPO 6
DAVI FAGUNDES FERREIRA DA SILVA		12544013
GUSTAVO SAMPAIO LIMA				12623992
PEDRO ROSSI SILVA RODRIGUES			11871775
THAÍS RIBEIRO LAURIANO 				12542518
THIERRY ARAÚJO DE SOUZA				12681094  
*/

-- Selecionar as comunidades que possuem contrato ativo de fornecimento entre 12/2022 e 05/2023
SELECT F.COMUNIDADE as ID_COMUNIDADE, C.NOME, P.INICIO_CONTRATO, ADD_MONTHS(P.INICIO_CONTRATO, P.DURACAO_CONTRATO) as FIM_CONTRATO
FROM  FORNECIMENTO F
JOIN COMUNIDADE C ON F.COMUNIDADE = C.ID_COMUNIDADE
JOIN PROVEDOR P ON P.CNPJ = F.PROVEDOR
WHERE
   ADD_MONTHS(P.INICIO_CONTRATO, P.DURACAO_CONTRATO) >= '01/12/2022' AND
    P.INICIO_CONTRATO <= '31/05/2023';


-- Selecionar todas as comunidades que falam todas as línguas cadastradas em DialetosComunidade
SELECT C.NOME
FROM COMUNIDADE C
JOIN DIALETOS_COMUNIDADE DC ON C.ID_COMUNIDADE = DC.COMUNIDADE
GROUP BY C.NOME
HAVING COUNT(DISTINCT DC.DIALETO) = (SELECT COUNT(DISTINCT DIALETO) FROM DIALETOS_COMUNIDADE);


-- Localizar, em ordem decrescente de custo, os roteadores mais caros disponíveis para cada comunidade.
SELECT R.MAC_ADRESS, R.MODELO, F.CUSTO, C.NOME
FROM ROTEADOR R
JOIN FORNECIMENTO F ON R.MAC_ADRESS = F.ROTEADOR
JOIN COMUNIDADE C ON F.COMUNIDADE = C.ID_COMUNIDADE
WHERE (
    SELECT COUNT(*)
    FROM FORNECIMENTO F2
    WHERE F2.COMUNIDADE = F.COMUNIDADE AND F2.CUSTO >= F.CUSTO
) <= 1
ORDER BY F.CUSTO DESC;

-- Selecionar o gasto com roteadores por estado em ordem crescente.
SELECT C.ESTADO, SUM(F.CUSTO) AS GASTO_TOTAL
FROM FORNECIMENTO F
JOIN ROTEADOR R ON F.ROTEADOR = R.MAC_ADDRESS
JOIN COMUNIDADE C ON F.COMUNIDADE = C.ID_COMUNIDADE
GROUP BY C.ESTADO
ORDER BY GASTO_TOTAL ASC;

-- Selecionar a velocidade média dos roteadores por estado
SELECT C.ESTADO, AVG(R.VELOCIDADE_MBPS) AS VELOCIDADE_MEDIA
FROM FORNECIMENTO F
JOIN ROTEADOR R ON F.ROTEADOR = R.MAC_ADDRESS
JOIN COMUNIDADE C ON F.COMUNIDADE = C.ID_COMUNIDADE
GROUP BY C.ESTADO
ORDER BY VELOCIDADE_MEDIA DESC;
