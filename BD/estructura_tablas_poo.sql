CREATE TABLE preguntas (
    id_pregunta SERIAL PRIMARY KEY,
    enunciado_pregunta VARCHAR(255) NOT NULL,
    rta_a CHAR(1) NOT NULL,
    rta_b CHAR(1) NOT NULL,
    rta_c CHAR(1) NOT NULL,
    rta_d CHAR(1) NOT NULL,
    rta_correcta CHAR(1) NOT NULL,
    tipo_pregunta VARCHAR(100) NOT NULL,
    estado_pregunta BOOLEAN NOT NULL
);

CREATE TABLE temas (
    id_tema SERIAL PRIMARY KEY,
    nombre_tema VARCHAR(100) NOT NULL
);

CREATE TABLE jugador (
    id_usuario SERIAL PRIMARY KEY,
    nombre_usuario VARCHAR(100) NOT NULL,
    puntaje INTEGER NOT NULL,
    activo BOOLEAN NOT NULL
);