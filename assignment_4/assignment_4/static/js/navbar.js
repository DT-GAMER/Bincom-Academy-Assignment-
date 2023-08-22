/* navbar.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize navigation menu interactions
  initNavigationMenu();
});

// Initialize navigation menu interactions
function initNavigationMenu() {
  const navToggleButton = document.querySelector('.nav-toggle-button');
  const navMenu = document.querySelector('.nav-menu');

  if (navToggleButton && navMenu) {
    navToggleButton.addEventListener('click', toggleNavMenu);
  }

  function toggleNavMenu() {
    navMenu.classList.toggle('active');
  }

  const navMenuItems = document.querySelectorAll('.nav-menu-item');
  navMenuItems.forEach(item => {
    item.addEventListener('click', closeNavMenu);
  });

}

// Function to close the navigation menu
function closeNavMenu() {
  const navMenu = document.querySelector('.nav-menu');
  navMenu.classList.remove('active');
}

