/* Marquee slider effect for the icons - minimalista, só rodando */

document.addEventListener('DOMContentLoaded', function () {
  const marquee = document.querySelector('.slider-marquee');
  if (!marquee) return;

  // Duplicate the icons for seamless looping
  const marqueeContent = marquee.innerHTML;
  marquee.innerHTML += marqueeContent;

  // Setup
  let marqueeWidth = marquee.scrollWidth / 2;
  let speed = 50; // px per second
  let pos = 0;
  let lastTime = null;

  marquee.style.animation = 'none';
  marquee.style.willChange = 'transform';

  function animate(ts) {
    if (!lastTime) lastTime = ts;
    let dt = (ts - lastTime) / 1000;
    lastTime = ts;
    pos -= speed * dt;
    if (Math.abs(pos) >= marqueeWidth) pos = 0;
    marquee.style.transform = `translateX(${pos}px)`;
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

  // Responsivo
  window.addEventListener('resize', () => {
    marqueeWidth = marquee.scrollWidth / 2;
  });
});
