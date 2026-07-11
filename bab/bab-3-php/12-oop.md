# Bab 3: PHP Intermediate — OOP, Security, Debugging, Error Handling

Setelah menguasai PHP dasar, langkah berikutnya adalah Object-Oriented Programming (OOP), keamanan, debugging, dan error handling — skill essential untuk production code.

## 1. Object-Oriented Programming (OOP)

### Classes & Objects
```php
<?php
class Mobil {
    // Properties
    public $brand;
    public $warna;
    private $kecepatan = 0;  // private: hanya bisa diakses dari dalam class

    // Constructor (dipanggil otomatis saat new)
    public function __construct($brand, $warna) {
        $this->brand = $brand;
        $this->warna = $warna;
    }

    // Method
    public function akselerasi() {
        $this->kecepatan += 10;
    }

    public function getKecepatan() {
        return $this->kecepatan;
    }
}

// Membuat object
$mobil1 = new Mobil("Toyota", "Merah");
$mobil1->akselerasi();
echo $mobil1->getKecepatan();  // 10
?>
```

### Inheritance & Polymorphism
```php
<?php
class Kendaraan {
    protected $jumlahRoda;

    public function __construct($jumlahRoda) {
        $this->jumlahRoda = $jumlahRoda;
    }

    public function info() {
        return "Kendaraan dengan {$this->jumlahRoda} roda";
    }
}

class Mobil extends Kendaraan {
    private $brand;

    public function __construct($brand, $jumlahRoda = 4) {
        parent::__construct($jumlahRoda);
        $this->brand = $brand;
    }

    public function info() {
        return "Mobil {$this->brand} dengan {$this->jumlahRoda} roda";
    }
}

$mobil = new Mobil("Honda");
echo $mobil->info();  // Mobil Honda dengan 4 roda
?>
```

### Interfaces & Abstract Classes
```php
<?php
interface Berkendara {
    public function start();
    public function stop();
}

abstract class Kendaraan implements Berkendara {
    protected $engine = false;

    abstract public function getSpeed();

    public function start() {
        $this->engine = true;
        echo "Engine started";
    }

    public function stop() {
        $this->engine = false;
        echo "Engine stopped";
    }
}

class Mobil extends Kendaraan {
    private $speed = 0;

    public function getSpeed() {
        return $this->speed;
    }
}
?>
```

### Static Properties & Methods
```php
<?php
class Counter {
    private static $count = 0;

    public static function increment() {
        self::$count++;
    }

    public static function getCount() {
        return self::$count;
    }
}

Counter::increment();
Counter::increment();
echo Counter::getCount();  // 2
?>
```

## 2. Security Best Practices

### SQL Injection Prevention (Prepared Statements)
```php
<?php
// ✗ BURUK: Vulnerable to SQL injection
$nama = $_GET['nama'];
$query = "SELECT * FROM users WHERE nama = '$nama'";

// ✓ BAIK: Using prepared statements
$pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
$stmt = $pdo->prepare("SELECT * FROM users WHERE nama = ?");
$stmt->execute([$nama]);
$users = $stmt->fetchAll();
?>
```

### XSS (Cross-Site Scripting) Prevention
```php
<?php
// ✗ BURUK: User input langsung ditampilkan
echo "Halo, " . $_GET['name'];

// ✓ BAIK: Escape HTML output
echo "Halo, " . htmlspecialchars($_GET['name']);

// ✓ LEBIH BAIK: Whitelist input
$name = preg_match('/^[a-zA-Z\s]+$/', $_GET['name']) ? $_GET['name'] : 'Guest';
echo "Halo, " . htmlspecialchars($name);
?>
```

### CSRF (Cross-Site Request Forgery) Protection
```php
<?php
session_start();

// Generate token
if (empty($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

// Tambahkan ke form
echo '<input type="hidden" name="csrf_token" value="' . $_SESSION['csrf_token'] . '">';

// Verify sebelum process
if ($_POST['csrf_token'] !== $_SESSION['csrf_token']) {
    die("CSRF token validation failed");
}
?>
```

### Password Hashing
```php
<?php
// ✓ BAIK: Gunakan password_hash (built-in)
$password = "user_password";
$hashed = password_hash($password, PASSWORD_BCRYPT);

// Verify password
if (password_verify($password, $hashed)) {
    echo "Password correct";
}
?>
```

## 3. Error Handling

### Try-Catch-Finally
```php
<?php
try {
    $pdo = new PDO("mysql:host=localhost;dbname=test", "root", "");
    $stmt = $pdo->prepare("SELECT * FROM users WHERE id = ?");
    $stmt->execute([$_GET['id']]);
} catch (PDOException $e) {
    echo "Database error: " . $e->getMessage();
    // Log error securely (jangan expose ke user)
    error_log($e->getMessage());
} finally {
    // Always execute, cleanup resources
    $pdo = null;
}
?>
```

### Custom Exceptions
```php
<?php
class InsufficientBalanceException extends Exception {}

class BankAccount {
    private $balance = 1000;

    public function withdraw($amount) {
        if ($amount > $this->balance) {
            throw new InsufficientBalanceException("Balance tidak cukup");
        }
        $this->balance -= $amount;
    }
}

try {
    $account = new BankAccount();
    $account->withdraw(2000);
} catch (InsufficientBalanceException $e) {
    echo "Error: " . $e->getMessage();
}
?>
```

## 4. Debugging Techniques

### var_dump & print_r
```php
<?php
$user = ['name' => 'Budi', 'email' => 'budi@example.com'];
var_dump($user);   // Show detailed info + type
print_r($user);    // Show readable format
?>
```

### error_log
```php
<?php
// Log ke file (aman untuk production)
error_log("User login failed: " . $_GET['username'], 3, "/var/log/app.log");

// Log ke syslog atau email
error_log("Critical error: " . $e->getMessage(), 1, "admin@example.com");
?>
```

### xdebug (Advanced)
```php
<?php
// Butuh install xdebug extension
// Gunakan dengan IDE (VS Code, PhpStorm) untuk step-through debugging
// Set breakpoints di IDE, kode akan pause dan bisa inspect variables
?>
```

## 5. Best Practices

- Always validate & sanitize user input
- Use prepared statements untuk database queries
- Hash passwords dengan password_hash()
- Implement CSRF tokens
- Use HTTPS di production
- Log errors securely (jangan expose details ke user)
- Use type hints untuk function parameters
- Implement proper exception handling
- Keep sensitive data di environment variables (.env)
- Never commit credentials ke version control
