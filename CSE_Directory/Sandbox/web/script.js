const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = 800;
canvas.height = 500;

let canvasPosition = canvas.getBoundingClientRect();
const mouse = {
  x: canvas.width/2,
  y: canvas.height/2,
  click: false
};
canvas.addEventListener('mousedown', function(event) {
  ctx.beginPath();
  ctx.moveTo(mouse.x, mouse.y);

  mouse.x = event.x - canvasPosition.left;
  mouse.y = event.y - canvasPosition.top;
  mouse.click = true;

  ctx.lineTo(mouse.x, mouse.y);
  ctx.stroke();
  
  ctx.beginPath();
  ctx.arc(mouse.x, mouse.y, 3, 0, 2*Math.PI);
  ctx.fillStyle = 'black';
  ctx.fill();
  
  
  
});
canvas.addEventListener('mouseup', function(event) {
  mouse.click = false;
});

