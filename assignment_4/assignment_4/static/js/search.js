
/* search.js */

// Document ready event
document.addEventListener('DOMContentLoaded', function () {
  // Initialize search functionality
  initSearch();
});

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

