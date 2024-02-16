const inputDate = document.getElementById('fecha');

inputDate.addEventListener('input', () => {
  inputDate.classList.toggle('text-gray-400', inputDate.value === '');
});