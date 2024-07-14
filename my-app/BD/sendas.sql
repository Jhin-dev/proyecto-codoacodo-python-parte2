/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP TABLE IF EXISTS `tbl_sitios`;
CREATE TABLE `tbl_sitios` (
  `id_sitio` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_sitio` varchar(50) NOT NULL,
  `ciudad_sitio` varchar(50) NOT NULL,
  `provincia_sitio` varchar(50) NOT NULL,
  `descripcion_sitio` text NOT NULL,
  `foto_sitio` mediumtext NOT NULL,
  `fecha_registro` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_sitio`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_surname` varchar(100) NOT NULL,
  `email_user` varchar(50) NOT NULL,
  `pass_user` text NOT NULL,
  `created_user` timestamp NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `tbl_sitios` (`id_sitio`, `nombre_sitio`, `ciudad_sitio`, `provincia_sitio`, `descripcion_sitio`, `foto_sitio`, `fecha_registro`) VALUES
(8, 'Cataratas del Iguazú', 'Puerto Iguazú', 'Misiones', 'Impresionante conjunto de cataratas ubicado en la selva subtropical, declarado Patrimonio de la Humanidad por la UNESCO.', '66b8697b0bc8469aaceaa526f34c8efa4a046e18f4e64b9482f5162b935b7a4f.jpg', '2024-07-14 02:27:21');
INSERT INTO `tbl_sitios` (`id_sitio`, `nombre_sitio`, `ciudad_sitio`, `provincia_sitio`, `descripcion_sitio`, `foto_sitio`, `fecha_registro`) VALUES
(9, 'Glaciar Perito Moreno', 'Lago Argentino', 'Santa Cruz', 'Espectacular glaciar ubicado en el Parque Nacional Los Glaciares, uno de los pocos en el mundo que se encuentra en avance.', '4c76bc2c185a40b6a0de480a3d4eab78f5299f94c6464e3bbc1f1545034b6066.jpg', '2024-07-14 02:29:38');


INSERT INTO `users` (`id`, `name_surname`, `email_user`, `pass_user`, `created_user`) VALUES
(5, 'admin', 'admin@admin.com', 'pbkdf2:sha256:600000$Mfow2DjwBItcFlsy$170506a703e1d5032b76fde29ccc6ff25ef6f332488904113dce28e087c0b3c6', '2024-07-13 22:21:15');



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;