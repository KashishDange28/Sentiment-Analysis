document.getElementById('textForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const userInput = document.getElementById('user_input').value;

    fetch('/analyze_text', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `user_input=${encodeURIComponent(userInput)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('text_result').textContent = data.sentiment;
    });
});

document.getElementById('csvForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', document.getElementById('file').files[0]);

    fetch('/analyze_csv', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('positive_reviews').textContent = data.positive;
        document.getElementById('negative_reviews').textContent = data.negative;

        // Display the review lists
        displayReviews(data.positive_reviews, data.negative_reviews);

        // Update the pie chart
        updateChart(data.positive, data.negative);
    });
});

// Display the review lists
function displayReviews(positiveReviews, negativeReviews) {
    const positiveList = document.getElementById('positive_review_list');
    const negativeList = document.getElementById('negative_review_list');

    // Clear previous lists
    positiveList.innerHTML = '';
    negativeList.innerHTML = '';

    // Populate positive reviews
    positiveReviews.forEach(review => {
        const li = document.createElement('li');
        li.textContent = review;
        positiveList.appendChild(li);
    });

    // Populate negative reviews
    negativeReviews.forEach(review => {
        const li = document.createElement('li');
        li.textContent = review;
        negativeList.appendChild(li);
    });

    // Show or hide the lists
    document.getElementById('view_positive').onclick = function() {
        const positiveListContainer = document.getElementById('positive_list');
        positiveListContainer.style.display = positiveListContainer.style.display === 'none' ? 'block' : 'none';
    };

    document.getElementById('view_negative').onclick = function() {
        const negativeListContainer = document.getElementById('negative_list');
        negativeListContainer.style.display = negativeListContainer.style.display === 'none' ? 'block' : 'none';
    };
};
