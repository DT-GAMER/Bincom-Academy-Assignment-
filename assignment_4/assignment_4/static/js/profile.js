/* profile.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize user profile interactions
  initUserProfile();
});

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

  // Function to update profile information
  const updateButton = document.querySelector('.update-button');
  if (updateButton) {
    updateButton.addEventListener('click', updateProfileInfo);
  }

  const changePasswordButton = document.querySelector('.change-password-button');
  if (changePasswordButton) {
    changePasswordButton.addEventListener('click', openChangePasswordModal);
  }
}

// Function to update profile information
function updateProfileInfo() {
  const formData = new FormData(document.querySelector('.edit-profile-form'));

  // Send a request to update the user's profile information
  fetch('/api/update-profile', {
    method: 'POST',
    body: formData
    // Add necessary headers and authentication if needed
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to update profile information');
    }
  })
  .then(data => {
    const successMessage = document.querySelector('.update-success');
    successMessage.style.display = 'block';

    setTimeout(() => {
      successMessage.style.display = 'none';
    }, 3000);

    // Update the displayed user profile information if needed
  })
  .catch(error => {
    console.error(error);
  });
}

// Function to open the change password modal
function openChangePasswordModal() {
  const changePasswordModal = document.querySelector('.change-password-modal');
  if (changePasswordModal) {
    changePasswordModal.classList.add('active');
  }
}

// Function to close the change password modal
function closeChangePasswordModal() {
  const changePasswordModal = document.querySelector('.change-password-modal');
  if (changePasswordModal) {
    changePasswordModal.classList.remove('active');
  }
}

// Event listener for modal close button
const modalCloseButton = document.querySelector('.modal-close-button');
if (modalCloseButton) {
  modalCloseButton.addEventListener('click', closeChangePasswordModal);
}

