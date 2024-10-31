const CACHE_NAME = 'temporary-cache';
const OFFLINE_URL = './index.html';  // Your offline fallback page
const TEMP_CACHE_DURATION = 60 * 60 * 24; // Cache resources for 1 day (in seconds)

// List of URLs to cache for offline use
const urlsToCache = [
  OFFLINE_URL,
  './index.html',
  './style.css',
  './app.webmanifest',
  './social.png',
  './icon-512x512.png',
  './icon-384x384.png',
  './icon-256x256.png',
  './icon-192x192.png',
  './Pyodizer/pyodizer.py',
  './Pyodizer/pyodizer.js',
  './robots.txt',
  './sitemap.xml'
];

self.addEventListener('install', (event) => {
  // Pre-cache essential offline resources
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
  // Immediately activate the service worker without waiting
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  // Clean up old caches and activate the new service worker
  event.waitUntil(
    (async () => {
      const keys = await caches.keys();
      await Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })()
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Network first, fallback to cache for offline support
  event.respondWith(
    (async () => {
      try {
        const response = await fetch(event.request);
        // If the request succeeds, temporarily cache the resource
        const cache = await caches.open(CACHE_NAME);
        cache.put(event.request, response.clone());
        return response;
      } catch (error) {
        // If network fails, check cache for offline resources
        const cache = await caches.open(CACHE_NAME);
        const cachedResponse = await cache.match(event.request);
        return cachedResponse || fetch(OFFLINE_URL); // Return offline page if not found
      }
    })()
  );
});

self.addEventListener('sync', (event) => {
  if (event.tag === 'clear-temp-cache') {
    event.waitUntil(clearTemporaryCache());
  }
});

// Function to clear the cache after a specified duration
async function clearTemporaryCache() {
  const cache = await caches.open(CACHE_NAME);
  const requests = await cache.keys();
  const now = Date.now();
  
  await Promise.all(
    requests.map(async (request) => {
      const response = await cache.match(request);
      const dateHeader = response.headers.get('Date');
      const dateCached = new Date(dateHeader).getTime();

      if (now - dateCached > TEMP_CACHE_DURATION * 1000) {
        // Delete the cached resource if it's older than the set duration
        await cache.delete(request);
      }
    })
  );
    }
