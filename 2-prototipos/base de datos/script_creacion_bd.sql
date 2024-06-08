-- MySQL Workbench Synchronization
-- Generated: 2024-06-08 10:51
-- Model: FlotaDB
-- Version: 1.0
-- Project: Control_de_Flota_mod_PROGRAMADOR
-- Author: FERNANDO

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `mydb`.`Maquina` (
  `id_Maquina` INT(11) NOT NULL AUTO_INCREMENT,
  `Tipo_maquina` VARCHAR(45) NOT NULL DEFAULT 'generic',
  `Nombre` VARCHAR(45) NOT NULL,
  `Chasis` VARCHAR(45) NULL DEFAULT NULL,
  `Motor` VARCHAR(45) NULL DEFAULT NULL,
  `Modelo` INT(11) NULL DEFAULT NULL,
  `Horas_de_trabajo` INT(11) NOT NULL,
  PRIMARY KEY (`id_Maquina`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Operario` (
  `idOperario` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `categoria` VARCHAR(45) NULL DEFAULT NULL,
  `esExterno` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idOperario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Actividad` (
  `id_Actividad` INT(11) NOT NULL AUTO_INCREMENT,
  `Tipo` VARCHAR(45) NULL DEFAULT NULL,
  `Descripcion` VARCHAR(60) NULL DEFAULT NULL,
  `Lugar` VARCHAR(45) NULL DEFAULT NULL,
  `Limite_horas` INT(11) NULL DEFAULT NULL,
  `Maquina_id_Maquina` INT(11) NOT NULL,
  `Operario_idOperario` INT(11) NOT NULL,
  PRIMARY KEY (`id_Actividad`),
  INDEX `fk_Actividad_Maquina1_idx` (`Maquina_id_Maquina` ASC) VISIBLE,
  INDEX `fk_Actividad_Operario1_idx` (`Operario_idOperario` ASC) VISIBLE,
  CONSTRAINT `fk_Actividad_Maquina1`
    FOREIGN KEY (`Maquina_id_Maquina`)
    REFERENCES `mydb`.`Maquina` (`id_Maquina`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Actividad_Operario1`
    FOREIGN KEY (`Operario_idOperario`)
    REFERENCES `mydb`.`Operario` (`idOperario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Repuesto` (
  `id_Repuesto` INT(11) NOT NULL AUTO_INCREMENT,
  `Descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `Marca` VARCHAR(45) NULL DEFAULT NULL,
  `Alternativo` VARCHAR(45) NULL DEFAULT NULL,
  `Actividad_id_Actividad` INT(11) NOT NULL,
  `Proveedor_id_Proveedor` INT(11) NOT NULL,
  `Almacen_id_Almacen` INT(11) NOT NULL,
  INDEX `fk_Repuesto_Actividad1_idx` (`Actividad_id_Actividad` ASC) VISIBLE,
  INDEX `fk_Repuesto_Proveedor1_idx` (`Proveedor_id_Proveedor` ASC) VISIBLE,
  INDEX `fk_Repuesto_Almacen1_idx` (`Almacen_id_Almacen` ASC) VISIBLE,
  PRIMARY KEY (`id_Repuesto`),
  CONSTRAINT `fk_Repuesto_Actividad1`
    FOREIGN KEY (`Actividad_id_Actividad`)
    REFERENCES `mydb`.`Actividad` (`id_Actividad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Repuesto_Proveedor1`
    FOREIGN KEY (`Proveedor_id_Proveedor`)
    REFERENCES `mydb`.`Proveedor` (`id_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Repuesto_Almacen1`
    FOREIGN KEY (`Almacen_id_Almacen`)
    REFERENCES `mydb`.`Almacen` (`id_Almacen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Almacen` (
  `id_Almacen` INT(11) NOT NULL AUTO_INCREMENT,
  `stock` INT(11) NULL DEFAULT NULL,
  `reserva` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id_Almacen`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Consumible` (
  `id_Consumible` INT(11) NOT NULL AUTO_INCREMENT,
  `Descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `Marca` VARCHAR(45) NULL DEFAULT NULL,
  `Alternativo` VARCHAR(45) NULL DEFAULT NULL,
  `Proveedor_id_Proveedor` INT(11) NOT NULL,
  `Almacen_id_Almacen` INT(11) NOT NULL,
  `Actividad_id_Actividad` INT(11) NOT NULL,
  PRIMARY KEY (`id_Consumible`),
  INDEX `fk_Consumible_Proveedor1_idx` (`Proveedor_id_Proveedor` ASC) VISIBLE,
  INDEX `fk_Consumible_Almacen1_idx` (`Almacen_id_Almacen` ASC) VISIBLE,
  INDEX `fk_Consumible_Actividad1_idx` (`Actividad_id_Actividad` ASC) VISIBLE,
  CONSTRAINT `fk_Consumible_Proveedor1`
    FOREIGN KEY (`Proveedor_id_Proveedor`)
    REFERENCES `mydb`.`Proveedor` (`id_Proveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Consumible_Almacen1`
    FOREIGN KEY (`Almacen_id_Almacen`)
    REFERENCES `mydb`.`Almacen` (`id_Almacen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Consumible_Actividad1`
    FOREIGN KEY (`Actividad_id_Actividad`)
    REFERENCES `mydb`.`Actividad` (`id_Actividad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `mydb`.`Proveedor` (
  `id_Proveedor` INT(11) NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Direccion` VARCHAR(45) NULL DEFAULT NULL,
  `Despacho` VARCHAR(45) NULL DEFAULT NULL,
  `Pago` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_Proveedor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
