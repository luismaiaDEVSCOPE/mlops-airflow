USE [MyDb]
GO

CREATE TABLE [dbo].[Consulta Marca��o] (
    [UtenteSkey] numeric(18,0),
    [EspecialidadeSKey] numeric(18,0),
    [EstruturaOrganicaSKey] numeric(18,0),
    [MedicoSKey] numeric(18,0),
    [CodEstadoMarca��o] int,
    [Estado Marca��o] varchar(30),
    [N� Sequencial] decimal(8,0),
    [Data Marca��o Consulta] date,
    [Data Consulta] date,
    [Hora Consulta] varchar(30),
    [HoraId] int,
    [Data Registo Falta] date,
    [Data Desmarca��o Consulta] date,
    [CodMotivo] decimal(2,0),
    [Motivo Desmarca��o] varchar(50),
    [Respons�vel Desmarca��o] varchar(15),
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
    [N� Sequencial] decimal(8,0),
    [Data Nascimento] datetime2(7),
    [Idade Atual] int,
    [N� Processo] numeric(14,0),
    [N� Utente SNS] decimal(12,0),
    [Nome] varchar(100),
    [CodSexo] varchar(1),
    [Sexo] varchar(50),
    [Nacionalidade] varchar(30),
    [Morada] varchar(200),
    [C�digo Postal] varchar(13),
    [Telefone] varchar(15),
    [Telem�vel] varchar(15),
    [Email] varchar(200),
    [C�digo Unidade Sa�de] decimal(7,0),
    [Unidade Sa�de] varchar(50),
    [M�dico Centro Sa�de] varchar(25),
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
    [Data Marca��o Consulta] date,
    [Data Consulta] date,
    [Data Alta Consulta] date,
    [Epis�dio Consulta] numeric(14,0),
    [Estado Alta] varchar(8),
    [N� Benefici�rio] varchar(20),
    [C�digo Secretariado] decimal(3,0),
    [Secretariado] varchar(20),
    [CodTipoAgenda] varchar(1),
    [Tipo Agenda] varchar(15),
    [CodTipoConsulta] varchar(6),
    [Tipo Consulta] varchar(19),
    [Tipo Consulta (detalhe)] varchar(50),
    [CodTipoMarcacao] varchar(1),
    [Tipo Marca��o] varchar(50),
    [CodTipoVaga] varchar(1),
    [Tipo Vaga] varchar(50),
    [CodCausa] decimal(2,0),
    [Causa] varchar(30),
    [CodMotivoAnulacao] decimal(2,0),
    [Motivo Anula��o] varchar(30),
    [N� Sequencial] decimal(8,0),
    [Emiss�o Factura] varchar(1),
    [Centro Custo] decimal(9,0),
    [Via CTH] varchar(3),
    [TMRG] int,
    [Ref. P1] varchar(20),
);

CREATE TABLE [dbo].[Especialidade](
	[EspecialidadeSKey] numeric(18,0),
	[GrupoEspecialidadeSKey] decimal(2,0),
	[CodEspecialidade] numeric(5,0),
	[C�digo Especialidade] numeric(5,0),
	[Especialidade] varchar(80),
	[CodGrupoEspecialidade] decimal(2,0),
	[Grupo Especialidade] varchar(30),
	[Especialidade M�dulo] varchar(8),
	[CodECLIN] varchar(5),
	[Estado] varchar(8),
);

CREATE TABLE [dbo].[Unidade Sa�de Destino](
    [C�digo Unidade Destino] decimal(7,0),
    [Unidade Destino] varchar(50),
    [Tipo Unidade Destino] varchar(1),
);

CREATE TABLE [dbo].[Unidade Sa�de Proveni�ncia](
    [C�digo Unidade Proveni�ncia] decimal(7,0),
    [Unidade Proveni�ncia] varchar(50),
    [Tipo Unidade Proveni�ncia] varchar(1),
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

CREATE TABLE [dbo].[Proveni�ncia] (
    [CodProveniencia] decimal(2,0),
    [Proveni�ncia] varchar(30),
);