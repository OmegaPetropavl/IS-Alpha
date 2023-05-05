CREATE DATABASE  IF NOT EXISTS `arenda_nedvizhimosti` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `arenda_nedvizhimosti`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: arenda_nedvizhimosti
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `employer`
--

DROP TABLE IF EXISTS `employer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employer` (
  `Employer_ID` int NOT NULL AUTO_INCREMENT,
  `Lastname` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Middlename` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Job_Title` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Login` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Password` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`Employer_ID`),
  UNIQUE KEY `Employer_ID` (`Employer_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employer`
--

LOCK TABLES `employer` WRITE;
/*!40000 ALTER TABLE `employer` DISABLE KEYS */;
/*!40000 ALTER TABLE `employer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fizlitco`
--

DROP TABLE IF EXISTS `fizlitco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fizlitco` (
  `IIN_Arendatora` int NOT NULL AUTO_INCREMENT,
  `Lastname` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Middlename` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `Passport_data` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Adress` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Telephone` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`IIN_Arendatora`),
  UNIQUE KEY `IIN_Arendatora_UNIQUE` (`IIN_Arendatora`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fizlitco`
--

LOCK TABLES `fizlitco` WRITE;
/*!40000 ALTER TABLE `fizlitco` DISABLE KEYS */;
INSERT INTO `fizlitco` VALUES (1,'asdas','asdsa',NULL,'asdsa','asdsa','asdsa');
/*!40000 ALTER TABLE `fizlitco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pomeshenie`
--

DROP TABLE IF EXISTS `pomeshenie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pomeshenie` (
  `id_pomesheniya` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `adress` varchar(100) NOT NULL,
  `square` int NOT NULL,
  `Podval` tinyint NOT NULL,
  `podval_square` int DEFAULT NULL,
  `koefficient_podvala` float DEFAULT NULL,
  `koefficient_tech_obustroistva` float NOT NULL,
  PRIMARY KEY (`id_pomesheniya`),
  UNIQUE KEY `id_pomesheniya_UNIQUE` (`id_pomesheniya`),
  UNIQUE KEY `name_UNIQUE` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pomeshenie`
--

LOCK TABLES `pomeshenie` WRITE;
/*!40000 ALTER TABLE `pomeshenie` DISABLE KEYS */;
INSERT INTO `pomeshenie` VALUES (1,'iPhone X','iPhone X',1,1,NULL,NULL,0.7),(4,'iPhone','iPhone X',1,1,NULL,NULL,0.7);
/*!40000 ALTER TABLE `pomeshenie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urlitco`
--

DROP TABLE IF EXISTS `urlitco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urlitco` (
  `BIN_Arendatora` varchar(10) NOT NULL,
  `Comp_Name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `FIO` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Ur_Adress` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Telephone` varchar(12) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Licence_number` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `Licence_Date` date NOT NULL,
  PRIMARY KEY (`BIN_Arendatora`),
  UNIQUE KEY `BIN_Arendatora` (`BIN_Arendatora`),
  UNIQUE KEY `BIN_Arendatora_UNIQUE` (`BIN_Arendatora`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urlitco`
--

LOCK TABLES `urlitco` WRITE;
/*!40000 ALTER TABLE `urlitco` DISABLE KEYS */;
/*!40000 ALTER TABLE `urlitco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'arenda_nedvizhimosti'
--

--
-- Dumping routines for database 'arenda_nedvizhimosti'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-02  2:03:30
