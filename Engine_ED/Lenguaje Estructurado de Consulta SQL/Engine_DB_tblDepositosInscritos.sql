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
-- Table structure for table `tblDepositosInscritos`
--

DROP TABLE IF EXISTS `tblDepositosInscritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblDepositosInscritos` (
  `ccnDepositosInscritos` bigint unsigned NOT NULL AUTO_INCREMENT,
  `filtroLista` varchar(50) NOT NULL,
  `tipoDeposito` varchar(5) NOT NULL,
  `depositoElectronico` bigint NOT NULL,
  `nombrePersonalizado` varchar(100) NOT NULL,
  `tipoId` char(2) NOT NULL,
  `numeroIdCliente` int NOT NULL,
  PRIMARY KEY (`ccnDepositosInscritos`),
  KEY `fk_tblDepositosInscritos_3_idx` (`tipoId`),
  KEY `fk_tblDepositosInscritos_1_idx` (`tipoDeposito`),
  KEY `fk_tblDepositosInscritos_5_idx` (`filtroLista`),
  CONSTRAINT `fk_tblDepositosInscritos_1` FOREIGN KEY (`tipoDeposito`) REFERENCES `tblTipoDeposito` (`idTipoDeposito`),
  CONSTRAINT `fk_tblDepositosInscritos_3` FOREIGN KEY (`tipoId`) REFERENCES `tblCliente` (`tipoId`),
  CONSTRAINT `fk_tblDepositosInscritos_5` FOREIGN KEY (`filtroLista`) REFERENCES `tblCliente` (`correoElectronicoCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-07 23:02:12
