/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Consulta Marcação]
           ([UtenteSkey]
           ,[EspecialidadeSKey]
           ,[EstruturaOrganicaSKey]
           ,[MedicoSKey]
           ,[CodEstadoMarcação]
           ,[Estado Marcação]
           ,[Nº Sequencial]
           ,[Data Marcação Consulta]
           ,[Data Consulta]
           ,[Hora Consulta]
           ,[HoraId]
           ,[Data Registo Falta]
           ,[Data Desmarcação Consulta]
           ,[CodMotivo]
           ,[Motivo Desmarcação]
           ,[Responsável Desmarcação]
           ,[Tipo Consulta]
           ,[Tipo Vaga]
           ,[CodTipoAgenda]
           ,[Tipo Agenda]
           ,[RefLECSKey]
           ,[SalaSKey]
           ,[COD_SECRETARIADO]
           ,[ProvenienciaSKey]
           ,[UnidadeSaudeProvenienciaSKey])
     VALUES
           (<UtenteSkey] numeric(18,0),
           [EspecialidadeSKey] numeric(18,0),
           [EstruturaOrganicaSKey] numeric(18,0),
           [MedicoSKey] numeric(18,0),
           [CodEstadoMarcação] int,
           [Estado Marcação] varchar(30),
           [Nº Sequencial] decimal(8,0),
           [Data Marcação Consulta] date,
           [Data Consulta] date,
           [Hora Consulta] varchar(30),
           [HoraId] int,
           [Data Registo Falta] date,
           [Data Desmarcação Consulta] date,
           [CodMotivo] decimal(2,0),
           [Motivo Desmarcação] varchar(50),
           [Responsável Desmarcação] varchar(15),
           [Tipo Consulta] varchar(19),
           [Tipo Vaga] varchar(11),
           [CodTipoAgenda] varchar(1),
           [Tipo Agenda] varchar(50),
           [RefLECSKey] numeric(18,0),
           [SalaSKey] numeric(18,0),
           [COD_SECRETARIADO] decimal(3,0),
           [ProvenienciaSKey] numeric(18,0),
           [UnidadeSaudeProvenienciaSKey] numeric(18,0),)
GO
*/

USE [MyDb]
GO

CREATE TABLE [dbo].[Consulta Marcação](
    [UtenteSkey] numeric(18,0),
    [EspecialidadeSKey] numeric(18,0),
    [EstruturaOrganicaSKey] numeric(18,0),
    [MedicoSKey] numeric(18,0),
    [CodEstadoMarcação] int,
    [Estado Marcação] varchar(30),
    [Nº Sequencial] decimal(8,0),
    [Data Marcação Consulta] date,
    [Data Consulta] date,
    [Hora Consulta] varchar(30),
    [HoraId] int,
    [Data Registo Falta] date,
    [Data Desmarcação Consulta] date,
    [CodMotivo] decimal(2,0),
    [Motivo Desmarcação] varchar(50),
    [Responsável Desmarcação] varchar(15),
    [Tipo Consulta] varchar(19),
    [Tipo Vaga] varchar(11),
    [CodTipoAgenda] varchar(1),
    [Tipo Agenda] varchar(50),
    [RefLECSKey] numeric(18,0),
    [SalaSKey] numeric(18,0),
    [COD_SECRETARIADO] decimal(3,0),
    [ProvenienciaSKey] numeric(18,0),
    [UnidadeSaudeProvenienciaSKey] numeric(18,0),
);