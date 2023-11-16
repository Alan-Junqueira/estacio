const img = new Image();
img.src = "../assets/images/passaro.jpg";
img.onload = function() {
  // Create a canvas and draw the image onto it
  const canvas = document.createElement('canvas');
  canvas.width = img.width;
  canvas.height = img.height;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0, img.width, img.height);

  // Get the image data from the canvas
  const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;

  // Loop over each pixel and set the red, green, and blue channels to 0
  for(let i = 0; i < data.length; i += 4) {
    data[i] = 0;     // Red
    data[i + 1] = 0; // Green
    data[i + 2] = 0; // Blue
  }

  // Put the modified image data back onto the canvas
  ctx.putImageData(imageData, 0, 0);

  // Add the canvas to the body of the document
  // So you can see the modified image
  document.body.appendChild(canvas);
};