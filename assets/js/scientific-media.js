/* Scientific media only: pause other experiments and honour motion preference changes.
   Native controls, posters, and all navigation remain usable without JavaScript. */
(() => {
  const videos = Array.from(document.querySelectorAll('[data-scientific-media]'));
  for (const video of videos) {
    video.addEventListener('play', () => {
      for (const other of videos) if (other !== video) other.pause();
    });
  }
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const pauseAll = () => videos.forEach(video => video.pause());
  if (motion.matches) pauseAll();
  motion.addEventListener('change', event => { if (event.matches) pauseAll(); });
  document.addEventListener('visibilitychange', () => { if (document.hidden) pauseAll(); });
})();
