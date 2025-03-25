/**
* PHP Email Form Validation - v3.9
* URL: https://bootstrapmade.com/php-email-form/
* Author: BootstrapMade.com
*/
(function () {
  "use strict";

let forms = document.querySelectorAll('.php-email-form');

forms.forEach(function(form) {
  form.addEventListener('submit', function(event) {
    event.preventDefault();

    let thisForm = this;
    let action = thisForm.getAttribute('action');
    let formData = new FormData(thisForm);

    let loading = thisForm.querySelector('.loading');
    let errorMessage = thisForm.querySelector('.error-message');
    let sentMessage = thisForm.querySelector('.sent-message');

    loading.style.display = 'block';
    errorMessage.style.display = 'none';
    sentMessage.style.display = 'none';

    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': csrftoken,  // CSRF tokenini qo'shish
      },
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Xatolik yuz berdi');
      }
    })
    .then(data => {
      loading.style.display = 'none';
      if (data.status === 'success') {
        sentMessage.style.display = 'block';
        thisForm.reset();
      } else {
        errorMessage.innerHTML = data.message || 'Xabar yuborishda xatolik yuz berdi';
        errorMessage.style.display = 'block';
      }
    })
    .catch(error => {
      loading.style.display = 'none';
      errorMessage.innerHTML = error.message;
      errorMessage.style.display = 'block';
    });
  });
});


  function php_email_form_submit(thisForm, action, formData) {
    fetch(action, {
      method: 'POST',
      body: formData,
      headers: {'X-Requested-With': 'XMLHttpRequest'}
    })
    .then(response => {
      if( response.ok ) {
        return response.text();
      } else {
        throw new Error(`${response.status} ${response.statusText} ${response.url}`); 
      }
    })
    .then(data => {
      thisForm.querySelector('.loading').classList.remove('d-block');
      if (data.trim() == 'OK') {
        thisForm.querySelector('.sent-message').classList.add('d-block');
        thisForm.reset(); 
      } else {
        throw new Error(data ? data : 'Form submission failed and no error message returned from: ' + action); 
      }
    })
    .catch((error) => {
      displayError(thisForm, error);
    });
  }

  function displayError(thisForm, error) {
    thisForm.querySelector('.loading').classList.remove('d-block');
    thisForm.querySelector('.error-message').innerHTML = error;
    thisForm.querySelector('.error-message').classList.add('d-block');
  }

})();
