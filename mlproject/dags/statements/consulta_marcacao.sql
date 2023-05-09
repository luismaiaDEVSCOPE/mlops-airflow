SELECT
    [UtenteSkey], [EspecialidadeSKey], [EstruturaOrganicaSKey], [MedicoSKey],
    [CodEstadoMarcação], [Estado Marcação], [Nº Sequencial], [Data Marcação Consulta], [Data Consulta], [Hora Consulta],
    [HoraId], [Data Registo Falta], [Data Desmarcação Consulta], [CodMotivo], [Motivo Desmarcação], 
    [Responsável Desmarcação], [Tipo Consulta], [Tipo Vaga], [CodTipoAgenda], [Tipo Agenda], [RefLECSKey], [SalaSKey], 
    [COD_SECRETARIADO], [ProvenienciaSKey], [UnidadeSaudeProvenienciaSKey]
FROM [dbo].[Consulta Marcação]
WHERE 
	-- DATEDIFF(day, [Data Marcação Consulta], CAST( GETDATE() AS Date )) <= 7
	DATEDIFF(%s, [Data Marcação Consulta], CAST('%s' as date)) <= %d
    AND [EspecialidadeSKey] IN (%s) 
    AND [Tipo Vaga] = 'Primeira'
    AND [Tipo Consulta] = 'Consulta Médica'
    -- AND "Data Marcação Consulta" >= 1/1/2021;
;