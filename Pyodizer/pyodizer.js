//Function to delete existing cookies
function deleteAllCookies() {
            document.cookie.split(';').forEach(function(c) {
                document.cookie = c.trim().split('=')[0] + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            });
            console.log("All cookies have been deleted.");
        }

        // Function to block new cookies
        function blockCookies() {
            Object.defineProperty(document, 'cookie', {
                get: function() {
                    return '';
                },
                set: function() {
                    console.warn('Blocked a cookie from being set.');
                },
                configurable: true
            });
        }

        // Execute functions on page load
        window.onload = function() {
            deleteAllCookies();
            blockCookies();
        };
