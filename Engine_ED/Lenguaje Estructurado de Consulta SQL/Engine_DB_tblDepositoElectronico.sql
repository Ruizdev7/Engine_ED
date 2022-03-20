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
-- Table structure for table `tblDepositoElectronico`
--

DROP TABLE IF EXISTS `tblDepositoElectronico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblDepositoElectronico` (
  `depositoElectronico` bigint unsigned NOT NULL COMMENT '	',
  `codigoCuenta` bigint unsigned NOT NULL,
  `ccnCliente` int NOT NULL,
  `cuantiaMaxDeposito` decimal(15,2) unsigned NOT NULL,
  `claseTasaInteres` char(1) NOT NULL,
  `tasaInteres` float(5,2) NOT NULL,
  `frecLiqIntereses` char(1) NOT NULL,
  `tipoDeposito` varchar(5) NOT NULL,
  `saldoDeposito` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`depositoElectronico`),
  KEY `fk_tblDepositoElectronico_1_idx` (`codigoCuenta`),
  KEY `fk_tblDepositoElectronico_2_idx` (`ccnCliente`),
  KEY `fk_tblDepositoElectronico_3_idx` (`claseTasaInteres`),
  KEY `fk_tblDepositoElectronico_4_idx` (`tipoDeposito`),
  KEY `fk_tblDepositoElectronico_5_idx` (`frecLiqIntereses`),
  CONSTRAINT `fk_tblDepositoElectronico_1` FOREIGN KEY (`codigoCuenta`) REFERENCES `tblPUC` (`codigoCuenta`),
  CONSTRAINT `fk_tblDepositoElectronico_2` FOREIGN KEY (`ccnCliente`) REFERENCES `tblCliente` (`ccnCliente`),
  CONSTRAINT `fk_tblDepositoElectronico_3` FOREIGN KEY (`claseTasaInteres`) REFERENCES `tblClaseTasaInteres` (`claseTasaInteres`),
  CONSTRAINT `fk_tblDepositoElectronico_4` FOREIGN KEY (`tipoDeposito`) REFERENCES `tblTipoDeposito` (`idTipoDeposito`),
  CONSTRAINT `fk_tblDepositoElectronico_5` FOREIGN KEY (`frecLiqIntereses`) REFERENCES `tblFrecLiquidacion` (`idFrecuencia`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `FIDeposito` AFTER INSERT ON `tblDepositoElectronico` FOR EACH ROW insert into `Engine_DB`.`tblControlFechasDepositos`(`depositoElectronico`,`FI`)
values(new.depositoElectronico,now()) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-07 23:02:09
