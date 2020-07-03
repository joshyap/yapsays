let quotes = [
    'You miss 100% of the shots you don\'t take - Wayne Gretzky - Michael Scott',
    "The greatest wealth is to live content with little - Plato",
    "Great minds discuss ideas. Average minds discuss events. Small minds discuss people. - Eleanor Roosevelt",
    "There is no greater agony than bearing an untold story inside you - May Angelou",
    "Could a greater miracle take place than for us to look through each other's eyes for an instant? - Henry David Thoreau",
    "One of the greatest diseases is to be nobody to anybody - Mother Teresa",
    "The greatest way to live with honor in this world is to be what we pretend to be - Socrates"
]

function getQuote() {
    let randomNumber = Math.floor(Math.random() * quotes.length)
    document.getElementById('newQuoteSection').innerHTML = quotes[randomNumber]
}