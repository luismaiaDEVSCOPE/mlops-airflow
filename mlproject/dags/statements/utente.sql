SELECT
    [UtenteSkey], [GeografiaSKey], [Nº Sequencial], [Data Nascimento], [Sexo],
    [Nacionalidade], [Código Unidade Saúde], [Unidade Saúde]
FROM [dbo].[Utente]
WHERE 
    [Nº Sequencial] IN (%s)
;