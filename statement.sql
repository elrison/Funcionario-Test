CREATE DATABASE `projeto` /*!40100 DEFAULT CHARACTER SET latin1 */;

CREATE TABLE `funcionario` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `nasc` date DEFAULT NULL,
  `salario` varchar(30) DEFAULT NULL,
  `foto` varchar(30) DEFAULT NULL,
  `idsetor` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FKSETOR` (`idsetor`),
  CONSTRAINT `FKSETOR` FOREIGN KEY (`idsetor`) REFERENCES `setor` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

CREATE TABLE `setor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;