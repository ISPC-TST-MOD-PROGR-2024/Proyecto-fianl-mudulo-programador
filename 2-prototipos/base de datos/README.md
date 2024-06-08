# Proyecto de Gestión de Máquinas y Actividades

## Descripción

Este proyecto gestiona información sobre máquinas, operarios, actividades, repuestos, consumibles, proveedores y almacenes. La base de datos está diseñada para llevar un control eficiente del mantenimiento y uso de las máquinas, así como de los recursos necesarios para su operación.

## Estructura de la Base de Datos

## Tablas ↓

### Maquina

| Columna          | Tipo        | Descripción                               |
| ---------------- | ----------- | ----------------------------------------- |
| id_Maquina       | INT         | Identificador único de la máquina (PK)    |
| Tipo_maquina     | VARCHAR(45) | Tipo de la máquina                        |
| Nombre           | VARCHAR(45) | Nombre de la máquina                      |
| Chasis           | VARCHAR(45) | Número de chasis de la máquina            |
| Motor            | VARCHAR(45) | Tipo o número de motor de la máquina      |
| Modelo           | INT         | Modelo de la máquina                      |
| Horas_de_trabajo | INT         | Horas de trabajo acumuladas de la máquina |

### Operario

| Columna            | Tipo        | Descripción                            |
| ------------------ | ----------- | -------------------------------------- |
| idOperario         | INT         | Identificador único del operario (PK)  |
| nombre             | VARCHAR(45) | Nombre del operario                    |
| apellido           | VARCHAR(45) | Apellido del operario                  |
| categoria          | VARCHAR(45) | Categoría del operario                 |
| esExterno          | VARCHAR(45) | Indicador de si el operario es externo |
| Maquina_id_Maquina | INT         | FK referenciando `Maquina.id_Maquina`  |

### Actividad

| Columna              | Tipo        | Descripción                              |
| -------------------- | ----------- | ---------------------------------------- |
| id_Actividad         | INT         | Identificador único de la actividad (PK) |
| Tipo                 | VARCHAR(45) | Tipo de actividad                        |
| Descripcion          | VARCHAR(45) | Descripción de la actividad              |
| Lugar                | VARCHAR(45) | Lugar donde se realiza la actividad      |
| Limite_horas         | INT         | Límite de horas para la actividad        |
| Maquina_id_Maquina   | INT         | FK referenciando `Maquina.id_Maquina`    |
| Operario_id_Operario | INT         | FK referenciando `Operario.idOperario`   |

### Repuesto

| Columna                        | Tipo        | Descripción                               |
| ------------------------------ | ----------- | ----------------------------------------- |
| Descripcion                    | VARCHAR(45) | Descripción del repuesto                  |
| Marca                          | VARCHAR(45) | Marca del repuesto                        |
| Alternativo                    | VARCHAR(45) | Alternativa del repuesto                  |
| Proveedor_id_Proveedor         | INT         | FK referenciando `Proveedor.id_Proveedor` |
| Almacen_id_Almacen             | INT         | FK referenciando `Almacen.id_Almacen`     |
| Actividad_id_Actividad         | INT         | FK referenciando `Actividad.id_Actividad` |
| Actividad_Maquina_id_Maquina   | INT         | FK referenciando `Maquina.id_Maquina`     |
| Actividad_Operario_id_Operario | INT         | FK referenciando `Operario.idOperario`    |

### Consumible

| Columna                        | Tipo        | Descripción                               |
| ------------------------------ | ----------- | ----------------------------------------- |
| id_Consumible                  | INT         | Identificador único del consumible (PK)   |
| Descripcion                    | VARCHAR(45) | Descripción del consumible                |
| Marca                          | VARCHAR(45) | Marca del consumible                      |
| Alternativo                    | VARCHAR(45) | Alternativa del consumible                |
| Proveedor_id_Proveedor         | INT         | FK referenciando `Proveedor.id_Proveedor` |
| Almacen_id_Almacen             | INT         | FK referenciando `Almacen.id_Almacen`     |
| Actividad_id_Actividad         | INT         | FK referenciando `Actividad.id_Actividad` |
| Actividad_Maquina_id_Maquina   | INT         | FK referenciando `Maquina.id_Maquina`     |
| Actividad_Operario_id_Operario | INT         | FK referenciando `Operario.idOperario`    |

### Proveedor

| Columna      | Tipo        | Descripción                            |
| ------------ | ----------- | -------------------------------------- |
| id_Proveedor | INT         | Identificador único del proveedor (PK) |
| Nombre       | VARCHAR(45) | Nombre del proveedor                   |
| Direccion    | VARCHAR(45) | Dirección del proveedor                |
| Despacho     | VARCHAR(45) | Información de despacho del proveedor  |
| Pago         | VARCHAR(45) | Información de pago del proveedor      |

### Almacen

| Columna    | Tipo | Descripción                          |
| ---------- | ---- | ------------------------------------ |
| id_Almacen | INT  | Identificador único del almacén (PK) |
| stock      | INT  | Cantidad de stock en el almacén      |
| reserva    | INT  | Cantidad de reserva en el almacén    |

## Relaciones entre Tablas

- **Maquina**:

  - Se relaciona con `Operario` mediante `Maquina_id_Maquina`.
  - Se relaciona con `Actividad` mediante `Maquina_id_Maquina`.
  - Tiene una relación indirecta con `Repuesto` y `Consumible` a través de `Actividad`.

- **Operario**:

  - Se relaciona con `Maquina` mediante `Maquina_id_Maquina`.
  - Se relaciona con `Actividad` mediante `Operario_id_Operario`.
  - Tiene una relación indirecta con `Repuesto` y `Consumible` a través de `Actividad`.

- **Actividad**:

  - Se relaciona con `Maquina` mediante `Maquina_id_Maquina`.
  - Se relaciona con `Operario` mediante `Operario_id_Operario`.
  - Se relaciona con `Repuesto` y `Consumible` mediante `Actividad_id_Actividad`.

- **Repuesto**:

  - Se relaciona con `Proveedor` mediante `Proveedor_id_Proveedor`.
  - Se relaciona con `Almacen` mediante `Almacen_id_Almacen`.
  - Se relaciona con `Actividad` mediante `Actividad_id_Actividad`.

- **Consumible**:

  - Se relaciona con `Proveedor` mediante `Proveedor_id_Proveedor`.
  - Se relaciona con `Almacen` mediante `Almacen_id_Almacen`.
  - Se relaciona con `Actividad` mediante `Actividad_id_Actividad`.

- **Proveedor**:

  - Se relaciona con `Repuesto` y `Consumible` mediante `id_Proveedor`.

- **Almacen**:
  - Se relaciona con `Repuesto` y `Consumible` mediante `id_Almacen`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para contribuir a este proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
