SELECT [EspecialidadeSKey] 
FROM [dbo].[Especialidade]
WHERE [Grupo Especialidade] IN (
	'Pediatria', 'Cirurgia', 'Cirurgia Pediatrica', 'Cirurgia Vascular', 
	'Ortopedia',  'Dermatologia', 'Oftalmologia', 'Otorrino',
	'Peneumologia', 'Neurologia'
);