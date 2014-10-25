#Descripcion de la aplicación

Esta aplicación se creó con el fin de tener un acceso sencillo a la información
concerniente a programa Estatal para el que fue creado, así como también a su
manipulación y gestión.

Anteriormente se habia creado en PHP sin utilizar algún Framework, aunque había
querido hacerlo. Ahora es recreada en Python con Django.

La apliación almacena los siguientes datos:

 Información de escuelas, como su clave, nombre, ubicación y datos de contactos
 Personal, como maestros y directores, estudios y capacitación que ha recibido
 así como el apoyo económico que ha recibido por parte del programa.
 Capacitaciones que ha recibido la escuela
 Cantidad de alumnos que tiene cada escuela por grado y ciclo escolar

Los datos que debe arrojar una consulta completa son los siguientes:
    La escuela debe estar activa en ese ciclo escolar para mostrarse
    Se mostrarán todos los datos de la escuela
    Se muestra el personal que labora en dicha escuela, su puesto y el resto de
    datos regerentes a éste
    La cantidad de grupos y de alumnos por grado escolar en el actual ciclo o en
    el ciclo elegido (debe ser anterior al actual)
    Las capacitaciones que ha recibido la escuela por parte del programa y fecha
    en la que fue impartida
    Cantidad monetaria en cuanto apoyos económicos que ha recibido cada personal
    por parte del programa con la fecha en que fue entregado

