-- database.sql - Setup database dan tabel

-- Buat database
CREATE DATABASE IF NOT EXISTS belajar_web;
USE belajar_web;

-- Buat tabel mahasiswa
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(20) NOT NULL UNIQUE,
    nama VARCHAR(100) NOT NULL,
    prodi VARCHAR(50) NOT NULL,
    semester INT NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data contoh
INSERT INTO mahasiswa (nim, nama, prodi, semester, email) VALUES
('2210631170', 'Andi Setiawan', 'Informatika', 4, 'andi@email.com'),
('2210631171', 'Budi Santoso', 'Sistem Informasi', 6, 'budi@email.com'),
('2210631172', 'Citra Dewi', 'Teknik Komputer', 2, 'citra@email.com');
