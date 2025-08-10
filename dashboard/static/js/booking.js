document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('bookingForm');
  const successMessage = document.getElementById('successMessage');
  const termsAccepted = document.getElementById('termsAccepted');
  const modal = document.getElementById("termsModal");
  const closeBtn = document.getElementById("closeTerms");
  const agreeCheckbox = document.getElementById("agreeCheckbox");
  const acceptBtn = document.getElementById("acceptBtn");

  let isSubmitting = false; // Flag to prevent double submission

  form.addEventListener('submit', function (e) {
    if (isSubmitting) {
      // Already submitting, let the form submit naturally
      return;
    }
    e.preventDefault();

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

    // Validate Description
    if (!form.description.value.trim()) {
      setError(form.description, 'Please provide a tattoo description.');
      valid = false;
    }

    if (!valid) return; // Stop if validation fails

    // Check if terms accepted
    if (termsAccepted.value !== "true") {
      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
      return;
    }

    // Show success message and disable submit button
    successMessage.style.display = 'block';
    this.querySelector('button[type="submit"]').disabled = true;

    // Set submitting flag
    isSubmitting = true;

    // Submit form after short delay so user can see success message
    setTimeout(() => {
      form.submit();
    }, 1500);
  });

  function setError(input, message) {
    const errorEl = input.parentElement.querySelector('.error-message');
    if (errorEl) errorEl.textContent = message;
  }

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Modal controls
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

  // Enable/disable Accept button based on checkbox
  agreeCheckbox.addEventListener('change', () => {
    acceptBtn.disabled = !agreeCheckbox.checked;
    acceptBtn.classList.toggle("enabled", agreeCheckbox.checked);
  });

  acceptBtn.onclick = () => {
    // Mark terms as accepted
    termsAccepted.value = "true";

    // Close modal
    modal.style.display = "none";
    document.body.style.overflow = 'auto';

    // Directly submit form (skip validation because already done)
    isSubmitting = true;
    form.submit();
  };
});
