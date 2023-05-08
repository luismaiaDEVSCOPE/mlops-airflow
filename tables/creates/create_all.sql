USE [MyDb]
GO

CREATE TABLE [dbo].[Consulta Marcação] (
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

CREATE TABLE [dbo].[Utente] (
    [UtenteSkey] numeric(18,0),
    [GeografiaSKey] numeric(18,0),
    [Nº Sequencial] decimal(8,0),
    [Data Nascimento] datetime2(7),
    [Idade Atual] int,
    [Nº Processo] numeric(14,0),
    [Nº Utente SNS] decimal(12,0),
    [Nome] varchar(100),
    [CodSexo] varchar(1),
    [Sexo] varchar(50),
    [Nacionalidade] varchar(30),
    [Morada] varchar(200),
    [Código Postal] varchar(13),
    [Telefone] varchar(15),
    [Telemóvel] varchar(15),
    [Email] varchar(200),
    [Código Unidade Saúde] decimal(7,0),
    [Unidade Saúde] varchar(50),
    [Médico Centro Saúde] varchar(25),
);

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

CREATE TABLE [dbo].[Especialidade](
	[EspecialidadeSKey] numeric(18,0),
	[GrupoEspecialidadeSKey] decimal(2,0),
	[CodEspecialidade] numeric(5,0),
	[Código Especialidade] numeric(5,0),
	[Especialidade] varchar(80),
	[CodGrupoEspecialidade] decimal(2,0),
	[Grupo Especialidade] varchar(30),
	[Especialidade Módulo] varchar(8),
	[CodECLIN] varchar(5),
	[Estado] varchar(8),
);

CREATE TABLE [dbo].[Unidade Saúde Destino](
    [Código Unidade Destino] decimal(7,0),
    [Unidade Destino] varchar(50),
    [Tipo Unidade Destino] varchar(1),
);

CREATE TABLE [dbo].[Unidade Saúde Proveniência](
    [Código Unidade Proveniência] decimal(7,0),
    [Unidade Proveniência] varchar(50),
    [Tipo Unidade Proveniência] varchar(1),
);

CREATE TABLE [dbo].[Destino](
    [CodDestino] decimal(2,0),
    [Destino] varchar(30),
);

CREATE TABLE [dbo].[Geografia](
    [GeografiaSKey] numeric(18,0),
    [CodDistrito] decimal(2,0),
    [Distirito] varchar(30),
    [CodConcelho] decimal(2,0),
    [Concelho] varchar(30),
    [CodFreguesia] decimal(2,0),
    [Freguesia] varchar(30),
    [Freguesia Geo] varchar(101),
    [Concelho Geo] varchar(70),
    [Distrito Geo] varchar(39),
);

CREATE TABLE [dbo].[Proveniência] (
    [CodProveniencia] decimal(2,0),
    [Proveniência] varchar(30),
);