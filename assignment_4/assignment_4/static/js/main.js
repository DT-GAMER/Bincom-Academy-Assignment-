// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize tooltips
  initTooltips();

  // Initialize navigation menu for mobile devices
  initMobileNavigation();

  // Initialize interactive gallery
  initInteractiveGallery();

  // Initialize form validation
  initFormValidation();

  // Initialize user profile interactions
  initUserProfile();

  // Initialize search functionality
  initSearch();

  // Initialize memory interactions
  initMemoryInteractions();

  // Initialize animations and transitions
  initAnimations();

  // Initialize navigation menu interactions
  initNavigationMenu();

});

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

function sendGetRequest(url, callback, errorCallback) {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);

  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 400) {
      const response = JSON.parse(xhr.responseText);
      callback(response);
    } else {
      console.error('Request failed');
      if (errorCallback) {
        errorCallback();
      }
    }
  };

  xhr.onerror = function () {
    console.error('Request error');
    if (errorCallback) {
      errorCallback();
    }
  };

  xhr.send();
}

// Function to send a POST request using AJAX
function sendPostRequest(url, data, callback, errorCallback) {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');

  xhr.onload = function () {
    if (xhr.status >= 200 && xhr.status < 400) {
      const response = JSON.parse(xhr.responseText);
      callback(response);
    } else {
      console.error('Request failed');
      if (errorCallback) {
        errorCallback();
      }
    }
  };

  xhr.onerror = function () {
    console.error('Request error');
    if (errorCallback) {
      errorCallback();
    }
  };

  xhr.send(JSON.stringify(data));
}

// Function to display an error message
function showError(message) {
  const errorElement = document.createElement('div');
  errorElement.className = 'error-message';
  errorElement.textContent = message;
  document.body.appendChild(errorElement);

  setTimeout(() => {
    document.body.removeChild(errorElement);
  }, 5000);
}


// Initialize tooltips
function initTooltips() {
  const tooltips = document.querySelectorAll('[data-tooltip]');
  tooltips.forEach((tooltip) => {
    const content = tooltip.getAttribute('data-tooltip');
    tooltip.addEventListener('mouseenter', () => {
      showTooltip(tooltip, content);
    });
    tooltip.addEventListener('mouseleave', () => {
      hideTooltip(tooltip);
    });
  });
}

// Function to show a tooltip
function showTooltip(element, content) {
  const tooltip = document.createElement('div');
  tooltip.classList.add('tooltip');
  tooltip.textContent = content;
  element.appendChild(tooltip);
}

// Function to hide a tooltip
function hideTooltip(element) {
  const tooltip = element.querySelector('.tooltip');
  if (tooltip) {
    element.removeChild(tooltip);
  }
}

// Initialize mobile navigation menu
function initMobileNavigation() {
  const menuToggle = document.querySelector('.menu-toggle');
  const navList = document.querySelector('.nav-list');

  menuToggle.addEventListener('click', () => {
    navList.classList.toggle('active');
  });
}

// Initialize interactive gallery
function initInteractiveGallery() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  galleryItems.forEach((item) => {
    item.addEventListener('click', () => {
      // Handle gallery item click, e.g., open lightbox or navigate to memory detail
    });
  });
}

function initFormValidation() {
  const form = document.querySelector('.form');

  if (form) {
    form.addEventListener('submit', (event) => {
      // Prevent form submission if validation fails
      if (!validateForm(form)) {
        event.preventDefault();
      }
    });
  }
}

// Initialize user profile interactions
function initUserProfile() {
  const editProfileButton = document.querySelector('.edit-profile-button');
  const editProfileForm = document.querySelector('.edit-profile-form');
  const cancelButton = document.querySelector('.cancel-button');

  if (editProfileButton && editProfileForm && cancelButton) {
    editProfileButton.addEventListener('click', toggleEditMode);
    cancelButton.addEventListener('click', toggleEditMode);
  }
  
  function toggleEditMode() {
    editProfileForm.classList.toggle('active');
  }

  // Other user profile functions...
  // For example: Update profile information, change password, etc.
  const updateButton = document.querySelector('.update-button');
  if (updateButton) {
    updateButton.addEventListener('click', updateProfileInfo);
  }

  const changePasswordButton = document.querySelector('.change-password-button');
  if (changePasswordButton) {
    changePasswordButton.addEventListener('click', openChangePasswordModal);
  }

}

// Initialize search functionality
function initSearch() {
  const searchInput = document.querySelector('.search-input');
  const searchButton = document.querySelector('.search-button');
  const searchResults = document.querySelector('.search-results');

  if (searchInput && searchButton && searchResults) {
    searchButton.addEventListener('click', performSearch);
  }

  function performSearch() {
    const searchText = searchInput.value.trim().toLowerCase();
    const allMemories = document.querySelectorAll('.memory');
    searchResults.innerHTML = '';

    allMemories.forEach(memory => {
      const memoryText = memory.textContent.toLowerCase();
      if (memoryText.includes(searchText)) {
        searchResults.appendChild(memory.cloneNode(true));
      }
    });

    if (searchResults.children.length === 0) {
      const noResultsMessage = document.createElement('p');
      noResultsMessage.textContent = 'No results found.';
      searchResults.appendChild(noResultsMessage);
    }
  }
}
 
// Initialize memory interactions
function initMemoryInteractions() {
  const likeButtons = document.querySelectorAll('.like-button');
  const commentForms = document.querySelectorAll('.comment-form');

  likeButtons.forEach(button => {
    button.addEventListener('click', likeMemory);
  });

  commentForms.forEach(form => {
    form.addEventListener('submit', postComment);
  });
}

// Initialize animations and transitions
function initAnimations() {
  const animateElements = document.querySelectorAll('.animate');
  animateElements.forEach(element => {
    element.addEventListener('mouseenter', startAnimation);
    element.addEventListener('animationend', resetAnimation);
  });

  function startAnimation(event) {
    event.target.classList.add('animated');
  }

  function resetAnimation(event) {
    event.target.classList.remove('animated');
  }
}

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

