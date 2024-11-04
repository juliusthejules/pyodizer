// Register Service Worker to intercept network requests and block trackers
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('./trackerBlocker-sw.js').then(registration => {
    console.log('Service Worker registered for blocking trackers.');
  }).catch(error => {
    console.error('Service Worker registration failed:', error);
  });
}