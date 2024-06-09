document.addEventListener('DOMContentLoaded', function () {
    const uploadBtn = document.getElementById('uploadBtn');
    const modal = document.getElementById('modal');
    const closeBtn = document.getElementById('closeBtn');
    const uploadForm = document.getElementById('uploadForm');

    uploadBtn.addEventListener('click', function () {
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden'; // Prevent background scrolling
    });

    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto'; // Allow background scrolling
    });

    window.addEventListener('click', function (event) {
        if (event.target == modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto'; // Allow background scrolling
        }
    });

    uploadForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(uploadForm);

        fetch('/article', { // Replace '/upload' with your server endpoint
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto'; // Allow background scrolling
                window.location.reload()
            })
            .catch(error => {
                alert('An error occurred while uploading the files.');
            });
    });
});