# Host: 127.0.0.1:2333  (Version 5.6.42-log)
# Date: 2020-03-28 19:34:44
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
  `time` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Data for table "game"
#

