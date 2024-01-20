function run_function(button_number){
    console.log("running");
    var uploaded_image_path = document.getElementById('uploaded-image').src;
    $.ajax({
        url: "/", // the endpoint
        type: "GET", // http method
        data: {
            button_number: button_number,
            uploaded_image_path: uploaded_image_path
        }, // data sent with the get request

        // handle a successful response
        success: function(data) {
            console.log("success");
            // Update the processed image on the page
            $('#processed-image').attr('src', 'data:image/png;base64,' + data.processed_image_base64);
        },

        // handle a non-successful response
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
};

function submitForm() {
    document.getElementById('upload-form').submit();
}

function downloadImage() {
    var processedImage = document.getElementById('processed-image');
    var link = document.createElement('a');
    link.href = processedImage.src;
    link.download = 'downloaded_image.png';
    link.click();
}