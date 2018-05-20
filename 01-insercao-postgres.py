import psycopg2, datetime, insercao_mongo_exemplos

opcoes = "dbname='' user='' host='linux.ime.usp.br' password='' port='5432'" #Altere essa linha! - Para alterar o DB que sera acessado
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()
cursor.execute("SET search_path TO mac0439") #Altere essa linha - Para mudar o Schema utilizado

# DOADOR -----------------------------------------------------------------------------------------

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


# Pets do Doador
cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailDoador, 'Lôro', 'Papagaio', datetime.date(2010, 5, 5), insercao_mongo_exemplos.insertMongoPet("Loro")))
idPetDoacao = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailDoador, 'John', 'Cachorro', datetime.date(2012, 10, 6), insercao_mongo_exemplos.insertMongoPet("John")))
idPetCruzamento = cursor.fetchone()[0]

# Anúncio de doação do Lôro
cursor.execute("""
   INSERT INTO anuncio (id_pet, momento, tipo, data_inicio, data_termino)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (idPetDoacao, datetime.datetime.now(), 'Doacao', datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10)))
idAnuncio = cursor.fetchone()[0]

# Requisitos doação
cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, id_mongo_requisito, tipo)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Janelas teladas', insercao_mongo_exemplos.insertMongoRequisito("Janelas"), 'Obrigatorio'))

cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, id_mongo_requisito, tipo, peso)
   VALUES (%s, %s, %s, %s, %s)
""", (idAnuncio, 'Alpiste francês',insercao_mongo_exemplos.insertMongoRequisito("Alpiste"), 'Opcional', 1))

# Anúncio de cruzamento do John
cursor.execute("""
   INSERT INTO anuncio (id_pet, momento, tipo, data_inicio, data_termino)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (idPetCruzamento, datetime.datetime.now(), 'Breeding', datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10)))
idAnuncio = cursor.fetchone()[0]

# Requisitos cruzamento
cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, id_mongo_requisito, tipo)
   VALUES (%s, %s, %s, %s)
""", (idAnuncio, 'Pelo cor preta', insercao_mongo_exemplos.insertMongoRequisito("Pelo"), 'Obrigatorio'))

cursor.execute("""
   INSERT INTO requisito (id_anuncio, titulo, id_mongo_requisito, tipo, peso)
   VALUES (%s, %s, %s, %s, %s)
""", (idAnuncio, 'Raca Golden',insercao_mongo_exemplos.insertMongoRequisito("Raca"), 'Opcional', 1))


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
idPetServico = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Ol', 'Cachorro', datetime.date(2013, 11, 20), insercao_mongo_exemplos.insertMongoPet("Ol")))

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

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_mongo_pet)
   VALUES (%s, %s, %s, %s, %s) RETURNING id
""", (emailCandidato, 'Tana', 'Cobra', datetime.date(2013, 11, 20), insercao_mongo_exemplos.insertMongoPet("Tana")))

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

# EMPRESA -----------------------------------------------------------------------------------------

# Empresa

emailEmpresa = 'empresa@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s))
""", (emailEmpresa, '333', 'Empresa', 'Rua da Empresa, 30', 'Liberdade', 'São Paulo', 'SP',
      '33333333', '3333333', 1, 2))

cursor.execute("""
   INSERT INTO pessoa_juridica (email, cnpj)
   VALUES (%s, %s)
""", (emailEmpresa, '33333333333'))

# Servico que a empresa prestou ao Luke
cursor.execute("""
   INSERT INTO servico (email_empresa, id_pet, tipo_servico, id_mongo_servico)
   values (%s, %s, %s, %s)
""", (emailEmpresa, idPetServico, 'Tosa', insercao_mongo_exemplos.insertMongoServico("Tosa")))

# Avaliação do Servico do Luke
cursor.execute("""
   SELECT id_avaliavel
   FROM servico
   WHERE {} = id_pet
""".format(idPetServico));
servicoAvaliavelId = cursor.fetchone()[0]

cursor.execute("""
   SELECT email
   FROM usuario, pet
   WHERE {} = id and email = email_dono
""".format(idPetServico));
emailAvaliador = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO avaliacao (email_avaliador, id_avaliavel, nota, id_mongo_avaliacao)
   values (%s, %s, %s, %s)
""", (emailAvaliador, servicoAvaliavelId, 8, insercao_mongo_exemplos.insertMongoAvaliacao("Tosa")))

conexao.commit()
cursor.close()
conexao.close()
