SELECT
    "Data", "DestinoSKey", "EpisodioSKey", "EpisodioModuloSKey","EspecialidadeSKey",
    "EstruturaOrganicaSKey", "HoraId", "IdadeId", "MedicoSKey", "CodModulo", "ProvenienciaSKey",
    "SalaSKey", "SubSistemaSKey", "UnidadeSaudeDestinoSKey", "UnidadeSaudeProvenienciaSKey",
    "UtenteSkey", "Data Marcação Consulta", "Data Consulta", "Data Alta Consulta",
    "Episódio Consulta", "Estado Alta", "Código Secretariado", "Secretariado", "CodTipoAgenda", "Tipo Agenda",
    "CodTipoConsulta", "Tipo Consulta", "Tipo Consulta (detalhe)", "CodTipoMarcacao", "Tipo Marcação", "CodTipoVaga",
    "Tipo Vaga", "CodCausa", "Causa", "CodMotivoAnulacao", "Motivo Anulação", "Nº Sequencial", "Emissão Factura", 
    "Centro Custo", "Via CTH", "TMRG", "Ref. P1" 
FROM [db_name].[Views].[Consulta] 
WHERE 
    "Data Consulta" >= 1/1/2021
    -- NUMS: List of N_Sequencial of the appoitments for ConsultaMarcação
    AND "Nº Sequencial" IN (NUMS)
    AND "EspecialidadeSKey" IN (ESPECIALIDADES_TO_CONSIDER) 
    AND "Tipo Vaga" IS "Primeira" 
    AND "Tipo Consulta" IS "Consulta Médica"
; 