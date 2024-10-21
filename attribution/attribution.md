# Attribution Documentation for Pyodizer

#### 1. **Overview**
The Pyodizer Attribution system allows developers and users to easily reuse and display the required attribution for using Pyodizer on their websites or apps. The attribution details are configured through an XML file that can be manually cloned and set up by users. By including the XML file and JavaScript, the attribution content can be dynamically injected into the webpage.

#### 2. **`attribution.xml` Structure**

The `attribution.xml` file contains all necessary attribution details:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<attribution>
    <credits>
        <title>Pyodizer</title>
        <url>https://juliusthejules.github.io/pyodizer/</url>
    </credits>
    <creator>
        <name>Joseph D. Smith</name>
        <url>https://juliusthejules.github.io/juliusthejules/</url>
        <license>
            <type>Creative Commons Attribution NonCommercial ShareAlike 4.0 International License</type>
            <url>https://creativecommons.org/licenses/by-nc-sa/4.0/</url>
        </license>
    </creator>
    <!-- This XML file configures the attribution details for Pyodizer users. -->
</attribution>
```

**Fields:**
- `<title>`: The name of the project (Pyodizer).
- `<url>`: A link to Pyodizer’s GitHub Pages site.
- `<name>`: The creator’s name (Joseph D. Smith), which links to his GitHub profile.
- `<license>`: License details, with a link to the Creative Commons license.

---

#### 3. **JavaScript Integration**

The provided JavaScript (`attribution.js`) file can be used to fetch the XML file and inject the attribution into your HTML dynamically.

1. **Include the following `<div>` where you want the attribution to appear:**

```html
<div id="attribution"></div>
```

2. **Link to the JavaScript file asynchronously:**

```html
<script src="./attribution/attribution.js" async></script>
```

---

#### 4. **Manual Setup for Cloning**

Because GitHub Pages does not natively support sending or receiving API endpoints, users will need to manually clone the `attribution.xml` and `attribution.js` files and host them on their own servers or web hosting solutions.

1. Clone the necessary files from the repository.
2. Upload the files to your own web host.
3. Reference the JavaScript file from your hosted environment in your HTML file.

```html
<script src="your-host/attribution.js" async></script>
```

---

#### 5. **Usage Example**

Below is an example of how to use the attribution system within your HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodizer Attribution Example</title>
</head>
<body>
    <header>
        <h1>Welcome to Pyodizer</h1>
    </header>

    <section>
        <p>Pyodizer helps configure privacy settings for Python scripts.</p>

        <!-- Attribution content will be dynamically loaded here -->
        <div id="attribution"></div>
    </section>

    <footer>
        <p>&copy; 2024 Pyodizer by Joseph D. Smith</p>
    </footer>

    <!-- Asynchronous loading of attribution -->
    <script src="your-host/attribution.js" async></script>
</body>
</html>
```

---

#### 6. **Updates Across Pages**

With this system, once set up, users can reuse the same attribution across multiple pages. Any changes to the XML file (e.g., updating the project details, license, or creator information) will reflect automatically across all pages where it’s implemented.

---

### **Conclusion**

By using this attribution system, you ensure proper credit is given to the creator of Pyodizer while maintaining a consistent and reusable setup across multiple pages. Although users need to manually set up the files, this solution provides flexibility and ease of updating attribution content.
