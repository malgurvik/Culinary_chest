// User icon modal functionality
const loginBtn = document.getElementById("loginBtn");
const authModal = document.getElementById("authModal");
const closeAuthModal = document.getElementById("closeAuthModal");

// Open modal
loginBtn.addEventListener("click", () => {
  authModal.style.display = "flex";
});

// Close modal
closeAuthModal.addEventListener("click", () => {
  authModal.style.display = "none";
});

// Close modal when clicking outside
window.addEventListener("click", (e) => {
  if (e.target === authModal) {
    authModal.style.display = "none";
  }
});

// Edit profile

const editProfileBtn = document.querySelector(".edit-profile-btn");
const editProfileSection = document.querySelector(".edit-profile-section");

editProfileBtn.addEventListener("click", () => {
  editProfileSection.style.display =
    editProfileSection.style.display === "none" ? "block" : "none";
});
