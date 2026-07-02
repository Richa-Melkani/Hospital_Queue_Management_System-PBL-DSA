// ===============================
// Hospital Queue Management System
// script.js
// ===============================

// Confirm before treating a patient
document.addEventListener("DOMContentLoaded", function () {

    const treatButton = document.querySelector('a[href="/treat"]');

    if (treatButton) {

        treatButton.addEventListener("click", function (event) {

            const confirmTreatment = confirm(
                "Are you sure you want to treat the next patient?"
            );

            if (!confirmTreatment) {
                event.preventDefault();
            }

        });

    }

});

// Auto-hide Bootstrap alerts after 4 seconds
document.addEventListener("DOMContentLoaded", function () {

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.classList.remove("show");

            alert.classList.add("fade");

        }, 4000);

    });

});

// Scroll to top on page load
window.onload = function () {

    window.scrollTo(0, 0);

};