create table marcavel (
	id SERIAL,
	tipo VARCHAR(12) CHECK (tipo = 'Usuario' OR tipo = 'Pet' OR tipo = 'Empresa'),
	primary key(id)
);

create table avaliavel (
	id SERIAL,
	tipo varchar(12) CHECK (tipo = 'Usuario' OR tipo = 'Pet' OR tipo = 'Anuncio' OR tipo = 'Servico' OR tipo = 'post'),
	primary key(id)
);

create table usuario (
	email	varchar(50),
	senha	varchar(50) NOT NULL,
	nome	varchar(50) NOT NULL,
	rua		varchar(50),
	bairro	varchar(50),
	cidade	varchar(50),
	estado	char(2),
	CEP	char(8),
	telefone varchar(12),
	lat_long point,
	id_mongo_usuario varchar(24),
	id_marcavel INT NOT NULL,
	id_avaliavel INT NOT NULL,
	primary key(email),
	foreign key(id_marcavel) references marcavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE
	
);

create table pessoa_fisica (
	email	varchar(50),
	cpf	char (11) UNIQUE,
	data_nasc	date,
	primary key(email),
	foreign key(email) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE
);

create table pessoa_juridica (
	email	varchar(50),
	cnpj	char (14) UNIQUE,
	primary key(email),
	foreign key(email) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE
);

create table pet (
	id SERIAL,
	email_dono	varchar(50) NOT NULL,
	nome varchar(50),
	especie varchar(50) NOT NULL,
	data_nasc date,
	id_mongo_pet varchar(24),
	id_marcavel INT NOT NULL,
	id_avaliavel INT NOT NULL,
	primary key(id),
	foreign key(email_dono) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_marcavel) references marcavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE
);

create table foto (
	id_pet SERIAL,
	id SERIAL,
	binario	BYTEA NOT NULL,
	formato varchar(10) NOT NULL,
	primary key(id_pet, id),
	foreign key(id_pet) references pet(id) ON DELETE CASCADE ON UPDATE CASCADE
);

create table visita (
	email_visitante varchar(50),
	id_pet INT,
	momento timestamp,
	comentario varchar(250),
	primary key(email_visitante, id_pet, momento),
	foreign key(id_pet) references pet(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(email_visitante) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE
);

create table post (
	email varchar(50),
	momento timestamp,
	titulo varchar(50) NOT NULL,
	id_mongo_post varchar(24),
	id_avaliavel INT,
	tem_midia boolean,
	CHECK(id_mongo_post IS NOT NULL OR tem_midia = 't'),
	primary key (email, momento),
	foreign key(email) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE
);

create table midia (
	email varchar(50),
	momento timestamp,
	binario_midia BYTEA,
	formato_midia varchar(10),
	primary key (email, momento),
	foreign key(email, momento) references post(email, momento) ON DELETE CASCADE ON UPDATE CASCADE
);

create table marcados_no_post (
	email varchar(50),
	momento timestamp,
	id_marcavel INT,
	foreign key(id_marcavel) references marcavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(email, momento) references post(email, momento) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key (email, momento)
);

create table avaliacao (
	email_avaliador	varchar(50),
	id_avaliavel INT,
	nota	INT NOT NULL,
	id_mongo_avaliacao	varchar(24),
	foreign key (email_avaliador) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(email_avaliador, id_avaliavel)
);

create table servico (
	email_empresa	varchar(50),
	id_pet	INT,
	tipo_servico	varchar(50),
	id_servico_mongo	varchar(24),
	id_avaliavel	INT NOT NULL,
	foreign key (email_empresa) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_pet) references pet(id) ON DELETE SET NULL ON UPDATE CASCADE,  -- preserva a informação do serviço prestado
	primary key(email_empresa, id_pet)
);

create table anuncio (
	id	SERIAL,
	id_pet	INT,
	momento timestamp,
	tipo	varchar(12) NOT NULL CHECK (tipo = 'Breeding' OR tipo = 'Doacao'),
	data_inicio	date NOT NULL,
	data_termino	date NOT NULL CHECK (data_inicio <= data_termino),
	id_avaliavel INT NOT NULL,
	status	varchar(12) DEFAULT 'Iniciado' NOT NULL,
		CHECK (status = 'Iniciado' OR status = 'Finalizado' OR status = 'Cancelado'),
	foreign key(id_pet) references pet(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_avaliavel) references avaliavel(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(id)
);

create table anuncio_cruzamento (
	id	INT,
	id_pet_escolhido	INT,
	foreign key(id_pet_escolhido) references pet(id) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id) references anuncio(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(id)
);

create table anuncio_doacao (
	id	INT,
	email_escolhido varchar(50),
	foreign key(email_escolhido) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id) references anuncio(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(id)
);

create table requisito (
	id_anuncio	INT,
	titulo	varchar(50) UNIQUE,
	id_mongo_requisito	varchar(24),
	tipo	varchar(24) CHECK(tipo = 'Obrigatorio' OR tipo = 'Opcional'),
	peso INT DEFAULT 1,
	primary key(id_anuncio, titulo),
	foreign key (id_anuncio) references anuncio(id) ON DELETE CASCADE ON UPDATE CASCADE
);

create table processo_cruzamento (
	id_anuncio	INT,
	id_pet_candidato	INT,
	data_inicio	date NOT NULL,
	data_termino	date NOT NULL CHECK (data_inicio <= data_termino),
	primary key(id_anuncio, id_pet_candidato),
	foreign key (id_anuncio) references anuncio(id) ON DELETE NO ACTION ON UPDATE CASCADE, -- requer notificar os candidatos da exclusão
	foreign key(id_pet_candidato) references pet(id) ON DELETE CASCADE ON UPDATE CASCADE
);

create table  processo_doacao (
	id_anuncio	INT,
	email_candidato varchar(50),
	data_inicio	date NOT NULL,
	data_termino	date NOT NULL CHECK (data_inicio <= data_termino),
	primary key(id_anuncio, email_candidato),
	foreign key(email_candidato) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_anuncio) references anuncio(id) ON DELETE NO ACTION ON UPDATE CASCADE -- requer notificar os candidatos da exclusão
);

create table status_requisito_cruzamento (
	id_anuncio	INT,
	id_pet_candidato	INT,
	titulo	varchar(50),
	status varchar(50) check (status = 'a verificar' OR status = 'cumprido' OR status = 'nao cumprido'),
	foreign key(titulo) references requisito(titulo)  ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(id_pet_candidato) references pet(id)  ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_anuncio) references anuncio(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(id_anuncio, titulo, id_pet_candidato)
);

create table status_requisito_doacao (
	id_anuncio	INT,
	titulo	varchar(50),
	email_candidato varchar(50),
	status varchar(50) check (status = 'a verificar' OR status = 'cumprido' OR status = 'nao cumprido'),
	foreign key(email_candidato) references usuario(email) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key(titulo) references requisito(titulo) ON DELETE CASCADE ON UPDATE CASCADE,
	foreign key (id_anuncio) references anuncio(id) ON DELETE CASCADE ON UPDATE CASCADE,
	primary key(id_anuncio, titulo, email_candidato)
);
