# Host: 127.0.0.1:2333  (Version 5.6.42-log)
# Date: 2020-03-28 20:41:34
# Generator: MySQL-Front 6.1  (Build 1.26)


#
# Structure for table "game"
#

CREATE TABLE `game` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `room` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `op` varchar(255) DEFAULT NULL,
  `players` text,
  `mission` text,
  `record` text,
  `secret` text,
  `time` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "game"
#

INSERT INTO `game` VALUES (1,67,0,'one','{\'one\': [1, 0], \'two\': [2, 0]}',NULL,'','',1585397369);
