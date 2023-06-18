-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: criminal_dbms
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `add_admin`
--

DROP TABLE IF EXISTS `add_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `role` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_admin`
--

LOCK TABLES `add_admin` WRITE;
/*!40000 ALTER TABLE `add_admin` DISABLE KEYS */;
INSERT INTO `add_admin` VALUES (3,'naveen','naveen@gmail.com','9555652362','Admin','123456'),(4,'nikhil','nikhil@gmail.com','9886646445','Admin','1234'),(5,'simran','simranjeetsinghm010@gmail.com','8288077118','Admin','1234');
/*!40000 ALTER TABLE `add_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `add_area`
--

DROP TABLE IF EXISTS `add_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_area` (
  `name` varchar(255) NOT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `landmark` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_area`
--

LOCK TABLES `add_area` WRITE;
/*!40000 ALTER TABLE `add_area` DISABLE KEYS */;
INSERT INTO `add_area` VALUES ('hall bazar','amritsar','punjab','srdar pagri house');
/*!40000 ALTER TABLE `add_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `add_category`
--

DROP TABLE IF EXISTS `add_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_category` (
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_category`
--

LOCK TABLES `add_category` WRITE;
/*!40000 ALTER TABLE `add_category` DISABLE KEYS */;
INSERT INTO `add_category` VALUES ('admin','of criminal dbms');
/*!40000 ALTER TABLE `add_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `center`
--

DROP TABLE IF EXISTS `center`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `center` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `a_idx` (`area`),
  KEY `B_idx` (`location`),
  CONSTRAINT `center1ertyuiop` FOREIGN KEY (`area`) REFERENCES `add_area` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `center2wserdftgyhujk` FOREIGN KEY (`location`) REFERENCES `surveilance_location` (`name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `center`
--

LOCK TABLES `center` WRITE;
/*!40000 ALTER TABLE `center` DISABLE KEYS */;
INSERT INTO `center` VALUES (1,'center1','simranjeetsinghm010@gmail.com','8288077118','123456',NULL,NULL),(2,'center2','simranjeetsinghm010@gmail.com','8288077118','123456','hall bazar','location');
/*!40000 ALTER TABLE `center` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `criminal_remarks`
--

DROP TABLE IF EXISTS `criminal_remarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criminal_remarks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `criminal_id` int DEFAULT NULL,
  `center_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `center1_idx` (`center_id`),
  KEY `criminal1_idx` (`criminal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criminal_remarks`
--

LOCK TABLES `criminal_remarks` WRITE;
/*!40000 ALTER TABLE `criminal_remarks` DISABLE KEYS */;
INSERT INTO `criminal_remarks` VALUES (6,12,1,'2023-05-09','14:31:09','lnkjbjjh;'),(7,11,1,'2023-05-11','10:12:17','i am simranjeet'),(8,11,1,'2023-05-11','12:47:46','status updated'),(9,11,1,'2023-05-11','12:54:47','submmitted'),(10,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(11,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(12,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(13,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(14,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(15,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(16,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(17,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(18,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(19,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(20,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(21,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(22,11,1,'2023-05-11','13:26:44','send mail at simranjeetsinghm010@gmail.com'),(23,11,1,'2023-05-11','13:32:22',''),(24,11,1,'2023-05-11','13:32:22',''),(25,11,1,'2023-05-11','13:34:30',''),(26,11,1,'2023-05-11','13:34:30',''),(27,11,1,'2023-05-11','13:34:30',''),(28,11,1,'2023-05-11','13:34:30',''),(29,11,1,'2023-05-11','13:34:30',''),(30,11,1,'2023-05-11','13:34:30',''),(31,11,1,'2023-05-11','13:34:30',''),(32,11,1,'2023-05-11','13:34:30',''),(33,11,1,'2023-05-12','14:48:50',''),(34,11,1,'2023-05-12','14:48:50',''),(35,11,1,'2023-05-12','14:52:58',''),(36,11,1,'2023-05-12','14:59:00',''),(37,11,1,'2023-05-12','15:12:35',''),(38,11,1,'2023-05-12','15:26:43',''),(39,11,1,'2023-05-13','10:22:55','empty'),(40,11,1,'2023-05-13','11:08:28','empty'),(41,11,1,'2023-05-13','11:08:28','empty'),(42,11,1,'2023-05-13','11:10:55','empty'),(43,11,1,'2023-05-13','11:24:35','empty'),(44,11,1,'2023-05-13','11:26:45','empty'),(45,11,1,'2023-05-13','11:27:53','empty'),(46,11,1,'2023-05-13','11:27:53','empty'),(47,11,1,'2023-05-13','11:29:44','empty'),(48,11,1,'2023-05-13','11:32:33','empty'),(49,11,1,'2023-05-13','11:34:02','empty'),(50,11,1,'2023-05-13','11:35:49','empty'),(51,11,1,'2023-05-13','11:38:58','empty'),(52,11,1,'2023-05-13','11:40:10','empty'),(53,11,1,'2023-05-13','11:48:58','empty'),(54,11,1,'2023-05-13','11:50:25','empty'),(55,11,1,'2023-05-13','11:52:02','empty'),(56,11,1,'2023-05-13','12:08:49','empty'),(57,11,1,'2023-05-13','12:11:01','empty'),(58,11,1,'2023-05-13','12:14:02','empty'),(59,11,1,'2023-05-13','12:23:30','add'),(60,11,1,'2023-05-13','12:24:59','add'),(61,11,1,'2023-05-13','12:35:25','add'),(62,11,1,'2023-05-13','12:37:53',''),(63,11,1,'2023-05-13','12:39:19','ad'),(64,11,1,'2023-05-13','12:52:28','ad'),(65,12,1,'2023-05-13','13:42:52','ad'),(66,12,1,'2023-05-13','13:45:32','ad'),(67,11,1,'2023-05-13','13:45:32','ad');
/*!40000 ALTER TABLE `criminal_remarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `criminals`
--

DROP TABLE IF EXISTS `criminals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criminals` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `father_name` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criminals`
--

LOCK TABLES `criminals` WRITE;
/*!40000 ALTER TABLE `criminals` DISABLE KEYS */;
INSERT INTO `criminals` VALUES (10,'a','b','9889972988','d','e','a_44430.jpeg'),(11,'simran','sakater singh','8288077118','simranjeetsinghm010@gmail.com','asr','simran_41766.jpeg'),(12,'naveen ','kumar','9987986986','kumarnaveen17205@gmail.com','asr','naveen _57217.jpeg');
/*!40000 ALTER TABLE `criminals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tittle` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `culprit_name` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
INSERT INTO `reports` VALUES (2,'report','report','2023-05-01','report','8977675767','report@gmail.com','report','image'),(3,'anything','dont know the actual crime','2023-05-01','vishwas','8765455785','vishwas@gmail.com','anything_87294.jpegvishwas colony, vishwas road, uttarpradesh',''),(4,'jhhccdhj','ekjbkkjcajjdc','2039-08-30','bbvuihhh','8967577776','bbjjiggiu@gmail.com','ggifyguliyygg','jhhccdhj_92667.jpeg'),(5,'Temp_title','abababababababababab','2001-03-23','abc','9090909090909090909090909','dasdasdas','asdasdasd','Temp_title_70476.jpegadsasdasdads');
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `surveilance_location`
--

DROP TABLE IF EXISTS `surveilance_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `surveilance_location` (
  `name` varchar(255) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `timings` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`name`),
  KEY `area_idx` (`area`),
  CONSTRAINT `area` FOREIGN KEY (`area`) REFERENCES `add_area` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `surveilance_location`
--

LOCK TABLES `surveilance_location` WRITE;
/*!40000 ALTER TABLE `surveilance_location` DISABLE KEYS */;
INSERT INTO `surveilance_location` VALUES ('location','location11','hall bazar','13:34');
/*!40000 ALTER TABLE `surveilance_location` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-15 15:38:37
