document.getElementById('form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const form = e.target;
  const data = {
    name: form.name.value,
    nim: form.nim.value,
    semester: parseInt(form.semester.value),
    prodi: form.prodi.value
  };

  const res = await fetch('http://localhost/api/add_student.php', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });

  const result = await res.json();
  alert(result.message);
});
