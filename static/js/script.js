document.getElementById('review-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let review = document.getElementById('review').value;
    
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `review=${encodeURIComponent(review)}`
    })
    .then(response => response.json())
    .then(data => {
        let result = `Positive: ${data.pos}, Neutral: ${data.neu}, Negative: ${data.neg}, Compound: ${data.compound}`;
        document.getElementById('result').innerText = result;
    });
});
