document.addEventListener('DOMContentLoaded', function() {
    function updateTime() {
        const now = new Date();

        const year = now.getFullYear();
        const month = now.getMonth() + 1;
        const day = now.getDate();
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();

        const formatted = `${year}年${month}月${day}日 ${hours}:${minutes}:${seconds}`;
        document.getElementById('clock').textContent = formatted;
    }
    updateTime();
    setInterval(updateTime, 1000);
})