import psycopg2, datetime, insercao_mongo_exemplos

opcoes = "dbname='' user='' host='linux.ime.usp.br' password='' port='5432'" #Altere essa linha! - Para alterar o DB que sera acessado
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()
cursor.execute("SET search_path TO mac0439") #Altere essa linha - Para mudar o Schema utilizado

# Doador

emailDoador = 'doador@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s))
""", (emailDoador, '123', 'Doador', 'Rua dos Doadores, 100', 'Centro', 'São Paulo', 'SP',
      '00000000', '00000000000', 10, 10))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailDoador, '00000000000', datetime.date(1990, 10, 10)))


# Pet

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailDoador, 'Lôro', 'Papagaio', datetime.date(2010, 5, 5), insercao_mongo_exemplos.insertMongoPet("Loro")))
idPet = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailDoador, 'John', 'Cachorro', datetime.date(2012, 10, 6), insercao_mongo_exemplos.insertMongoPet("John")))
idPet = cursor.fetchone()[0]


# Anúncio de doação
cursor.execute("""
   INSERT INTO anuncio (id_pet, momento, tipo, data_inicio, data_termino)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (idPet, datetime.datetime.now(), 'Doacao', datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10)))
idAnuncio = cursor.fetchone()[0]


# Requisitos
cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, tipo)
   VALUES (%s, %s, %s)
""", (idAnuncio, 'Janelas teladas', 'Obrigatorio'))

cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, tipo, peso)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Alpiste francês', 'Opcional', 1))



# CANDIDATO 1 -----------------------------------------------------------------------------------------

# Candidato

emailCandidato = 'candidato1@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s))
""", (emailCandidato, '321', 'Candidato 1', 'Rua dos Candidatos, 200', 'Liberdade', 'São Paulo', 'SP',
      '11111111', '11111111111', 11, 20))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailCandidato, '11111111111', datetime.date(1995, 12, 10)))

#Pets do Candidato 1
cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Luke', 'Gato', datetime.date(2013, 11, 20), insercao_mongo_exemplos.insertMongoPet("Luke")))
idPet = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Ol', 'Cachorro', datetime.date(2013, 11, 20), insercao_mongo_exemplos.insertMongoPet("Ol")))
idPet = cursor.fetchone()[0]


# Processo de doação
cursor.execute("""
   INSERT INTO processo_doacao (id_anuncio, email_candidato, data_inicio, data_termino)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, emailCandidato, datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10)))

# Status dos requisitos
cursor.execute("""
   INSERT INTO status_requisito_doacao (id_anuncio, titulo, email_candidato, status)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Janelas teladas', emailCandidato, 'cumprido'))

cursor.execute("""
   INSERT INTO status_requisito_doacao (id_anuncio, titulo, email_candidato, status)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Alpiste francês', emailCandidato, 'cumprido'))



# CANDIDATO 2 -----------------------------------------------------------------------------------------

# Candidato

emailCandidato = 'candidato2@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s))
""", (emailCandidato, '321', 'Candidato 2', 'Rua dos Candidatos, 200', 'Liberdade', 'São Paulo', 'SP',
      '22222222', '22222222222', 12, 21))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailCandidato, '22222222222', datetime.date(1985, 1, 20)))

# Pets do Candidato 2
cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Azuril', 'Peixe', datetime.date(2017, 1, 30), insercao_mongo_exemplos.insertMongoPet("Azuril")))
idPet = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Tana', 'Cobra', datetime.date(2013, 11, 20), insercao_mongo_exemplos.insertMongoPet("Tana")))
idPet = cursor.fetchone()[0]


# Processo de doação
cursor.execute("""
   INSERT INTO processo_doacao (id_anuncio, email_candidato, data_inicio, data_termino)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, emailCandidato, datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10)))

# Status dos requisitos
cursor.execute("""
   INSERT INTO status_requisito_doacao (id_anuncio, titulo, email_candidato, status)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Janelas teladas', emailCandidato, 'cumprido'))

conexao.commit()
cursor.close()
conexao.close()
