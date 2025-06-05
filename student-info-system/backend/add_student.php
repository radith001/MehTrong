<?php
include 'db.php';

$data = json_decode(file_get_contents("php://input"), true);

$name = $data['name'];
$nim = $data['nim'];
$semester = $data['semester'];
$prodi = $data['prodi'];

$sql = "INSERT INTO students (name, nim, semester, prodi) VALUES (?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssis", $name, $nim, $semester, $prodi);

if ($stmt->execute()) {
    echo json_encode(["message" => "Data mahasiswa ditambahkan"]);
} else {
    http_response_code(500);
    echo json_encode(["message" => "Gagal menambahkan data"]);
}

$stmt->close();
$conn->close();
?>
