-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: lab4
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `backups`
--

DROP TABLE IF EXISTS `backups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backups` (
  `backups_num` int NOT NULL,
  `backups_date` date DEFAULT NULL,
  `backups_versional` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`backups_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backups`
--

LOCK TABLES `backups` WRITE;
/*!40000 ALTER TABLE `backups` DISABLE KEYS */;
INSERT INTO `backups` VALUES (1,'2019-10-20','49856.45646.35'),(2,'2019-10-20','49856.45646.3');
/*!40000 ALTER TABLE `backups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `division`
--

DROP TABLE IF EXISTS `division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `division` (
  `Division_num` int NOT NULL AUTO_INCREMENT,
  `Division_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Division_num`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `division`
--

LOCK TABLES `division` WRITE;
/*!40000 ALTER TABLE `division` DISABLE KEYS */;
INSERT INTO `division` VALUES (1,'dfhndjkgb'),(2,'hdfhdfhdfgfdhdfhd');
/*!40000 ALTER TABLE `division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `document`
--

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `document` (
  `document_num` int NOT NULL AUTO_INCREMENT,
  `document_date_of_transfer` date DEFAULT NULL,
  `technics_technics_inventory_num` int NOT NULL,
  `technics_Division_Division_num` int NOT NULL,
  `technics_repair_technics_repair_num` int NOT NULL,
  PRIMARY KEY (`document_num`,`technics_technics_inventory_num`,`technics_Division_Division_num`,`technics_repair_technics_repair_num`),
  KEY `fk_document_technics1_idx` (`technics_technics_inventory_num`,`technics_Division_Division_num`),
  KEY `fk_document_technics_repair1_idx` (`technics_repair_technics_repair_num`),
  CONSTRAINT `fk_document_technics1` FOREIGN KEY (`technics_technics_inventory_num`, `technics_Division_Division_num`) REFERENCES `technics` (`technics_inventory_num`, `division_division_num`),
  CONSTRAINT `fk_document_technics_repair1` FOREIGN KEY (`technics_repair_technics_repair_num`) REFERENCES `technics_repair` (`technics_repair_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice`
--

DROP TABLE IF EXISTS `invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice` (
  `invoice_num` int NOT NULL AUTO_INCREMENT,
  `invoice_price_componentParrt` double DEFAULT NULL,
  `invoice_list_of_required_spare_parts` varchar(45) DEFAULT NULL,
  `technics_technics_inventory_num` int NOT NULL,
  `technics_Division_Division_num` int NOT NULL,
  PRIMARY KEY (`invoice_num`,`technics_technics_inventory_num`,`technics_Division_Division_num`),
  KEY `fk_invoice_technics1_idx` (`technics_technics_inventory_num`,`technics_Division_Division_num`),
  CONSTRAINT `fk_invoice_technics1` FOREIGN KEY (`technics_technics_inventory_num`, `technics_Division_Division_num`) REFERENCES `technics` (`technics_inventory_num`, `division_division_num`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice`
--

LOCK TABLES `invoice` WRITE;
/*!40000 ALTER TABLE `invoice` DISABLE KEYS */;
INSERT INTO `invoice` VALUES (1,3543,'dhhddfh',1,1),(2,3522523,'dhhddfh',1,1);
/*!40000 ALTER TABLE `invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technics`
--

DROP TABLE IF EXISTS `technics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technics` (
  `technics_inventory_num` int NOT NULL AUTO_INCREMENT,
  `technics_name` varchar(45) DEFAULT NULL,
  `technics_model` varchar(45) DEFAULT NULL,
  `technics_year_of_release` date DEFAULT NULL,
  `Division_Division_num` int NOT NULL,
  PRIMARY KEY (`technics_inventory_num`,`Division_Division_num`),
  KEY `fk_technics_Division_idx` (`Division_Division_num`),
  CONSTRAINT `fk_technics_Division` FOREIGN KEY (`Division_Division_num`) REFERENCES `division` (`division_num`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technics`
--

LOCK TABLES `technics` WRITE;
/*!40000 ALTER TABLE `technics` DISABLE KEYS */;
INSERT INTO `technics` VALUES (1,'dfhdhf','dfhdfh','2019-10-10',1),(2,'dfh','dhhdf','2019-10-11',1);
/*!40000 ALTER TABLE `technics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `technics_repair`
--

DROP TABLE IF EXISTS `technics_repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `technics_repair` (
  `technics_repair_num` int NOT NULL,
  `Date_of_delivery_for_repair` date DEFAULT NULL,
  `Repair_period` varchar(45) DEFAULT NULL,
  `Type_of_repair` varchar(45) DEFAULT NULL,
  `Date_of_transfer` date DEFAULT NULL,
  `FIO_Employee_passed_repair` varchar(45) DEFAULT NULL,
  `Number__Employee_passed_repair` int DEFAULT NULL,
  `FIO_Employee_accepted_repair` varchar(45) DEFAULT NULL,
  `Number__Employee_accepted_repair` int DEFAULT NULL,
  `Position_of_repair_person` varchar(45) DEFAULT NULL,
  `technics_technics_inventory_num` int NOT NULL,
  `technics_Division_Division_num` int NOT NULL,
  PRIMARY KEY (`technics_repair_num`,`technics_technics_inventory_num`,`technics_Division_Division_num`),
  KEY `fk_technics_repair_technics1_idx` (`technics_technics_inventory_num`,`technics_Division_Division_num`),
  CONSTRAINT `fk_technics_repair_technics1` FOREIGN KEY (`technics_technics_inventory_num`, `technics_Division_Division_num`) REFERENCES `technics` (`technics_inventory_num`, `division_division_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `technics_repair`
--

LOCK TABLES `technics_repair` WRITE;
/*!40000 ALTER TABLE `technics_repair` DISABLE KEYS */;
INSERT INTO `technics_repair` VALUES (1,'2019-10-10','dbdbf','dbfdbdf','2019-11-11','dbdffb',134,'dfbdfbdf',1234,'sggsgs',1,1),(2,'2019-10-10','dfhfdh','fdhfhd','2019-10-11','dhfdhdf',145,'fdhfd',214,'hdfh',1,1);
/*!40000 ALTER TABLE `technics_repair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_post` varchar(45) DEFAULT NULL,
  `user_date_start_work` date DEFAULT NULL,
  `user_date_end_work` date DEFAULT NULL,
  `user_FIO` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  `user_login` varchar(45) DEFAULT NULL,
  `Division_Division_num` int NOT NULL,
  PRIMARY KEY (`user_id`,`Division_Division_num`),
  KEY `fk_user_Division1_idx` (`Division_Division_num`),
  CONSTRAINT `fk_user_Division1` FOREIGN KEY (`Division_Division_num`) REFERENCES `division` (`division_num`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'fghfghf','2019-10-10','2019-10-10','fgfjghjkg','fghfg','dhghrgt',1),(2,'fghfghf','2019-10-10','2019-10-10','fgfjghjkg','fghfg','dhghrgt',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'lab4'
--

--
-- Dumping routines for database 'lab4'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-29  6:22:26
