async function setAccountDetails() {
    const bucketUrl = document.getElementById('bucketUrl').value;
    const bucketKey = document.getElementById('bucketKey').value;
    const bucketSecret = document.getElementById('bucketSecret').value;
    const bucketName = document.getElementById('bucketName').value;

    const response = await fetch('http://127.0.0.1:8000/set_account_details', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            bucket_url: bucketUrl,
            bucket_key: bucketKey,
            bucket_secret: bucketSecret,
            bucket_name: bucketName,
        }),
    });

    const result = await response.json();
    document.getElementById('accountForm').reset();
    alert(result.message);
}

async function refreshEmbeddings() {
    const response = await fetch('http://127.0.0.1:8000/refresh_embeddings');
    const result = await response.json();
    alert(result.message);
}

async function searchImage() {
    const searchInput = document.getElementById('searchInput').value;
    const response = await fetch(`http://127.0.0.1:8000/search?item=${searchInput}`);
    const result = await response.json();

    const searchResults = document.getElementById('searchResults');
    searchResults.innerHTML = `<p>${result.message}</p>`;

    if (result.result) {
        result.result.forEach(image => {
            const imageContainer = document.createElement('div');
            imageContainer.classList.add('image-container');

            const imageElement = document.createElement('img');
            imageElement.src = image.image_url;
            imageElement.alt = `Image ${image.id}`;

            const imageDetails = document.createElement('div');
            imageDetails.classList.add('image-details');
            imageDetails.innerHTML = `<p>ID: ${image.id}</p><p>Distance: ${image.distance.toFixed(2)}</p>`;
            
            imageContainer.appendChild(imageElement);
            imageContainer.appendChild(imageDetails);
            searchResults.appendChild(imageContainer);
        });
    }
}