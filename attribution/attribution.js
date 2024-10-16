// attribution.js
fetch('./attribution/attribution.xml') // Path to the XML file
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(data, "text/xml");

        const creator = xmlDoc.getElementsByTagName("creator")[0];
        const name = creator.getElementsByTagName("name")[0].textContent;
        const url = creator.getElementsByTagName("url")[0].textContent;
        const licenseType = creator.getElementsByTagName("type")[0].textContent;
        const licenseUrl = creator.getElementsByTagName("url")[1].textContent;

        const attributionHtml = `
            <p>Created by <a href="${url}" target="_blank">${name}</a> 
            under <a href="${licenseUrl}" target="_blank">${licenseType}</a>.</p>
        `;
        document.getElementById('attribution').innerHTML = attributionHtml;
    })
    .catch(error => console.error('Error fetching the attribution file:', error));