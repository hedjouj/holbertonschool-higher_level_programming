document.addEventListener('DOMContentLoaded', () => {
  const redHeaderButton = document.querySelector('#red_header');
  const header = document.querySelector('header');
  redHeaderButton.addEventListener('click', () => {
    header.style.color = 'red';
  });
});
