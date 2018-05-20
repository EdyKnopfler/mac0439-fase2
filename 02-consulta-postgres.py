from conexao import conexao, cursor

cursor.execute("""
   SELECT COUNT(*)
   FROM requisito
   WHERE id_anuncio = 2 AND tipo = 'Obrigatorio'
""");

quantidade = cursor.fetchone()[0]
print("\nO anúncio de doação possui %d requisito(s) obrigatório(s)." % (quantidade,))

cursor.execute("""
   SELECT
      u.nome, COUNT(*)
   FROM
      status_requisito_doacao st
      JOIN requisito req
         ON st.id_anuncio = req.id_anuncio AND st.titulo = req.titulo
      JOIN usuario u ON st.email_candidato = u.email
   WHERE st.id_anuncio = 2 AND st.status = 'cumprido' AND req.tipo = 'Obrigatorio'
   GROUP BY u.nome
""")

print("\nQuantidade de requisitos obrigatórios cumpridos:")
for tupla in cursor:
   print("%s (%d)" % tupla)
cursor.execute("""
   SELECT
      u.nome, SUM(req.peso)
   FROM
      status_requisito_doacao st
      JOIN requisito req
         ON st.id_anuncio = req.id_anuncio AND st.titulo = req.titulo
      JOIN usuario u ON st.email_candidato = u.email
   WHERE st.id_anuncio = 2 AND st.status = 'cumprido' AND req.tipo = 'Opcional'
   GROUP BY u.nome
""")

print("\nPeso total de requisitos não obrigatórios cumpridos:")
for tupla in cursor:
   print("%s (%d)" % tupla)

cursor.close()
conexao.close()
