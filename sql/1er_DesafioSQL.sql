--1er Desafío SQL

SELECT
    fecha_renta,
    titulo,
    genero,
    cantidad_pagada,
    RANK() OVER(PARTITION BY genero ORDER BY cantidad_pagada
    DESC)
FROM pelicula
JOIN alquiler
ON alquiler.pelicula_id = pelicula.id;

/*
En la consulta SQL se estan seleccionando datos de una tabla (fecha_renta, titulo, genero, cantidad_pagada) 
para luego hacer una particion de los datos por genero (PARTITION BY), 
y luego por el dato de cantidad_pagada (ORDER BY) ordenarlos en forma descendiente (DESC).
A todo esto (OVER) se le asigna un rango (RANK) que empieza desde el 1 consecutivamente, a menos que el dato 
este repetido, en este caso le asigna el mismo numero salteandose el numero siguiente (ej: 1,1,3).
Estos datos se obtienen de la tabla peliculas (FROM) que esta conectada (JOIN) con alquiler mediante (ON)
el id de la pelicula.
*/


-- Diseño de la tabla
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nombre VARCHAR (50),
    apellido VARCHAR (50),
    mail VARCHAR (100),
);

--Agregar a la tabla alquiler el dato de id cliente como clave foranea
ALTER TABLE alquiler ADD id_cliente INT FOREIGN KEY;

--Nueva consulta con la incorporacion de estos nuevos datos y ordenados por nombre de pelicula y cliente
SELECT
    fecha_renta,
    titulo,
    genero,
    cantidad_pagada,
    nombre,
    apellido,
    mail,
RANK() OVER(PARTITION BY genero ORDER BY cantidad_pagada
DESC)
FROM pelicula
JOIN alquiler
ON alquiler.pelicula_id = pelicula.id;
JOIN clientes 
ON clientes.id = alquileres.id_cliente;
ORDER BY pelicula.titulo, clientes.nombre;

