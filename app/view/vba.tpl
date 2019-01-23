<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Excel Format</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css">


    <link rel="stylesheet" href="/public/css/style1.css">

</head>

<body>

<h2>Excel Format</h2>
<p class="lead">Just for excel file</b></p>

<!-- Upload  -->
<form id="file-upload-form" class="uploader" enctype="multipart/form-data" method="post"
      action="/upload?_csrf={{ ctx.csrf | safe }}">
    <div class="js-input-file">
        <input id="file-upload" type="file" name="fileUpload"/>

        <label for="file-upload" id="file-drag">
            <img id="file-image" src="#" alt="Preview" class="hidden">
            <div id="start">
                <i class="fa fa-download" aria-hidden="true"></i>
                <div>Select a file or drag here</div>
                <div id="notimage" class="hidden">Please select an excel file</div>
                <span id="file-upload-btn" class="btn btn-primary">Select a file</span>
                <span class="input-file__info">No file chosen</span>
            </div>
            <div id="response" class="hidden">
                <div id="messages"></div>
                <progress class="progress" id="file-progress" value="0">
                    <span>0</span>%
                </progress>
            </div>
        </label>
    </div>
    <div class="row">
        <button class="btn btn-primary" type="submit">Upload</button>
    </div>

</form>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>


<script src="/public/js/index.js"></script>


</body>

</html>
<!--<!DOCTYPE html>-->
<!--<html>-->
<!--<head>-->
<!--<title>Upload Files using XMLHttpRequest - Minimal</title>-->

<!--<script type="text/javascript">-->
<!--function fileSelected() {-->
<!--var file = document.getElementById('fileToUpload').files[0];-->
<!--if (file) {-->
<!--var fileSize = 0;-->
<!--if (file.size > 1024 * 1024)-->
<!--fileSize = (Math.round(file.size * 100 / (1024 * 1024)) / 100).toString() + 'MB';-->
<!--else-->
<!--fileSize = (Math.round(file.size * 100 / 1024) / 100).toString() + 'KB';-->

<!--document.getElementById('fileName').innerHTML = 'Name: ' + file.name;-->
<!--document.getElementById('fileSize').innerHTML = 'Size: ' + fileSize;-->
<!--document.getElementById('fileType').innerHTML = 'Type: ' + file.type;-->
<!--}-->
<!--}-->

<!--function uploadFile() {-->
<!--var fd = new FormData();-->
<!--fd.append("fileToUpload", document.getElementById('fileToUpload').files[0]);-->
<!--var xhr = new XMLHttpRequest();-->
<!--xhr.upload.addEventListener("progress", uploadProgress, false);-->
<!--xhr.addEventListener("load", uploadComplete, false);-->
<!--xhr.addEventListener("error", uploadFailed, false);-->
<!--xhr.addEventListener("abort", uploadCanceled, false);-->
<!--xhr.open("POST", "/upload?_csrf={{ ctx.csrf | safe }}");-->
<!--xhr.send(fd);-->
<!--}-->

<!--function uploadProgress(evt) {-->
<!--if (evt.lengthComputable) {-->
<!--var percentComplete = Math.round(evt.loaded * 100 / evt.total);-->
<!--document.getElementById('progressNumber').innerHTML = percentComplete.toString() + '%';-->
<!--}-->
<!--else {-->
<!--document.getElementById('progressNumber').innerHTML = 'unable to compute';-->
<!--}-->
<!--}-->

<!--function uploadComplete(evt) {-->
<!--/* This event is raised when the server send back a response */-->
<!--alert(evt.target.responseText);-->
<!--}-->

<!--function uploadFailed(evt) {-->
<!--alert("There was an error attempting to upload the file.");-->
<!--}-->

<!--function uploadCanceled(evt) {-->
<!--alert("The upload has been canceled by the user or the browser dropped the connection.");-->
<!--}-->
<!--</script>-->
<!--</head>-->
<!--<body>-->
<!--<form id="form1" enctype="multipart/form-data" method="post" action="/upload?_csrf={{ ctx.csrf | safe }}">-->
<!--<div class="row">-->
<!--<label for="fileToUpload">Select a File to Upload</label><br/>-->
<!--<input type="file" name="fileToUpload" id="fileToUpload" onchange="fileSelected();"/>-->
<!--</div>-->
<!--<div id="fileName"></div>-->
<!--<div id="fileSize"></div>-->
<!--<div id="fileType"></div>-->
<!--<div class="row">-->
<!--<input type="button" onclick="uploadFile()" value="Upload"/>-->
<!--</div>-->
<!--<div id="progressNumber"></div>-->
<!--</form>-->
<!--</body>-->
<!--</html>-->
