-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: library_db
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `book_id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(100) DEFAULT NULL,
  `available` tinyint(1) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (16,'The Life Divine',1,'Philosophy'),(17,'The Alchemist',1,'Novel'),(18,'Da Vinci Code',1,'Thriller'),(19,'Head-First Python',1,'Programming'),(20,'Storytelling with Data',1,'Analytics');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `borrowed_books`
--

DROP TABLE IF EXISTS `borrowed_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrowed_books` (
  `borrow_id` int NOT NULL AUTO_INCREMENT,
  `book_id` int DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `borrow_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `return_date` date DEFAULT NULL,
  PRIMARY KEY (`borrow_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrowed_books`
--

LOCK TABLES `borrowed_books` WRITE;
/*!40000 ALTER TABLE `borrowed_books` DISABLE KEYS */;
INSERT INTO `borrowed_books` VALUES (13,2,'ram','2026-03-15','2026-03-22','2026-03-25'),(14,3,'sita','2026-03-16','2026-03-23','2026-03-22'),(15,4,'john','2026-03-17','2026-03-24',NULL),(16,5,'alex','2026-03-18','2026-03-25','2026-03-28'),(17,1,'kiran','2026-03-19','2026-03-26','2026-03-26'),(18,2,'meena','2026-03-20','2026-03-27',NULL),(19,3,'ram','2026-03-21','2026-03-28','2026-03-30'),(20,4,'sita','2026-03-22','2026-03-29','2026-03-29'),(21,5,'john','2026-03-23','2026-03-30',NULL),(22,1,'alex','2026-03-24','2026-03-31','2026-04-02'),(23,2,'kiran','2026-03-25','2026-04-01','2026-04-01'),(24,3,'meena','2026-03-26','2026-04-02',NULL),(25,4,'ram','2026-03-27','2026-04-03','2026-04-05'),(26,5,'sita','2026-03-28','2026-04-04','2026-04-03'),(27,1,'john','2026-03-29','2026-04-05',NULL),(28,2,'Naveen','2026-04-03','2026-04-10','2026-04-03');
/*!40000 ALTER TABLE `borrowed_books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-04-04 20:13:38
