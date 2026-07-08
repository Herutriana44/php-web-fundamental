# Bab 4: MySQL Advanced — Indexes, Transactions, Relationships, Performance

Setelah menguasai SQL dasar (CRUD), langkah berikutnya adalah optimasi performa, relasi tabel kompleks, dan transaksi atomik.

## 1. Indexes — Optimasi Query Performance

### Jenis-Jenis Index

```sql
-- PRIMARY KEY (default index, unique, not null)
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(100) UNIQUE,
    nama VARCHAR(100)
);

-- UNIQUE index (nilai harus unik)
CREATE UNIQUE INDEX idx_email ON users(email);

-- Regular index (mempercepat WHERE, JOIN, ORDER BY)
CREATE INDEX idx_nama ON users(nama);

-- FULLTEXT index (untuk full-text search)
CREATE FULLTEXT INDEX idx_deskripsi ON produk(deskripsi);

-- Composite index (multiple columns)
CREATE INDEX idx_user_date ON orders(user_id, created_at);
```

### Query Performance Analysis

```sql
-- EXPLAIN: lihat bagaimana query dieksekusi
EXPLAIN SELECT * FROM users WHERE email = 'test@example.com';

-- Output:
-- type: ALL (scan semua rows) = BURUK
-- type: ref (pakai index) = BAIK
-- rows: jumlah rows yang dipindai

-- ✗ BURUK: Tanpa index (table scan)
SELECT * FROM users WHERE nama LIKE '%Budi%';

-- ✓ BAIK: Pakai FULLTEXT index
SELECT * FROM users WHERE MATCH(nama) AGAINST('Budi');
```

### Index Best Practices
- Jangan create index untuk semua kolom (overhead pada INSERT/UPDATE)
- Index high-selectivity columns (email, id)
- Hindari index low-selectivity columns (gender, status)
- Monitor dan remove unused indexes
- Composite index: order matters (WHERE id=1 AND created_at>date)

## 2. Relasi & Foreign Keys

### One-to-Many Relationship

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama VARCHAR(100)
);

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    total DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Query dengan JOIN
SELECT u.nama, COUNT(o.id) as jumlah_order
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

### Many-to-Many Relationship (pakai junction table)

```sql
CREATE TABLE students (id INT PRIMARY KEY, nama VARCHAR(100));
CREATE TABLE courses (id INT PRIMARY KEY, nama VARCHAR(100));

-- Junction table
CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Query students & courses mereka
SELECT s.nama, GROUP_CONCAT(c.nama) as courses
FROM students s
JOIN student_courses sc ON s.id = sc.student_id
JOIN courses c ON sc.course_id = c.id
GROUP BY s.id;
```

### Foreign Key Constraints

```sql
-- ON DELETE CASCADE: hapus orders jika user dihapus
ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE CASCADE
ON UPDATE CASCADE;

-- ON DELETE SET NULL: set ke NULL jika parent dihapus
ALTER TABLE comments
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES users(id)
ON DELETE SET NULL;
```

## 3. Transactions

### ACID Properties
- **Atomicity**: semua atau tidak sama sekali
- **Consistency**: dari state valid ke state valid
- **Isolation**: concurrent transactions tidak interfere
- **Durability**: committed data persisten

### Transaction Syntax

```sql
START TRANSACTION;

-- Multiple operations
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- Jika error, ROLLBACK
-- Jika success, COMMIT
COMMIT;

-- Manual rollback
ROLLBACK;
```

### PHP PDO Transactions

```php
<?php
try {
    $pdo->beginTransaction();
    
    $stmt1 = $pdo->prepare("UPDATE accounts SET balance = balance - ? WHERE id = ?");
    $stmt1->execute([100, 1]);
    
    $stmt2 = $pdo->prepare("UPDATE accounts SET balance = balance + ? WHERE id = ?");
    $stmt2->execute([100, 2]);
    
    $pdo->commit();
} catch (Exception $e) {
    $pdo->rollBack();
    echo "Transaction failed: " . $e->getMessage();
}
?>
```

## 4. Normalization — Database Design

### Normal Forms (1NF, 2NF, 3NF)

```sql
-- ✗ BURUK: Non-normalized (repeating groups)
CREATE TABLE orders (
    id INT,
    customer_name VARCHAR(100),
    product1 VARCHAR(100),
    product2 VARCHAR(100),
    product3 VARCHAR(100)
);

-- ✓ BAIK: Normalized (3NF)
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

## 5. Backup & Recovery

```bash
# Backup database (dari CLI)
mysqldump -u root -p database_name > backup.sql

# Backup specific table
mysqldump -u root -p database_name table_name > backup.sql

# Restore dari backup
mysql -u root -p database_name < backup.sql
```

## 6. Query Optimization Tips

```sql
-- ✗ BURUK: Subquery di SELECT
SELECT id, nama, (SELECT COUNT(*) FROM orders WHERE user_id = users.id) as order_count
FROM users;

-- ✓ BAIK: Pakai JOIN & aggregation
SELECT u.id, u.nama, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;

-- ✗ BURUK: SELECT *
SELECT * FROM users;

-- ✓ BAIK: Select specific columns
SELECT id, nama, email FROM users;

-- Use LIMIT
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;
```

## 7. Locking & Concurrency

```sql
-- Pessimistic locking
START TRANSACTION;
SELECT * FROM accounts WHERE id = 1 FOR UPDATE;  -- Lock row
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
COMMIT;

-- Optimistic locking (pakai version number)
UPDATE accounts 
SET balance = balance - 100, version = version + 1
WHERE id = 1 AND version = 5;  -- Check version before update
```
