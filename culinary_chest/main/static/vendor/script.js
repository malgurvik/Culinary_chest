

// Edit profile

const editProfileBtn = document.querySelector(".edit-profile-btn");
const editProfileSection = document.querySelector(".edit-profile-section");

editProfileBtn.addEventListener("click", () => {
  editProfileSection.style.display =
    editProfileSection.style.display === "none" ? "block" : "none";
});
