document.getElementById('contactForm').addEventListener('submit', function (event) {
    var isValid = true;

    var inputs = document.querySelectorAll('#contactForm input[required], #contactForm select[required], #contactForm textarea[required]');

    inputs.forEach(function (input) {
        if (!input.value) {
            isValid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });

    var contactPreference = document.querySelector('input[name="contactPreference"]:checked');
    if (!contactPreference) {
        isValid = false;
        document.querySelectorAll('input[name="contactPreference"]').forEach(function (input) {
            input.parentNode.style.color = 'red';
        });
    } else {
        document.querySelectorAll('input[name="contactPreference"]').forEach(function (input) {
            input.parentNode.style.color = 'black';
        });
    }


    if (!isValid) {
        event.preventDefault();
        alert('Gracias por su mensaje, pronto recibirá una respuesta.');
        this.submit();
    }
});