/*

USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Consulta]
           ([Data]
           ,[DestinoSKey]
           ,[EpisodioSKey]
           ,[EpisodioModuloSKey]
           ,[EspecialidadeSKey]
           ,[EstruturaOrganicaSKey]
           ,[HoraId]
           ,[IdadeId]
           ,[MedicoSKey]
           ,[CodModulo]
           ,[ProvenienciaSKey]
           ,[SalaSKey]
           ,[SubSistemaSKey]
           ,[UnidadeSaudeDestinoSKey]
           ,[UnidadeSaudeProvenienciaSKey]
           ,[UtenteSkey]
           ,[Data Marcação Consulta]
           ,[Data Consulta]
           ,[Data Alta Consulta]
           ,[Episódio Consulta]
           ,[Estado Alta]
           ,[Nº Beneficiário]
           ,[Código Secretariado]
           ,[Secretariado]
           ,[CodTipoAgenda]
           ,[Tipo Agenda]
           ,[CodTipoConsulta]
           ,[Tipo Consulta]
           ,[Tipo Consulta (detalhe)]
           ,[CodTipoMarcacao]
           ,[Tipo Marcação]
           ,[CodTipoVaga]
           ,[Tipo Vaga]
           ,[CodCausa]
           ,[Causa]
           ,[CodMotivoAnulacao]
           ,[Motivo Anulação]
           ,[Nº Sequencial]
           ,[Emissão Factura]
           ,[Centro Custo]
           ,[Via CTH]
           ,[TMRG]
           ,[Ref. P1])
     VALUES
           (<Data, date,>
           ,<DestinoSKey, numeric(18,0),>
           ,<EpisodioSKey, numeric(18,0),>
           ,<EpisodioModuloSKey, varchar(33),>
           ,<EspecialidadeSKey, numeric(18,0),>
           ,<EstruturaOrganicaSKey, numeric(18,0),>
           ,<HoraId, int,>
           ,<IdadeId, int,>
           ,<MedicoSKey, numeric(18,0),>
           ,<CodModulo, varchar(3),>
           ,<ProvenienciaSKey, numeric(18,0),>
           ,<SalaSKey, numeric(18,0),>
           ,<SubSistemaSKey, numeric(18,0),>
           ,<UnidadeSaudeDestinoSKey, numeric(18,0),>
           ,<UnidadeSaudeProvenienciaSKey, numeric(18,0),>
           ,<UtenteSkey, numeric(18,0),>
           ,<Data Marcação Consulta, date,>
           ,<Data Consulta, date,>
           ,<Data Alta Consulta, date,>
           ,<Episódio Consulta, numeric(14,0),>
           ,<Estado Alta, varchar(8),>
           ,<Nº Beneficiário, varchar(20),>
           ,<Código Secretariado, decimal(3,0),>
           ,<Secretariado, varchar(20),>
           ,<CodTipoAgenda, varchar(1),>
           ,<Tipo Agenda, varchar(15),>
           ,<CodTipoConsulta, varchar(6),>
           ,<Tipo Consulta, varchar(19),>
           ,<Tipo Consulta (detalhe), varchar(50),>
           ,<CodTipoMarcacao, varchar(1),>
           ,<Tipo Marcação, varchar(50),>
           ,<CodTipoVaga, varchar(1),>
           ,<Tipo Vaga, varchar(50),>
           ,<CodCausa, decimal(2,0),>
           ,<Causa, varchar(30),>
           ,<CodMotivoAnulacao, decimal(2,0),>
           ,<Motivo Anulação, varchar(30),>
           ,<Nº Sequencial, decimal(8,0),>
           ,<Emissão Factura, varchar(1),>
           ,<Centro Custo, decimal(9,0),>
           ,<Via CTH, varchar(3),>
           ,<TMRG, int,>
           ,<Ref. P1, varchar(20),>)
GO
*/

CREATE TABLE [dbo].[Consulta](
    [Data] date,
    [DestinoSKey] numeric(18,0),
    [EpisodioSKey] numeric(18,0),
    [EpisodioModuloSKey] varchar(33),
    [EspecialidadeSKey] numeric(18,0),
    [EstruturaOrganicaSKey] numeric(18,0),
    [HoraId] int,
    [IdadeId] int,
    [MedicoSKey] numeric(18,0),
    [CodModulo] varchar(3),
    [ProvenienciaSKey] numeric(18,0),
    [SalaSKey] numeric(18,0),
    [SubSistemaSKey] numeric(18,0),
    [UnidadeSaudeDestinoSKey] numeric(18,0),
    [UnidadeSaudeProvenienciaSKey] numeric(18,0),
    [UtenteSkey] numeric(18,0),
    [Data Marcação Consulta] date,
    [Data Consulta] date,
    [Data Alta Consulta] date,
    [Episódio Consulta] numeric(14,0),
    [Estado Alta] varchar(8),
    [Nº Beneficiário] varchar(20),
    [Código Secretariado] decimal(3,0),
    [Secretariado] varchar(20),
    [CodTipoAgenda] varchar(1),
    [Tipo Agenda] varchar(15),
    [CodTipoConsulta] varchar(6),
    [Tipo Consulta] varchar(19),
    [Tipo Consulta (detalhe)] varchar(50),
    [CodTipoMarcacao] varchar(1),
    [Tipo Marcação] varchar(50),
    [CodTipoVaga] varchar(1),
    [Tipo Vaga] varchar(50),
    [CodCausa] decimal(2,0),
    [Causa] varchar(30),
    [CodMotivoAnulacao] decimal(2,0),
    [Motivo Anulação] varchar(30),
    [Nº Sequencial] decimal(8,0),
    [Emissão Factura] varchar(1),
    [Centro Custo] decimal(9,0),
    [Via CTH] varchar(3),
    [TMRG] int,
    [Ref. P1] varchar(20),
);