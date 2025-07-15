const header = document.getElementById('header');
const toggleButton = document.getElementById('toggle_header');
toggleButton.addEventListener('click', function () {
  header.classList.toggle('hidden');
});
