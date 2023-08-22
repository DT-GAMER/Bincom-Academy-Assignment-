/* ajax.js */

// Function to send a GET request using AJAX
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

