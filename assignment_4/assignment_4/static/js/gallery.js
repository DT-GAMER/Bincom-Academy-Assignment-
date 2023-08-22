/* gallery.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize interactive gallery
  initInteractiveGallery();
});

// Initialize interactive gallery
function initInteractiveGallery() {
  const galleryItems = document.querySelectorAll('.gallery-item');
  const lightbox = document.querySelector('.lightbox');
  const lightboxImage = document.querySelector('.lightbox-image');
  const closeButton = document.querySelector('.lightbox-close');

  galleryItems.forEach((item) => {
    item.addEventListener('click', () => {
      const imageUrl = item.getAttribute('data-image');
      openLightbox(imageUrl);
    });
  });

  closeButton.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', closeLightbox);

  function openLightbox(imageUrl) {
    lightboxImage.src = imageUrl;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
}

