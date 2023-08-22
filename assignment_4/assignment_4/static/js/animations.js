/* animations.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize animations and transitions
  initAnimations();
});

// Initialize animations and transitions
function initAnimations() {
  // Add event listeners for animations
  const animateElements = document.querySelectorAll('.animate');
  animateElements.forEach(element => {
    element.addEventListener('mouseenter', startAnimation);
    element.addEventListener('animationend', resetAnimation);
  });

  const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
  smoothScrollLinks.forEach(link => {
    link.addEventListener('click', smoothScroll);
  });
}

// Function to start an animation
function startAnimation(event) {
  event.target.classList.add('animated');
}

// Function to reset an animation
function resetAnimation(event) {
  event.target.classList.remove('animated');
}

// Function for smooth scrolling
function smoothScroll(event) {
  event.preventDefault();
  const targetId = event.target.getAttribute('href');
  const targetElement = document.querySelector(targetId);
  if (targetElement) {
    targetElement.scrollIntoView({ behavior: 'smooth' });
  }
}

