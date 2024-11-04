// Listen for fetch events and block requests matching tracking patterns
self.addEventListener('fetch', event => {
  const url = event.request.url;
  
  // Define patterns commonly found in tracking URLs
  const blockPatterns = [
    'track', 'analytics', 'adservice', 'pixel', 'doubleclick', 'collect',
    'facebook', 'google-analytics', 'advertising', 'click', 'data-collection',
    'tag', 'beacon', 'metrics'
  ];

  // Check if the URL contains any block patterns
  const isTracker = blockPatterns.some(pattern => url.includes(pattern));
  
  if (isTracker) {
    // Block the request by responding with an empty response
    event.respondWith(new Response(null, { status: 204 }));
    console.log(`Blocked tracker: ${url}`);
  } else {
    // Proceed with the original request
    event.respondWith(fetch(event.request));
  }
});