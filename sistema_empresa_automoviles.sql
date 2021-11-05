-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-11-2021 a las 20:50:37
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_empresa_automoviles`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `cliente_cedula` int(11) NOT NULL,
  `cliente_tipo_cedula` varchar(10) NOT NULL,
  `cliente_nombre` varchar(30) NOT NULL,
  `cliente_apellido` varchar(30) NOT NULL,
  `cliente_calificacion_credito` int(10) NOT NULL,
  `cliente_direccion` varchar(100) NOT NULL,
  `cliente_telefono` varchar(14) NOT NULL,
  `cliente_fecha_nacimiento` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`cliente_cedula`, `cliente_tipo_cedula`, `cliente_nombre`, `cliente_apellido`, `cliente_calificacion_credito`, `cliente_direccion`, `cliente_telefono`, `cliente_fecha_nacimiento`) VALUES
(118790224, 'DIMEX', 'Andrei', 'Rivera', 80, 'Calle Arias', '+506 8310 0984', '2003-06-30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vendedores`
--

CREATE TABLE `vendedores` (
  `vendedores_civ` int(11) NOT NULL,
  `vendedores_nombre` varchar(30) NOT NULL,
  `vendedores_apellido` varchar(30) NOT NULL,
  `vendedores_fecha_nacimiento` date NOT NULL,
  `vendedores_tipo` varchar(30) NOT NULL,
  `vendedores_salario` int(11) NOT NULL,
  `vendedores_direccion` varchar(100) NOT NULL,
  `vendedores_telefono` varchar(14) NOT NULL,
  `vendedores_porcentaje_comision` float NOT NULL,
  `vendedores_monto_comision` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `vendedores`
--

INSERT INTO `vendedores` (`vendedores_civ`, `vendedores_nombre`, `vendedores_apellido`, `vendedores_fecha_nacimiento`, `vendedores_tipo`, `vendedores_salario`, `vendedores_direccion`, `vendedores_telefono`, `vendedores_porcentaje_comision`, `vendedores_monto_comision`) VALUES
(1000250, 'Pedro', 'Fernandez', '1994-11-08', 'Todo terrenos', 100000, 'Costa Rica', '+506 8888 1111', 5, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `ventas_cuv` int(11) NOT NULL,
  `ventas_codigo_consecutivo` int(11) NOT NULL,
  `ventas_contrato` varchar(30) NOT NULL,
  `ventas_civ` int(11) NOT NULL,
  `ventas_cedula` int(11) NOT NULL,
  `ventas_monto` int(11) NOT NULL,
  `ventas_fecha` date NOT NULL,
  `ventas_producto` varchar(100) NOT NULL,
  `ventas_marca` varchar(30) NOT NULL,
  `ventas_modelo` varchar(30) NOT NULL,
  `ventas_year` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`ventas_cuv`, `ventas_codigo_consecutivo`, `ventas_contrato`, `ventas_civ`, `ventas_cedula`, `ventas_monto`, `ventas_fecha`, `ventas_producto`, `ventas_marca`, `ventas_modelo`, `ventas_year`) VALUES
(1, 180001, 'CR-FTA-0008-20-1', 1000250, 118790224, 500000, '2021-11-10', 'Carro Sedan 4 puertas', 'Hyundai', 'Ascent', '2019');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_cedula`);

--
-- Indices de la tabla `vendedores`
--
ALTER TABLE `vendedores`
  ADD PRIMARY KEY (`vendedores_civ`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`ventas_cuv`),
  ADD KEY `civ` (`ventas_civ`),
  ADD KEY `cedula_cliente` (`ventas_cedula`),
  ADD KEY `cedulaCliente` (`ventas_cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `ventas_cuv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`ventas_civ`) REFERENCES `vendedores` (`vendedores_civ`),
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`ventas_cedula`) REFERENCES `clientes` (`cliente_cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
