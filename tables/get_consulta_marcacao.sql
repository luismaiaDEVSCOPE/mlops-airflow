SELECT TOP(5) 
    [UtenteSkey], [EspecialidadeSKey], [EstruturaOrganicaSKey], [MedicoSKey],
    [CodEstadoMarcação], [Estado Marcação], [Nº Sequencial], [Data Marcação Consulta], [Data Consulta], [Hora Consulta],
    [HoraId], [Data Registo Falta], [Data Desmarcação Consulta], [CodMotivo], [Motivo Desmarcação], 
    [Responsável Desmarcação], [Tipo Consulta], [Tipo Vaga], [CodTipoAgenda], [Tipo Agenda], [RefLECSKey], [SalaSKey], 
    [COD_SECRETARIADO], [ProvenienciaSKey], [UnidadeSaudeProvenienciaSKey]
FROM [dbo].[Consulta Marcação]
WHERE 
    -- '7 DAYS' needs to be a configurable variable equal to the value of scheduling fo the DAG
    -- Example of Approach to do things: 'TODAY' represents 00:00 and this DAG runs on 23:59
	-- DATEDIFF(day, [Data Marcação Consulta], CAST( GETDATE() AS Date )) <= 7
	DATEDIFF(day, [Data Marcação Consulta], CAST('01/24/2023' as date)) <= 7
    -- ESPECIALIDADES_TO_CONSIDER: List of considerd especilaides. This list can be "updated" in the retraining DAG. 
    -- Example: SELECT ID FROM ESP WHERE "name" IN (NAME_LIST)
    -- AND [EspecialidadeSKey] IN (ESPECIALIDADES_TO_CONSIDER) 
    AND [EspecialidadeSKey] IN (6, 7, 8) 
    AND [Tipo Vaga] = 'Primeira'
    AND [Tipo Consulta] = 'Consulta Médica'
    -- AND "Data Marcação Consulta" >= 1/1/2021; -- Redundunt
;