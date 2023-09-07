-- MySQL dump 10.19  Distrib 10.3.38-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: python2023
-- ------------------------------------------------------
-- Server version	10.3.38-MariaDB-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `status` enum('enable','disable') DEFAULT NULL,
  `deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'迫田','佑也','sakota@example.com','pass1234@','enable',0),(2,'ジョン','ドエ','john.doe@example.com','pass@321','disable',1),(3,'John','Doe','john.d1oe@example.com','secure_password','enable',1),(4,'テスト','テスト','test21@test.jp','pass@123','enable',1),(5,'テスト','テスト','test23@test.jp','pass@1234','enable',1),(6,'テスト２','テスト２','test2@test.jp','test@123','disable',1),(7,'テスト３','テスト３','test3@test.lp','test3@123','enable',0),(8,'test','test','test@test.com','test@123','enable',0),(9,'高橋','高橋','takahashinariaki@example.com','takahashinariaki@123','enable',0),(10,'佐藤','佐藤','isaosato@example.co.jp','isaosato@123','enable',0),(11,'山口','山口','yamaguchi_627@example.ne.jp','yamaguchi@123','disable',0),(12,'渡辺','渡辺','watanabe_kyouichi@example.jp','watanabe@123','disable',0),(13,'山下','山下','atsuhisayamashita@example.co.jp','atsuhisayamashita/123','enable',0),(14,'吉川','吉川','yoshikawaakira@example.co.jp','yoshikawaakira-123','enable',0),(15,'福田','福田','takashi_fukuda@example.jp','takashi_fukuda123','enable',0),(16,'鈴木','鈴木','shuuhei_suzuki@example.com','shuuhei_suzuki123','enable',0),(17,'諫山','諫山','isayama416@example.org','isayam_a416','enable',0),(18,'後藤','後藤','shunsukegoto@example.org','shunsukegoto@123','enable',0),(19,'吉武','吉武','masahiro_yoshitake@example.com','masahiro_yoshitake432','enable',0),(20,'井上','井上','hitoshi_inoue@example.ne.jp','hitoshi_inoue345','enable',0),(21,'高野','高野','hitoshitakano@example.ne.jp','hitoshitakano654','enable',0),(22,'加藤','行使','katoyasuko@example.com','passcord@345','enable',0),(23,'山野','山野','yamanokenichi@example.org','yamanokenichi324@^','enable',0),(24,'松尾','松尾','matsuo_219@example.ne.jp','matsuo_219','enable',0),(25,'櫻井','櫻井','sakurai_210@example.com','sakurai_210','enable',0),(26,'川島','川島','kawashimashinichi@example.net','kawashimashinich@45','enable',0),(27,'小池','小池','masayuki_koike@example.ne.jp','masayuki_koik43','enable',0),(28,'廣井','直樹','hiroinaoki@example.jp','hiroinaoki@*321','disable',1),(29,'臼井','康平','usui812@example.ne.jp','usui812/-12','enable',0),(30,'萱野','貴志','kayanotakashi@example.net','kayanotakashi','enable',0),(31,'梅木','亮介','ryousukeumeki@example.jp','ryousukeumek','enable',0),(32,'中沢','優美','nakazawayumi@example.jp','nakazawa','enable',0),(33,'横須賀','達郎','yokosuka_920@example.co.jp','yokosuka','enable',0),(34,'山田','壮太','yamda_souta@exsamplecom','password','enable',0),(35,'中島','聡','akira_nakajima@example.org','passcode','enable',0),(36,'川邊','絵里子','erikokawabe@example.ne.jp','erikokawabe','enable',0),(37,'磯貝','敬子','isogai116@example.jp','passcode','enable',0),(38,'中尾','学','manabusugisaki@example.net','pass12344@','enable',0),(39,'織田','信長','odanobunaga@example.com','odanobunaga3*','disable',1),(40,'豊臣','秀吉','toyoyomi@example.net','toyoyomi@23','enable',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-07 10:34:48
