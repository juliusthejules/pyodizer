// pyodizer.js - Client-Side Privacy Enhancements

// Disable cookies and clear existing ones
(function disableCookies() {
    document.cookie.split(";").forEach(cookie => {
        document.cookie = cookie.replace(/^ +/, "")
            .replace(/=.*/, `=;expires=${new Date(0).toUTCString()};path=/`);
    });
    Object.defineProperty(document, 'cookie', {
        get: () => "",
        set: () => {},
        configurable: false
    });
    console.log("Cookies disabled and cleared.");
})();

// Set cache to load only essential resources
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then(registration => {
        console.log("ServiceWorker registered:", registration);
    }).catch(error => {
        console.log("ServiceWorker registration failed:", error);
    });
}

// Create ServiceWorker (sw.js) file for cache control
// Only cache essential files
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('pyodizer-cache').then(cache => {
            return cache.addAll([
                // Specify essential files here
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
            ]);
        })
    );
});
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});

// Set all hyperlinks to open securely
(function secureHyperlinks() {
    document.querySelectorAll("a").forEach(link => {
        link.setAttribute("rel", "noopener noreferrer");
    });
    console.log("Hyperlink security enhanced.");
})();

// Disable telemetry by blocking tracking URLs
(function blockTelemetry() {
    const blockList = ["analytics", "track", "adservice"];
    const originalFetch = window.fetch;
    window.fetch = function(url, options) {
        if (blockList.some(block => url.includes(block))) {
            console.warn(`Blocked telemetry request to: ${url}`);
            return Promise.resolve(new Response(null, {status: 204}));
        }
        return originalFetch(url, options);
    };
    console.log("Telemetry requests blocked.");
})();

// Obfuscate browser fingerprinting attempts
(function obfuscateFingerprinting() {
    const originalUserAgent = navigator.userAgent;
    Object.defineProperty(navigator, 'userAgent', {
        get: () => "Mozilla/5.0 (compatible; Pyodizer/1.0)",
        configurable: false
    });

    const originalLanguages = navigator.languages;
    Object.defineProperty(navigator, 'languages', {
        get: () => ["en-US", "en"],
        configurable: false
    });

    console.log("Browser fingerprint obfuscation applied.");
})();

// Pyodizer™. Copyright © 2024. Joseph D. Smith.
