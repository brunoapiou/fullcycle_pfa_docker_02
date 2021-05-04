USE desafio;

CREATE TABLE tab_modulos (
    id integer not null auto_increment PRIMARY KEY,
    modulo varchar(255)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

insert into tab_modulos (modulo) values ('Fundamentos de Arquitetura de Software');
insert into tab_modulos (modulo) values ('Docker');
insert into tab_modulos (modulo) values ('Comunicação');
insert into tab_modulos (modulo) values ('RabbitMQ');
insert into tab_modulos (modulo) values ('Autenticação e Keycloak');
insert into tab_modulos (modulo) values ('Domain Driven Desgin e Arquitetura hexagonal');
insert into tab_modulos (modulo) values ('Arquitetura de projeto prático - Codeflix');
insert into tab_modulos (modulo) values ('Microserviço: Catálogo de vídeos com Laravel (Back-end)');
insert into tab_modulos (modulo) values ('Microserviço: Catálogo de vídeos com React (Forn-end)');
insert into tab_modulos (modulo) values ('Microserviço de Encoder de Vídeo com Go Lang');
insert into tab_modulos (modulo) values ('Microserviço - API do Catálogo com Node.JS (Back-end)');