# Attribution API Documentation for Pyodizer

#### 1. **Overview**
The Pyodizer Attribution API allows developers and users to automatically load and display the required attribution for using Pyodizer on their website or app. This is done by asynchronously fetching an XML configuration file and dynamically injecting attribution content into the webpage.

#### 2. **`attribution.xml` Structure**

The `attribution.xml` file contains the necessary attribution details:

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
    <description>
        This XML file configures the attribution details for Pyodizer users.
    </description>
</attribution>
```

**Fields:**
- `<title>`: Name of the project (Pyodizer).
- `<url>`: Link to Pyodizer’s GitHub Pages site.
- `<name>`: The creator’s name (Joseph D. Smith), which links to his GitHub profile.
- `<license>`: License information with a link to the appropriate Creative Commons license.

---

#### 3. **JavaScript Integration**

The JavaScript (`attribution.js`) file fetches and parses the XML file, then injects the attribution into the HTML dynamically. This ensures that if there are updates in the XML file, the attribution will update automatically.

1. **Include the following `<div>` in your HTML where you want the attribution to appear:**

```html
<div id="attribution"></div>
```

2. **Link to the JavaScript file asynchronously:**

```html
<script src="https://juliusthejules.github.io/pyodizer/attribution/attribution.js" async></script>
```

---

#### 4. **Usage Example**

Here is an example of how to use the Attribution API within your HTML:

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
    <script src="https://juliusthejules.github.io/pyodizer/attribution/attribution.js" async></script>
</body>
</html>
```

---

#### 5. **Asynchronous Updates**

With this approach, any future updates to the `attribution.xml` file (e.g., changes in licensing, creator information, or project details) will automatically reflect on the websites or applications using the API. There is no need for manual changes to the HTML code when the XML is updated.

---

### **Conclusion**

By using this Attribution API, you ensure that proper credit is given to the creator of Pyodizer while maintaining a clean and modern website structure. The async nature of the implementation allows for easy updates to attribution information, providing flexibility and ease of use for developers.