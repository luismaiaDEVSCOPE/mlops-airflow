/*
USE [SSDH_BI_DataWarehouse]
GO

INSERT INTO [tab].[Especialidade]
           ([EspecialidadeSKey]
           ,[GrupoEspecialidadeSKey]
           ,[CodEspecialidade]
           ,[Código Especialidade]
           ,[Especialidade]
           ,[CodGrupoEspecialidade]
           ,[Grupo Especialidade]
           ,[Especialidade Módulo]
           ,[CodECLIN]
           ,[Estado])
     VALUES
           (<EspecialidadeSKey, numeric(18,0),>
           ,<GrupoEspecialidadeSKey, decimal(2,0),>
           ,<CodEspecialidade, numeric(5,0),>
           ,<Código Especialidade, numeric(5,0),>
           ,<Especialidade, varchar(80),>
           ,<CodGrupoEspecialidade, decimal(2,0),>
           ,<Grupo Especialidade, varchar(30),>
           ,<Especialidade Módulo, varchar(8),>
           ,<CodECLIN, varchar(5),>
           ,<Estado, varchar(8),>)
GO

*/

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