SELECT
    "UtenteSkey", "GeografiaSKey", "Nº Sequencial", "Data Nascimento", "Sexo", "Nacionalidade",
    "Código Unidade Saúde", "Unidade Saúde"
FROM [db_name].[Views].[Utente]
WHERE 
    -- NUMS: List of N_Sequencial of the appointments for ConsultaMarcação
    "Nº Sequencial" IN (NUMS)
;