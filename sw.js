/*
Copyright 2015, 2019 Google Inc. All Rights Reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
*/

// Incrementing OFFLINE_VERSION will kick off the install event and force
// previously cached resources to be updated from the network.
const OFFLINE_VERSION = 9;
const CACHE_NAME = 'offline';
// Customize this with a different URL if needed.
const OFFLINE_URL = './index.html';

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Setting {cache: 'reload'} in the new request will ensure that the response
    // isn't fulfilled from the HTTP cache; i.e., it will be from the network.
    await cache.add(new Request(OFFLINE_URL, {cache: 'reload'}));
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    // Enable navigation preload if it's supported.
    if ('navigationPreload' in self.registration) {
      await self.registration.navigationPreload.enable();
    }
  })());

  // Tell the active service worker to take control of the page immediately.
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.mode === 'navigate') {
    event.respondWith((async () => {
      try {
        const preloadResponse = await event.preloadResponse;
        if (preloadResponse) {
          return preloadResponse;
        }

        const networkResponse = await fetch(event.request);
        return networkResponse;
      } catch (error) {
        console.log('Fetch failed; returning offline page instead.', error);

        const cache = await caches.open(CACHE_NAME);
        const cachedResponse = await cache.match(OFFLINE_URL);
        return cachedResponse;
      }
    })());
  }
});

// Background Sync setup for performing tasks like anonymizing in the background
self.addEventListener('sync', (event) => {
  if (event.tag === 'background-sync') {
    event.waitUntil(handleBackgroundSync());
  }
});

async function handleBackgroundSync() {
  try {
    // Example: Make an anonymizing request in the background
    const response = await fetch('/anonymize', {
      method: 'POST',
      body: JSON.stringify({ /* Add necessary data */ }),
      headers: {
        'Content-Type': 'application/json'
      }
    });
    const data = await response.json();
    console.log('Background sync successful:', data);
  } catch (error) {
    console.error('Background sync failed:', error);
  }
}

// Push Notifications for security alerts
self.addEventListener('push', (event) => {
  const data = event.data ? event.data.json() : {};
  const options = {
    body: data.body || 'Security alert from Pyodizer!',
    icon: './icon-512x512.png',
    badge: './icon-192x192.png'
  };

  event.waitUntil(
    self.registration.showNotification(data.title || 'Pyodizer Notification', options)
  );
});

// Optional: Periodic Background Sync (Experimental)
self.addEventListener('periodicsync', (event) => {
  if (event.tag === 'background-sync-periodic') {
    event.waitUntil(handleBackgroundSync());
  }
});
