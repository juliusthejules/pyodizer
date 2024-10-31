# Pyodizer Implementation Guide

Follow the steps below to implement **Pyodizer** on your website. This guide will walk you through adding the necessary scripts to your `<head>` section, along with important usage information.

## Step 1: Integrate Pyodizer

To add **Pyodizer** to your website, place the following code in the `<head>` section of your HTML file. This includes preloading the necessary resources for optimal performance and then loading the scripts for execution.

### Step 2: Add the Required `<link>` and `<script>` Tags

Add the following lines to the `<head>` of your HTML document:

    <!-- Preload Pyodizer Scripts -->
<link rel="preload" as="script" href="https://juliusthejules.github.io/pyodizer/Pyodizer/pyodizer.py" type="text/x-python" crossorigin="anonymous">
<link rel="preload" as="script" href="https://juliusthejules.github.io/pyodizer/Pyodizer/pyodizer.js" type="text/javascript" crossorigin="anonymous">

<!-- Load Pyodizer Scripts Asynchronously with Cross-Origin Policy -->
<script src="https://juliusthejules.github.io/pyodizer/Pyodizer/pyodizer.js" type="text/javascript" async crossorigin="anonymous"></script>
<script src="https://juliusthejules.github.io/pyodizer/Pyodizer/pyodizer.py" type="text/x-python" async crossorigin="anonymous"></script>

#### Licensing and Attribution

By using **Pyodizer**, you agree to the following terms:

- **License**: Pyodizer is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). 
- **Attribution**: You must include appropriate credit, provide a link to the license, and indicate if changes were made. This should be done in a reasonable way, but not in any manner that suggests Pyodizer or its creator endorses you or your use.
- **Commercial Use**: Commercial use of Pyodizer is **strictly prohibited** without an active subscription. A valid subscription provides automatic permission for commercial purposes. 

To learn more about subscription options, please visit the `Commercial Use` section of the [index.html](https://juliusthejules.github.io/pyodizer/index.html) page.
