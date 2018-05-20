set search_path to mac0439; --Altere essa linha - Para mudar o Schema utilizado

-- Cria Marcável e Avaliável para usuário --
CREATE OR REPLACE FUNCTION InsereMarcavelAvaliavel()
RETURNS TRIGGER AS $$
DECLARE
   tipao TEXT;
BEGIN
   tipao = TG_ARGV[0];
   INSERT INTO marcavel(tipo) VALUES (tipao) RETURNING id into NEW.id_marcavel;
   INSERT INTO avaliavel(tipo) VALUES (tipao) RETURNING id into NEW.id_avaliavel;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS MarcaUsuario ON usuario;
CREATE TRIGGER MarcaUsuario
BEFORE INSERT ON usuario
FOR EACH ROW
EXECUTE PROCEDURE InsereMarcavelAvaliavel();

-- Cria Marcável e Avaliável para pet --
DROP TRIGGER IF EXISTS MarcaPet ON pet;
CREATE TRIGGER MarcaPet
BEFORE INSERT ON pet
FOR EACH ROW
EXECUTE PROCEDURE InsereMarcavelAvaliavel('Pet');

-- Deleta o marcável e o Avaliável para usuario --
CREATE OR REPLACE FUNCTION DeleteMarcavelAvaliavel()
RETURNS TRIGGER AS $$
BEGIN
   DELETE FROM marcavel r1 WHERE r1.id = OLD.id_marcavel;
   DELETE FROM avaliavel r2 WHERE r2.id = OLD.id_avaliavel;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS DeleteUsuario ON usuario;
CREATE TRIGGER DeleteUsuario
AFTER DELETE ON usuario
FOR EACH ROW
EXECUTE PROCEDURE DeleteMarcavelAvaliavel();

-- Deleta marcável e Avaliável para pet --
DROP TRIGGER IF EXISTS DeletePet ON pet;
CREATE TRIGGER DeletePet
AFTER DELETE ON pet
FOR EACH ROW
EXECUTE PROCEDURE DeleteMarcavelAvaliavel();


-- Insere Status para processo de cruzamento --
CREATE OR REPLACE FUNCTION CriaStatusCruzamento()
RETURNS TRIGGER AS $$
BEGIN
   INSERT INTO status_requisito_cruzamento VALUES (OLD.id_anuncio, OLD.id_pet_candidato, 'Insira seu Título', 'a verificar');
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS StatusProcessoCruzamento ON processo_cruzamento;
CREATE TRIGGER StatusProcessoCruzamento
AFTER INSERT ON processo_cruzamento
FOR EACH ROW
EXECUTE PROCEDURE CriaStatusCruzamento();


-- Insere Status para processo de Doação --
CREATE OR REPLACE FUNCTION CriaStatusDoacao()
RETURNS TRIGGER AS $$
BEGIN
   INSERT INTO status_requisito_doacao VALUES (OLD.id_anuncio, 'Insira seu Título', OLD.email_candidasto, 'a verificar');
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS StatusProcessoDoacao ON processo_doacao;
CREATE TRIGGER StatusProcessoDoacao
AFTER INSERT ON processo_cruzamento
FOR EACH ROW
EXECUTE PROCEDURE CriaStatusDoacao();


-- Cria Avaliável para Anúncio --
CREATE OR REPLACE FUNCTION InsereAvaliavel()
RETURNS TRIGGER AS $$
DECLARE
   tipao TEXT;
BEGIN
   tipao = TG_ARGV[0];
   INSERT INTO avaliavel(tipo) VALUES (tipao) RETURNING id into NEW.id_avaliavel;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;
DROP TRIGGER IF EXISTS AvaliavelAnuncio ON anuncio;
CREATE TRIGGER AvaliavelAnuncio
BEFORE INSERT ON anuncio
FOR EACH ROW
EXECUTE PROCEDURE InsereAvaliavel('Anuncio');


-- Cria Avaliável para Servico --

DROP TRIGGER IF EXISTS AvaliavelServico ON servico;
CREATE TRIGGER AvaliavelServico
BEFORE INSERT ON servico
FOR EACH ROW
EXECUTE PROCEDURE InsereAvaliavel('Servico');


-- Cria Avaliável para Post --

DROP TRIGGER IF EXISTS AvaliavelPost ON post;
CREATE TRIGGER AvaliavelPost
BEFORE INSERT ON post
FOR EACH ROW
EXECUTE PROCEDURE InsereAvaliavel('Post');
