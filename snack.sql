-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: snack
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `상품명` text,
  `재료` text,
  `수량` int DEFAULT NULL,
  `단위` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('김밥','우엉',30,'g'),('김밥','오이',50,'g'),('김밥','계란',1,'개'),('김밥','햄',30,'g'),('김밥','당근',40,'g'),('김밥','어묵',1,'장'),('김밥','맛살',50,'g'),('김밥','단무지',30,'g'),('김밥','김',1,'장'),('참치김밥','우엉',30,'g'),('참치김밥','오이',50,'g'),('참치김밥','계란',1,'개'),('참치김밥','햄',30,'g'),('참치김밥','당근',40,'g'),('참치김밥','어묵',1,'장'),('참치김밥','맛살',50,'g'),('참치김밥','단무지',30,'g'),('참치김밥','참치',50,'g'),('참치김밥','김',1,'장'),('치즈김밥','우엉',30,'g'),('치즈김밥','오이',50,'g'),('치즈김밥','계란',1,'개'),('치즈김밥','햄',30,'g'),('치즈김밥','당근',40,'g'),('치즈김밥','어묵',1,'장'),('치즈김밥','맛살',50,'g'),('치즈김밥','단무지',30,'g'),('치즈김밥','치즈',1,'장'),('치즈김밥','김',1,'장'),('떡볶이','떡',800,'g'),('떡볶이','대파',100,'g'),('떡볶이','설탕',40,'g'),('떡볶이','간장',16,'g'),('떡볶이','고추장',80,'g'),('떡볶이','고추가루',80,'g'),('떡볶이','어묵',2,'장'),('라볶이','떡',800,'g'),('라볶이','대파',100,'g'),('라볶이','설탕',40,'g'),('라볶이','간장',16,'g'),('라볶이','고추장',80,'g'),('라볶이','고추가루',80,'g'),('라볶이','라면사리',2,'개'),('라볶이','어묵',2,'장'),('치즈떡볶이','떡',800,'g'),('치즈떡볶이','대파',100,'g'),('치즈떡볶이','설탕',40,'g'),('치즈떡볶이','간장',16,'g'),('치즈떡볶이','고추장',80,'g'),('치즈떡볶이','고추가루',80,'g'),('치즈떡볶이','치즈',2,'개'),('치즈떡볶이','어묵',2,'장'),('돼지김치찌개','돼지고기',300,'g'),('돼지김치찌개','설탕',10,'g'),('돼지김치찌개','간장',12,'g'),('돼지김치찌개','대파',50,'g'),('돼지김치찌개','청양고추',15,'g'),('돼지김치찌개','새우젓',10,'g'),('돼지김치찌개','김치',800,'g'),('돼지김치찌개','고추가루',30,'g'),('돼지김치찌개','양파',150,'g'),('돼지김치찌개','다진마늘',4,'g'),('돼지김치찌개','들기름',8,'g'),('돼지김치찌개','된장',20,'g'),('참치김치찌개','설탕',20,'g'),('참치김치찌개','간장',24,'g'),('참치김치찌개','대파',100,'g'),('참치김치찌개','청양고추',30,'g'),('참치김치찌개','새우젓',20,'g'),('참치김치찌개','김치',1600,'g'),('참치김치찌개','고추가루',60,'g'),('참치김치찌개','양파',300,'g'),('참치김치찌개','다진마늘',8,'g'),('참치김치찌개','들기름',16,'g'),('참치김치찌개','된장',40,'g'),('참치김치찌개','참치',100,'g');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `finance`
--

DROP TABLE IF EXISTS `finance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `finance` (
  `주문번호` text,
  `내역` text,
  `수입` int DEFAULT NULL,
  `지출` bigint DEFAULT NULL,
  `잔액` int DEFAULT NULL,
  `시간` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finance`
--

LOCK TABLES `finance` WRITE;
/*!40000 ALTER TABLE `finance` DISABLE KEYS */;
/*!40000 ALTER TABLE `finance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `재료` text,
  `수량` int DEFAULT NULL,
  `단가` int DEFAULT NULL,
  `구매량` int DEFAULT NULL,
  `단위` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('간장',0,2500,1800,'g'),('계란',0,6780,30,'개'),('고추가루',0,11000,1000,'g'),('고추장',0,26500,14000,'g'),('김치',0,12300,10000,'g'),('다진마늘',0,2300,1000,'g'),('단무지',0,2170,500,'g'),('당근',0,17910,3000,'g'),('대파',0,6400,2000,'g'),('돼지고기',0,25140,3000,'g'),('된장',0,26490,14000,'g'),('들기름',0,22000,1800,'g'),('떡',0,14400,8000,'g'),('라면사리',0,12400,48,'개'),('맛살',0,17910,2000,'g'),('새우젓',0,23000,2200,'ml'),('설탕',0,3950,3000,'g'),('양파',0,11900,5000,'g'),('어묵',0,26740,24,'장'),('오이',0,18500,2000,'g'),('우엉',0,8440,1000,'g'),('참치',0,31900,1880,'g'),('청양고추',0,6900,1000,'g'),('치즈',0,21690,100,'장'),('햄',0,5700,1000,'g'),('김',0,8000,100,'장');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `상품` text,
  `단가` int DEFAULT NULL,
  `단위` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES ('김밥',7500,'개'),('참치김밥',8200,'개'),('치즈김밥',9900,'개'),('떡복이',6500,'개'),('라볶이',7300,'개'),('치즈떡복이',7100,'개'),('돼지김치찌개',16600,'개'),('참치김치찌개',11600,'개');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `주문번호` text,
  `아이디` text,
  `문의내용` text,
  `문의시간` text,
  `답변` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request`
--

DROP TABLE IF EXISTS `request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request` (
  `주문번호` text,
  `아이디` text,
  `상품명` text,
  `수량` text,
  `금액` text,
  `시간` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request`
--

LOCK TABLES `request` WRITE;
/*!40000 ALTER TABLE `request` DISABLE KEYS */;
/*!40000 ALTER TABLE `request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `아이디` text,
  `비밀번호` text,
  `이름` text,
  `주소` text,
  `전화번호` text,
  `사업자 여부` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-17 10:51:37
