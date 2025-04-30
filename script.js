let x = 100, y = 100;

document.addEventListener('keydown', (e) => {
  if(e.key === 'ArrowLeft') x -= 10;
  if(e.key === 'ArrowRight') x += 10;
});

function update() {
  ctx.fillStyle = 'black';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'red';
  ctx.fillRect(x, y, 50, 50);
  requestAnimationFrame(update);
}
update();
