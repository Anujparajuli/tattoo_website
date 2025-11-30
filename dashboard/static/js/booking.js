document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('bookingForm');
  const termsAccepted = document.getElementById('termsAccepted');
  const modal = document.getElementById("termsModal");
  const closeBtn = document.getElementById("closeTerms");
  const agreeCheckbox = document.getElementById("agreeCheckbox");
  const acceptBtn = document.getElementById("acceptBtn");

  // Success Popup
  const successPopup = document.getElementById('successPopup');
  const closePopup = document.getElementById('closePopup');
  const okBtn = document.getElementById('okBtn');

  let isSubmitting = false; // Flag to prevent double submission

  form.addEventListener('submit', function(e) {
    e.preventDefault();
    if (isSubmitting) return;

    // Clear previous error messages
    const errorMessages = form.querySelectorAll('.error-message');
    errorMessages.forEach(em => em.textContent = '');

    let valid = true;

    // Validate Full Name
    if (!form.name.value.trim()) {
      setError(form.name, 'Please enter your full name.');
      valid = false;
    }

    // Validate Email
    if (!form.email.value.trim()) {
      setError(form.email, 'Please enter your email.');
      valid = false;
    } else if (!validateEmail(form.email.value.trim())) {
      setError(form.email, 'Please enter a valid email address.');
      valid = false;
    }

    // Validate Phone
    if (!form.phone.value.trim()) {
      setError(form.phone, 'Please enter your phone number.');
      valid = false;
    }

    if (!valid) return;

    // Check if terms accepted
    if (termsAccepted.value !== "true") {
      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
      return;
    }

    // Submit form via AJAX
    const formData = new FormData(form);
    isSubmitting = true;

    fetch(form.action || window.location.href, {
      method: 'POST',
      body: formData,
      headers: {
        'X-Requested-With': 'XMLHttpRequest'
      }
    })
    .then(response => response.json())
    .then(data => {
      isSubmitting = false;
      if (data.success) {
        // Show popup
        successPopup.style.display = 'flex';
        // Reset form
        form.reset();
        const fileInput = document.getElementById('reference');
        if (fileInput) fileInput.value = '';
        // Reset terms
        termsAccepted.value = "false";
        agreeCheckbox.checked = false;
        acceptBtn.disabled = true;
      } else if (data.errors) {
        // Display field errors
        Object.keys(data.errors).forEach(field => {
          const fieldEl = document.getElementById('id_' + field);
          if (fieldEl) {
            let errorEl = fieldEl.parentElement.querySelector('.error-message');
            if (errorEl) {
              errorEl.textContent = data.errors[field][0];
            }
          }
        });
      }
    })
    .catch(err => {
      console.error('Error submitting form:', err);
      isSubmitting = false;
    });
  });

  function setError(input, message) {
    const errorEl = input.parentElement.querySelector('.error-message');
    if (errorEl) errorEl.textContent = message;
  }

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Terms Modal Controls
  closeBtn.onclick = () => {
    modal.style.display = "none";
    document.body.style.overflow = 'auto';
  };

  window.onclick = event => {
    if (event.target === modal) {
      modal.style.display = "none";
      document.body.style.overflow = 'auto';
    }
  };

  window.addEventListener("keydown", event => {
    if (event.key === "Escape" && modal.style.display === "flex") {
      modal.style.display = "none";
      document.body.style.overflow = 'auto';
    }
  });

  agreeCheckbox.addEventListener('change', () => {
    acceptBtn.disabled = !agreeCheckbox.checked;
    acceptBtn.classList.toggle("enabled", agreeCheckbox.checked);
  });

  acceptBtn.onclick = () => {
    termsAccepted.value = "true";
    modal.style.display = "none";
    document.body.style.overflow = 'auto';
  };

  // Success Popup Controls
  closePopup.addEventListener('click', () => {
    successPopup.style.display = 'none';
  });

  okBtn.addEventListener('click', () => {
    successPopup.style.display = 'none';
  });
});
