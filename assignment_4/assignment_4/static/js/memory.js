/* memory.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize memory interactions
  initMemoryInteractions();
});

// Initialize memory interactions
function initMemoryInteractions() {
  const memoryCards = document.querySelectorAll('.memory-card');
  memoryCards.forEach((card) => {
    card.addEventListener('click', () => {
      const memoryId = card.getAttribute('data-memory-id');
      viewMemoryDetail(memoryId);
    });
  });

  // Other memory interactions...
  // For example: Like memory, comment on memory, etc.
  const likeButtons = document.querySelectorAll('.like-button');
  likeButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const memoryId = button.getAttribute('data-memory-id');
      likeMemory(memoryId);
    });
  });

  const commentForms = document.querySelectorAll('.comment-form');
  commentForms.forEach((form) => {
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      const memoryId = form.getAttribute('data-memory-id');
      const commentInput = form.querySelector('.comment-input');
      const comment = commentInput.value.trim();
      if (comment !== '') {
        postComment(memoryId, comment);
        commentInput.value = '';
      }
    });
  });

  // ...
}

// Function to view memory detail
function viewMemoryDetail(memoryId) {
  // Mock implementation to simulate displaying memory details
  const memoryDetailModal = document.querySelector('.memory-detail-modal');
  if (memoryDetailModal) {
    memoryDetailModal.classList.add('active');
    const memoryDetailContent = memoryDetailModal.querySelector('.modal-content');
    memoryDetailContent.innerHTML = `Memory ID: ${memoryId}<br>Memory details and content here...`;
  }
}

// Function to close memory detail modal
function closeMemoryDetailModal() {
  const memoryDetailModal = document.querySelector('.memory-detail-modal');
  if (memoryDetailModal) {
    memoryDetailModal.classList.remove('active');
  }
}

// Function to like a memory
function likeMemory(memoryId) {
  // Send a request to the server to update the like status
  fetch(`/api/memories/${memoryId}/like`, {
    method: 'POST',
    // Add necessary headers and authentication if needed
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to like memory');
    }
  })
  .then(data => {
    const likeButton = document.querySelector(`.like-button[data-memory-id="${memoryId}"]`);
    const likeCountElement = likeButton.querySelector('.like-count');
    const currentLikes = parseInt(likeCountElement.textContent);
    const isLiked = data.isLiked;

    if (isLiked) {
      likeButton.classList.add('liked');
      likeCountElement.textContent = currentLikes + 1;
    } else {
      likeButton.classList.remove('liked');
      likeCountElement.textContent = currentLikes - 1;
    }
  })
  .catch(error => {
    console.error(error);
  });
}

// Function to post a comment on a memory
function postComment(memoryId, comment) {
  // Send a request to the server to save the comment
  fetch(`/api/memories/${memoryId}/comments`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ comment: comment })
    // Add necessary authentication if needed
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Failed to post comment');
    }
  })
  .then(data => {
    const commentList = document.querySelector(`.comment-list[data-memory-id="${memoryId}"]`);
    const newCommentElement = document.createElement('li');
    newCommentElement.textContent = data.comment;
    commentList.appendChild(newCommentElement);
  })
  .catch(error => {
    console.error(error);
  });
}

