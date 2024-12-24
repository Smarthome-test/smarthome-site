// Load saved theme from localStorage and apply it
document.addEventListener('DOMContentLoaded', function () {
    const savedTheme = localStorage.getItem('theme') || 'light'; // Default to 'light' if no theme is saved
    document.documentElement.setAttribute('data-theme', savedTheme);
    changeMenuIcon(savedTheme);
    changeSideMenuIcons(savedTheme);

    // Set the select element to the saved theme value
    const themeSelector = document.getElementById('themeSelector');
    if (themeSelector) themeSelector.value = savedTheme;
});

// Change theme and save it to localStorage
function changeTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);

    // Change the menu icon based on the theme
    changeMenuIcon(theme);
    changeSideMenuIcons(theme);
}

// Function to change the menu icon based on the theme
function changeMenuIcon(theme) {
    const headerMenuIcon = document.getElementById('menu-icon-header');
    const sideMenuIcon = document.getElementById('menu-icon-side');

    // Assuming `data-light-icon` and `data-dark-icon` attributes are set in HTML
    headerMenuIcon.src = theme === 'dark' ? headerMenuIcon.dataset.darkIcon : headerMenuIcon.dataset.lightIcon;
    sideMenuIcon.src = theme === 'dark' ? sideMenuIcon.dataset.darkIcon : sideMenuIcon.dataset.lightIcon;
}

// Function to change the side menu icons based on the theme
function changeSideMenuIcons(theme) {
    // Get all menu icons and change their sources based on the theme
    document.querySelectorAll('.menu-icon').forEach(icon => {
        icon.src = theme === 'dark' ? icon.dataset.darkIcon : icon.dataset.lightIcon;
    });
}

// Toggle side menu visibility
function toggleMenu() {
    const sideMenu = document.getElementById('sideMenu');
    const isVisible = sideMenu.style.left === '0px';
    sideMenu.style.left = isVisible ? '-250px' : '0px';
}