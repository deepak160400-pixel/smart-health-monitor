function show(id){

document
.querySelectorAll(
".content > div"
)

.forEach(

x=>

x.style.display=

"none"

)

document
.getElementById(
id
)

.style.display=

"block"

}

function previewImage(){

const input=

document.getElementById(
"thermalInput"
)

if(

!input.files[0]

){

return

}

const reader=

new FileReader()

reader.onload=

function(e){

document
.querySelector(
".upload-zone"
)

.style.display=

"none"

const img=

document
.getElementById(
"previewImage"
)

img.src=

e.target.result

img.style.display=

"block"

document
.getElementById(
"imageActions"
)

.style.display=

"flex"

}

reader.readAsDataURL(

input.files[0]

)

}

function replaceImage(){

document
.getElementById(
"thermalInput"
)

.click()

}

function removeImage(){

document
.getElementById(
"thermalInput"
)

.value=

""

document
.getElementById(
"previewImage"
)

.style.display=

"none"

document
.querySelector(
".upload-zone"
)

.style.display=

"flex"

document
.getElementById(
"imageActions"
)

.style.display=

"none"

document
.getElementById(
"result"
)

.innerHTML=

""

document
.getElementById(
"assistantResult"
)

.innerHTML=

""

}

function analyzeImage(){

document
.getElementById(
"result"
)

.innerHTML=

`

<div class="metric">

Detected Footprints

<span>

1 Foot

</span>

</div>

<div class="metric">

Status

<span>

Need Both Feet

</span>

</div>

<div class="final-result">

Upload both feet for comparison

</div>

`

document
.getElementById(
"assistantResult"
)

.innerHTML=

`

<h3>

AI Summary</h3>

<ul>

<li>

Image uploaded successfully

</li>

<li>

Comparison unavailable

</li>

<li>

Upload another image if required

</li>

</ul>

`

}
