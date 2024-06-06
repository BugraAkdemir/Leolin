document.addEventListener('DOMContentLoaded', function() {
    var countdownElement = document.getElementById('countdown');
    var countdownTime = 180; // 180 saniye (3 dakika)
    var count = 0;

    var countdownInterval = setInterval(function() {
        countdownTime--;
        countdownElement.textContent = countdownTime;

        if (countdownTime <= 0) {
            clearInterval(countdownInterval);
            countdownElement.textContent = "0";

            var secondCountdownInterval = setInterval(function() {
                count += 1;
                countdownElement.textContent = count;

                if (count >= 1000) {
                    clearInterval(secondCountdownInterval);
                    countdownElement.textContent = "Tamamlandı!";
                    countdownElement.classList.add("red-theme");
                }
            }, 500); // 500 milisaniyede bir güncelle
        }
    }, 1000); // 1 saniyede bir güncelle
});