/* forms.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize form validation for relevant forms
  initFormValidation();
});

// Initialize form validation
function initFormValidation() {
  const forms = document.querySelectorAll('.needs-validation');

  forms.forEach((form) => {
    form.addEventListener('submit', (event) => {
      if (!validateForm(form)) {
        event.preventDefault();
      }
    });
  });
}

// Function to validate a form
function validateForm(form) {
  const requiredFields = form.querySelectorAll('.required');
  let isValid = true;

  requiredFields.forEach((field) => {
    if (field.value.trim() === '') {
      isValid = false;
      addErrorClass(field); // Add error class to field
      displayErrorMessage(field, 'This field is required.'); // Display error message
    } else {
      removeErrorClass(field); // Remove error class from field
      hideErrorMessage(field); // Hide error message
    }
  });

  // Validate email format
  const emailField = form.querySelector('[type="email"]');
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (emailField && !emailPattern.test(emailField.value)) {
    isValid = false;
    addErrorClass(emailField); // Add error class to email field
    displayErrorMessage(emailField, 'Enter a valid email address.'); // Display error message
  } else {
    removeErrorClass(emailField); // Remove error class from email field
    hideErrorMessage(emailField); // Hide error message
  }

  return isValid;
}

// Function to add error class to a field
function addErrorClass(field) {
  field.classList.add('error');
}

// Function to remove error class from a field
function removeErrorClass(field) {
  field.classList.remove('error');
}

// Function to display an error message
function displayErrorMessage(field, message) {
  const errorContainer = field.closest('.field-container').querySelector('.error-message');
  if (errorContainer) {
    errorContainer.textContent = message;
    errorContainer.style.display = 'block';
  }
}

// Function to hide an error message
function hideErrorMessage(field) {
  const errorContainer = field.closest('.field-container').querySelector('.error-message');
  if (errorContainer) {
    errorContainer.style.display = 'none';
  }
}

