  
<center><img src="./assets/visuales/logo caratula.png" width="1200"></center>         

## Profesores:  
- Prof. Lisandro Lanfranco (Programacion)

- Prof. Martin Gerlero (Bases de Datos) 

- Prof. Pablo Figueroa (Etica y Deontologia Profesional)

## Alumnos:   

- Nicolás Nahuel Barrionuevo, GitHub: [@NicolasBa27](https://github.com/NicolasBa27).  

- Diego Ares, GitHub: [@diegote7](https://github.com/diegote7).  

- Fernando Gimenez Coria, GitHub: [@FernandoGC](https://github.com/FerCbr).  

- Raul Jara, GitHub: [@r-j28](https://github.com/r-j28).  


# **Proyecto final del Módulo Programador**  

<center><img src="./assets/visuales/logo pythonmysql.png" width="800"></center>  

## Objetivo  

Desarrollar una pequeña aplicación que demuestre la integración de conceptos de programación y bases de datos, y que aborde aspectos éticos y profesionales según la normativa vigente en la provincia de Córdoba.  

## Parte 1 - Integradora: Definición de la Temática  

## Consigna  

Elige una temática para tu aplicación que te resulte interesante y que te permita demostrar tus habilidades de programación y diseño de bases de datos. Escribe una breve descripción (máximo 150 palabras) de tu aplicación, asegurándote de que esta permita llevar a cabo las siguientes partes del proyecto.   
Para ello pueden reutilizar el desarrollo realizado en la evidencia de aprendizaje 2.  

## Parte 2 - Programación: Desarrollo de aplicación por consola en Python  

## Consigna  

Crea un programa en Python utilizando POO que presente un menú de opciones al usuario. Cada opción debe corresponder a una funcionalidad específica de tu aplicación. Cuando el usuario seleccione una opción de dicho menú, se debe invocar al método que ejecute las consultas sobre la BD.
**Ejemplo de Menú:**  
1. Registrar nuevo amigo
2. Registrar nuevo libro
3. Registrar préstamo de libro
4. Consultar libros prestados y no devueltos  

Para esto se deberá crear una clase que se encargue de la conexión y las operaciones con la base de datos MySQL.  

Implementa métodos en esta clase para mostrar el menú al usuario y permitir que elija una opción.  
Los métodos deben realizar las operaciones de insertar, consultar datos y consultas multi-tabla de acuerdo a la temática elegida.

El menú debe repetir el proceso hasta que el usuario decida salir del programa.  

## Parte 3 - Base de Datos: Diseño y Normalización  

## Consigna  

1. Diseña una base de datos sencilla relacionada con la temática de tu aplicación. La base de datos debe constar de al menos 3 tablas y estar correctamente normalizada hasta la tercera forma normal (3FN).   
Presenta el modelo relacional de la base de datos.
2. Crea la base de datos en un DBMS, se sugiere MySQL.
3. Escriba las consultas SQL que permiten interactuar con la base de datos ejecutando las funciones definidas en el menú de opciones.   
En las consultas se debe contemplar lo siguiente:  

a. Que exista al menos 1 consulta que permita insertar datos.  

b. Que exista al menos 1 consulta que permita obtener datos.  

c. Que exista al menos 1 consulta multitabla.  

Las consultas realizadas deben tener coherencia con la situación problemática, por ejemplo mostrar los datos ordenados de modo que tenga sentido, o utilizar funciones de agregación si es necesario (si tiene sentido para nuestro enunciado por ejemplo mostrar precios con y sin iva, podemos usar funciones de agregación para agregar ese valor directamente desde la consulta SQL y no dejar que el usuario deba
calcular el costo).  

## Parte 4 - Aspectos Éticos y Profesionales  

## Consigna  

Investiga y reflexiona sobre la ética profesional y el ejercicio profesional de las ciencias informáticas en la provincia de Córdoba, basándote en la Ley 7642 y el Estatuto de Regulación del Consejo Profesional de Ciencias Informáticas de Córdoba. Redacta un informe breve (máximo 300 palabras) donde describas la importancia de estos aspectos en el desarrollo de tu proyecto.  

**Puntos a cubrir:**  

La importancia de la ética profesional en el desarrollo de software.  

Cómo se aplican los principios de la Ley 7642 en tu proyecto.  

Reflexiones sobre el Estatuto de Regulación del Consejo Profesional de Ciencias Informáticas de Córdoba y su relevancia para tu práctica profesional.  

## Pautas de grupo y entregable  

El presente trabajo práctico final integrador, se plantea para realizarse en grupo de hasta 4 alumnos. Una vez confeccionado se debe entregar un archivo en PDF que contenga lo siguiente:  

1. Código fuente en Python que incluya la temática seleccionada a desarrollar, con las respectivas consultas a la base de datos.  

2. Modelo relacional normalizado en 3 FN  

3. Consultas SQL.  

4. Informé de aspectos éticos y profesionales  

Se deberá entregar una ficha informativa que incluya:  

● Título del proyecto  

● Nombres completos de los integrantes del grupo  

● Fecha de entrega  

● Relato de problemática planteada (máximo 200 palabras)  

Extensión: El informe final deberá tener una extensión de entre 10 y 20 páginas, escritas en letra Arial 12, a doble espacio, con márgenes de 2,5 cm.  

Formato: El proyecto deberá presentarse en formato digital (PDF).  

Plazo máximo de entrega: 10 de Junio de 2024  

Cada grupo deberá presentar su proyecto ante los docentes del módulo. La defensa oral tendrá una duración de 15 minutos por grupo y se evaluará la capacidad de los integrantes para explicar y defender su trabajo de manera clara y concisa.   
Los integrantes del grupo deberán exponer de manera conjunta, distribuyendo el tiempo de manera equitativa.
Se evaluará la presentación y funcionamiento del proyecto, la capacidad de respuesta a las preguntas y la defensa general del trabajo.  


# Organizacion de la estructura del repositorio

El proyecto sera almacenado en un repositorio en GitHub segun la siguiente estructura de carpetas:


1-requisitos: aqui se guarda la consigna del proyecto

2-investigación: aqui se guarda toda la documemtación recolectada para el desarrollo del proyecto

3-prototipos: Aqui se guarda el programa en python, la base de datos, y los documentos entregables.

4-presentacion: Aqui se guarda el informe final del proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia Creative Commons Atribución-NoComercial (CC BY-NC). Esta licencia permite que otros remixen, adapten y construyan sobre el trabajo de forma no comercial y, aunque sus nuevos trabajos deben también reconocer al autor original y ser no comerciales, no tienen que licenciar sus obras derivadas en los mismos términos.

Esta licencia es adecuada para un uso educativo y de aprendizaje, permitiendo la libre distribución y utilización del material mientras se protege contra el uso comercial sin autorización previa. Para usos comerciales, es necesario contactar a los autores para obtener permiso.

Para obtener más información sobre esta licencia y ver una copia completa de sus términos, visite [Creative Commons Atribución-NoComercial (CC BY-NC)](https://creativecommons.org/licenses/by-nc/4.0/).


