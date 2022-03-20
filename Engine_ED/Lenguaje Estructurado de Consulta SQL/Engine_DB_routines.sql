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
-- Temporary view structure for view `listaConvenios`
--

DROP TABLE IF EXISTS `listaConvenios`;
/*!50001 DROP VIEW IF EXISTS `listaConvenios`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `listaConvenios` AS SELECT 
 1 AS `codigoConvenio`,
 1 AS `nombreEmpresa`,
 1 AS `convenio`,
 1 AS `datoCaptura`,
 1 AS `modalidadConvenio`,
 1 AS `descripcionMunicipio`,
 1 AS `descripcionDepartamento`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `listaConvenios`
--

/*!50001 DROP VIEW IF EXISTS `listaConvenios`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `listaConvenios` AS select `tc`.`codigoConvenio` AS `codigoConvenio`,`tc`.`nombreEmpresa` AS `nombreEmpresa`,`tc`.`convenio` AS `convenio`,`tc`.`datoCaptura` AS `datoCaptura`,`tc`.`modalidadConvenio` AS `modalidadConvenio`,`tm`.`descripcionMunicipio` AS `descripcionMunicipio`,`td`.`descripcionDepartamento` AS `descripcionDepartamento` from ((`tblConvenios` `tc` join `tblMunicipio` `tm` on((`tc`.`idMunicipio` = `tm`.`idMunicipio`))) join `tblDepartamento` `td` on((`tc`.`idDepartamento` = `td`.`idDepartamento`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'Engine_DB'
--

--
-- Dumping routines for database 'Engine_DB'
--
/*!50003 DROP PROCEDURE IF EXISTS `spTransferencia` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spTransferencia`(in `depositoElectronicoOrigen` bigint(10), `depositoElectronicoDestino` bigint(10), `montoTransferencia` decimal(15,2))
BEGIN    
	update `Engine_DB`.`tblDepositoElectronico` set `saldoDeposito` = `saldoDeposito` - `montoTransferencia` where `depositoElectronico` = `depositoElectronicoOrigen`;
    update `Engine_DB`.`tblDepositoElectronico` set `saldoDeposito` = `saldoDeposito` + `montoTransferencia` where `depositoElectronico` = `depositoElectronicoDestino`;
END ;;
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

-- Dump completed on 2021-11-07 23:02:13
