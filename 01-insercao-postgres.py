import psycopg2, datetime

opcoes = "dbname='mac0439' user='ederson' host='localhost' password='jethrotull' port='5432'"
conexao = psycopg2.connect(opcoes)
cursor = conexao.cursor()


# Doador
cursor.execute("INSERT INTO marcavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idMarcavelDoador = cursor.fetchone()[0]

cursor.execute("INSERT INTO avaliavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idAvaliavelDoador = cursor.fetchone()[0]

emailDoador = 'doador@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long, id_marcavel, id_avaliavel)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s), %s, %s)
""", (emailDoador, '123', 'Doador', 'Rua dos Doadores, 100', 'Centro', 'São Paulo', 'SP', 
      '00000000', '00000000000', 10, 10, idMarcavelDoador, idAvaliavelDoador))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailDoador, '00000000000', datetime.date(1990, 10, 10)))


# Pet
cursor.execute("INSERT INTO marcavel (tipo) VALUES (%s) RETURNING id", ('Pet',))
idMarcavelPet = cursor.fetchone()[0]

cursor.execute("INSERT INTO avaliavel (tipo) VALUES (%s) RETURNING id", ('Pet',))
idAvaliavelPet = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO pet (email_dono, nome, especie, data_nasc, id_marcavel, id_avaliavel)
   VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
""", (emailDoador, 'Lôro', 'Papagaio', datetime.date(2010, 5, 5), idMarcavelPet, idAvaliavelPet))
idPet = cursor.fetchone()[0]


# Anúncio de doação
cursor.execute("INSERT INTO avaliavel (tipo) VALUES (%s) RETURNING id", ('Anuncio',))
idAvaliavelAnuncio = cursor.fetchone()[0]

cursor.execute("""
   INSERT INTO anuncio (id_pet, momento, tipo, data_inicio, data_termino, id_avaliavel)
   VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
""", (idPet, datetime.datetime.now(), 'Doacao', datetime.datetime.now(),
      datetime.datetime.now() + datetime.timedelta(days=10), idAvaliavelAnuncio))
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
cursor.execute("INSERT INTO marcavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idMarcavelCandidato = cursor.fetchone()[0]

cursor.execute("INSERT INTO avaliavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idAvaliavelCandidato = cursor.fetchone()[0]

emailCandidato = 'candidato1@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long, id_marcavel, id_avaliavel)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s), %s, %s)
""", (emailCandidato, '321', 'Candidato 1', 'Rua dos Candidatos, 200', 'Liberdade', 'São Paulo', 'SP', 
      '11111111', '11111111111', 11, 20, idMarcavelCandidato, idAvaliavelCandidato))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailCandidato, '11111111111', datetime.date(1995, 12, 10)))


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
cursor.execute("INSERT INTO marcavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idMarcavelCandidato = cursor.fetchone()[0]

cursor.execute("INSERT INTO avaliavel (tipo) VALUES (%s) RETURNING id", ('Usuario',))
idAvaliavelCandidato = cursor.fetchone()[0]

emailCandidato = 'candidato2@mac0439.com'

cursor.execute("""
   INSERT INTO usuario (email, senha, nome, rua, bairro, cidade, estado, cep, telefone,
                        lat_long, id_marcavel, id_avaliavel)
   values (%s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s), %s, %s)
""", (emailCandidato, '321', 'Candidato 2', 'Rua dos Candidatos, 200', 'Liberdade', 'São Paulo', 'SP', 
      '22222222', '22222222222', 12, 21, idMarcavelCandidato, idAvaliavelCandidato))

cursor.execute("""
   INSERT INTO pessoa_fisica (email, cpf, data_nasc)
   VALUES (%s, %s, %s)
""", (emailCandidato, '22222222222', datetime.date(1985, 1, 20)))


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
