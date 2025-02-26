function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed');

    // Ajuste para dispositivos móveis
    if (window.innerWidth <= 768) {
        const chatMain = document.querySelector('.chat-main');
        if (sidebar.classList.contains('collapsed')) {
            chatMain.style.marginLeft = '0';
        } else {
            chatMain.style.marginLeft = '250px';
        }
    }
}