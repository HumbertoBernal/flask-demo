drop proyecto_db; 

CREATE DATABASE proyecto_db;

USE proyecto_db;

CREATE TABLE usuario(
id int(5) NOT NULL primary key auto_increment,
nombre varchar(50) NOT NULL,
telefono varchar(50) NOT NULL,
email varchar(50) NOT NULL
)ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;

insert into usuario(nombre,telefono,email)
values('Jaime','999888777','jaime@abc.com');

CREATE TABLE producto (
id INT NOT NULL AUTO_INCREMENT,
codigo varchar(10) NOT NULL,
descripcion varchar(150),
precio int(8) not null,
stock varchar(15),
categoria varchar(100),
PRIMARY KEY (id)
);

insert into producto(codigo,descripcion,precio,stock,categoria)
values('A000000001','Objeto para decorar',100,5,'adorno');