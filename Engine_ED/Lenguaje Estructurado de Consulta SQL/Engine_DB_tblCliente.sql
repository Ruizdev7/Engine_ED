-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: Engine_DB
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblCliente`
--

DROP TABLE IF EXISTS `tblCliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblCliente` (
  `ccnCliente` int NOT NULL AUTO_INCREMENT,
  `numeroIdCliente` int unsigned NOT NULL,
  `tipoId` char(2) NOT NULL,
  `fechaExpIdCliente` date DEFAULT NULL,
  `lugarExpIdCliente` mediumint NOT NULL,
  `primerNombreCliente` varchar(12) NOT NULL,
  `segundoNombreCliente` varchar(12) DEFAULT NULL,
  `primerApellidoCliente` varchar(12) NOT NULL,
  `segundoApellidoCliente` varchar(12) DEFAULT NULL,
  `fechaNacimientoCliente` date NOT NULL,
  `idEstado` char(1) NOT NULL DEFAULT 'A',
  `idRoles` varchar(7) NOT NULL DEFAULT 'SHE-005',
  `direccionCliente` varchar(30) NOT NULL,
  `barrioCliente` varchar(20) NOT NULL,
  `idPais` char(2) NOT NULL,
  `idDepartamento` mediumint NOT NULL,
  `idMunicipio` mediumint NOT NULL,
  `celularCliente` bigint unsigned NOT NULL,
  `correoElectronicoCliente` varchar(50) NOT NULL,
  `contraseñaCliente` varchar(300) NOT NULL,
  PRIMARY KEY (`ccnCliente`),
  UNIQUE KEY `numeroIdCliente_UNIQUE` (`numeroIdCliente`),
  UNIQUE KEY `correoElectronicoCliente_UNIQUE` (`correoElectronicoCliente`),
  KEY `fk_tblCliente_1_idx` (`tipoId`),
  KEY `fk_tblCliente_2_idx` (`lugarExpIdCliente`),
  KEY `fk_tblCliente_3_idx` (`idEstado`),
  KEY `fk_tblCliente_4_idx` (`idRoles`),
  KEY `fk_tblCliente_5_idx` (`idPais`),
  KEY `fk_tblCliente_6_idx` (`idDepartamento`),
  KEY `fk_tblCliente_7_idx` (`idMunicipio`),
  CONSTRAINT `fk_tblCliente_1` FOREIGN KEY (`tipoId`) REFERENCES `tblTipoId` (`tipoId`),
  CONSTRAINT `fk_tblCliente_2` FOREIGN KEY (`lugarExpIdCliente`) REFERENCES `tblMunicipio` (`idMunicipio`),
  CONSTRAINT `fk_tblCliente_3` FOREIGN KEY (`idEstado`) REFERENCES `tblEstado` (`idEstado`),
  CONSTRAINT `fk_tblCliente_4` FOREIGN KEY (`idRoles`) REFERENCES `tblRoles` (`idRoles`),
  CONSTRAINT `fk_tblCliente_5` FOREIGN KEY (`idPais`) REFERENCES `tblPais` (`idPais`),
  CONSTRAINT `fk_tblCliente_6` FOREIGN KEY (`idDepartamento`) REFERENCES `tblDepartamento` (`idDepartamento`),
  CONSTRAINT `fk_tblCliente_7` FOREIGN KEY (`idMunicipio`) REFERENCES `tblMunicipio` (`idMunicipio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-07 23:02:09
