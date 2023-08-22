/* utils.js */

// Utility function to get a DOM element by ID
function getById(elementId) {
  return document.getElementById(elementId);
}

// Utility function to show an element
function showElement(element) {
  element.style.display = 'block';
}

// Utility function to hide an element
function hideElement(element) {
  element.style.display = 'none';
}

// Utility function to check if an element has a specific class
function hasClass(element, className) {
  return element.classList.contains(className);
}

// Utility function to add a class to an element
function addClass(element, className) {
  element.classList.add(className);
}

// Utility function to remove a class from an element
function removeClass(element, className) {
  element.classList.remove(className);
}

