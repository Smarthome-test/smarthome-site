console.log("Ładowanie skryptu script.js");

function toggleMenu() {
    const sideMenu = document.getElementById('sideMenu');
    const isVisible = sideMenu.style.left === '0px';
    console.log('Widoczność menu:', isVisible); // Logowanie widoczności menu
    sideMenu.style.left = isVisible ? '-250px' : '0px';
}

