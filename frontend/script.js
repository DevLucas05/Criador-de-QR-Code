const generateBtn = document.getElementById("generateBtn");
const preview = document.getElementById("preview");
const sizeSlider = document.getElementById("size");
const sizeValue = document.getElementById("size_value");

sizeSlider.addEventListener("input", () => {
  sizeValue.textContent = `${sizeSlider.value}px`;
});

generateBtn.addEventListener("click", async () => {
  const content = document.getElementById("content").value;
  const fill_color = document.getElementById("fill_color").value;
  const back_color = document.getElementById("back_color").value;
  const size = sizeSlider.value;

  const response = await fetch("http://127.0.0.1:5000/generate_qr", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content, fill_color, back_color, size })
  });

  if (response.ok) {
    const blob = await response.blob();
    const imgUrl = URL.createObjectURL(blob);
    preview.innerHTML = `<img src="${imgUrl}" class="w-64 h-64 rounded shadow">`;
  } else {
    preview.textContent = "Erro ao gerar QR Code";
  }
});
