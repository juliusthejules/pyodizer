# Attribution API Documentation for Pyodizer

## Overview

The Attribution API for Pyodizer allows users to easily include attribution information for the Pyodizer tool on their websites. This ensures that credit is given to the creator while maintaining compliance with the Creative Commons Attribution NonCommercial ShareAlike 4.0 International License.

## XML Configuration File

The attribution information is provided in an XML format, which can be hosted on any web server. Users are required to create an XML file named `attribution.xml` with the following structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<attribution>
    <creator>
        <name>Joseph D. Smith</name>
        <url>https://juliusthejules.github.io/pyodizer/</url>
        <license>
            <type>Creative Commons Attribution NonCommercial ShareAlike 4.0 International License</type>
            <url>https://creativecommons.org/licenses/by-nc-sa/4.0/</url>
        </license>
    </creator>
    <description>This XML file configures the attribution details for Pyodizer users.</description>
</attribution>
```

### File Structure Explanation

- **`<creator>`**: This section contains the details of the creator.
  - **`<name>`**: The name of the creator.
  - **`<url>`**: A URL linking to the creator's webpage or profile.
  - **`<license>`**: Information about the license under which the tool is released.
    - **`<type>`**: The name of the license.
    - **`<url>`**: A link to the license details.

- **`<description>`**: A brief description of the XML file's purpose.

## Implementation Steps

### Step 1: Create the XML File

1. Create a new file named `attribution.xml`.
2. Copy the provided XML structure into the file.
3. Modify the `<name>`, `<url>`, and license details as needed.
4. Upload the file to your web server or hosting platform, ensuring it is publicly accessible.

### Step 2: Include the Attribution in Your Website

To display the attribution on your website, you will need to include the following HTML and JavaScript code:

```html
<div id="attribution"></div>

<script>
    // Fetch the attribution XML file
    fetch('path/to/attribution.xml') // Replace with the actual path to your XML file
        .then(response => response.text())
        .then(data => {
            // Parse the XML data
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(data, "text/xml");

            // Extract creator information
            const creator = xmlDoc.getElementsByTagName("creator")[0];
            const name = creator.getElementsByTagName("name")[0].textContent;
            const url = creator.getElementsByTagName("url")[0].textContent;
            const licenseType = creator.getElementsByTagName("type")[0].textContent;
            const licenseUrl = creator.getElementsByTagName("url")[1].textContent;

            // Construct the attribution HTML
            const attributionHtml = `
                <p>Created by <a href="${url}" target="_blank">${name}</a> 
                under <a href="${licenseUrl}" target="_blank">${licenseType}</a>.</p>
            `;
            // Insert the attribution HTML into the page
            document.getElementById('attribution').innerHTML = attributionHtml;
        })
        .catch(error => console.error('Error fetching the attribution file:', error));
</script>
```

### Step 3: Replace the Path to the XML File

- Ensure you update the `fetch('path/to/attribution.xml')` line with the correct path to where the `attribution.xml` file is hosted.

### Step 4: Display Attribution

- Add the above HTML and JavaScript code to the section of your webpage where you want the attribution information to appear.
- Upon loading the page, the script will fetch the XML file, parse its contents, and display the attribution information in the designated `<div>` element.

## Example Implementation

Here’s a simple example of how to implement the attribution code within a basic HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodizer</title>
    <style>
        /* Add your existing styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        #attribution {
            margin-top: 20px;
            padding: 10px;
            background-color: #ecf0f1;
            border: 1px solid #3498db;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Pyodizer</h1>
    </header>

    <section>
        <p>Your content here...</p>
    </section>

    <div id="attribution"></div>

    <script>
        // Include the JavaScript code provided above here
    </script>
</body>
</html>
```

## Conclusion

This Attribution API allows Pyodizer users to easily provide appropriate credit, ensuring compliance with licensing requirements. By following the steps outlined above, users can seamlessly integrate attribution into their websites, promoting transparency and acknowledgment for the creators.
