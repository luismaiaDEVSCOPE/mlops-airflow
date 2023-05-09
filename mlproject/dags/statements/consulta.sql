SELECT
    [Data], [DestinoSKey], [EpisodioSKey], [EpisodioModuloSKey], [EspecialidadeSKey],
    [EstruturaOrganicaSKey], [HoraId], [IdadeId], [MedicoSKey], [CodModulo], [ProvenienciaSKey],
    [SalaSKey], [SubSistemaSKey], [UnidadeSaudeDestinoSKey], [UnidadeSaudeProvenienciaSKey],
    [UtenteSkey], [Data Marcação Consulta], [Data Consulta], [Data Alta Consulta],
    [Episódio Consulta], [Estado Alta], [Código Secretariado], [Secretariado], [CodTipoAgenda], [Tipo Agenda],
    [CodTipoConsulta], [Tipo Consulta], [Tipo Consulta (detalhe)], [CodTipoMarcacao], [Tipo Marcação], [CodTipoVaga],
    [Tipo Vaga], [CodCausa], [Causa], [CodMotivoAnulacao], [Motivo Anulação], [Nº Sequencial], [Emissão Factura], 
    [Centro Custo], [Via CTH], [TMRG], [Ref. P1]
FROM [dbo].[Consulta] 
WHERE 
    -- DATEDIFF(day, [Data Consulta], CAST( GETDATE() AS Date )) <= 30
	DATEDIFF(%s, [Data Consulta], CAST('%s' as date)) <= %d
    AND [Nº Sequencial] IN (%s)
    AND [EspecialidadeSKey] IN (%s) 
    AND [Tipo Vaga] = 'Primeira' 
    AND [Tipo Consulta] = 'Consulta Médica'
    -- AND [Data Consulta] > CAST('01/01/2023' as date)
;