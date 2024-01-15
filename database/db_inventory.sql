-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 15 Jan 2024 pada 17.16
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_inventory`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_items`
--

CREATE TABLE `tb_items` (
  `item_id` int(11) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `merk` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date_of_entry` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_items`
--

INSERT INTO `tb_items` (`item_id`, `name`, `merk`, `description`, `quantity`, `date_of_entry`) VALUES
(6, 'elektronik', 'usus', 'laptop usus', 3, '2024-01-15 12:59:44');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_transactions`
--

CREATE TABLE `tb_transactions` (
  `transaction_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `merk` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `date_of_entry` datetime NOT NULL,
  `date_of_return` datetime NOT NULL,
  `cost` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_transactions`
--

INSERT INTO `tb_transactions` (`transaction_id`, `name`, `merk`, `quantity`, `date_of_entry`, `date_of_return`, `cost`) VALUES
(2, 'name1', 'merk1', 1, '2024-01-14 16:25:04', '2024-01-18 16:25:20', 40000),
(3, 'name3', 'merk3', 4, '2024-01-14 16:46:50', '2024-01-19 17:07:45', 50000),
(4, 'motor', 'suzuki', 1, '2024-01-15 10:41:41', '2024-01-18 10:42:07', 30000),
(5, 'Elektronik', 'Samsul', 1, '2024-01-15 11:48:37', '2024-01-18 12:51:50', 30000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_items`
--
ALTER TABLE `tb_items`
  ADD PRIMARY KEY (`item_id`);

--
-- Indeks untuk tabel `tb_transactions`
--
ALTER TABLE `tb_transactions`
  ADD PRIMARY KEY (`transaction_id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tb_items`
--
ALTER TABLE `tb_items`
  MODIFY `item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `tb_transactions`
--
ALTER TABLE `tb_transactions`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
