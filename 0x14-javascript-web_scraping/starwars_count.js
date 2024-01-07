#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const characterId = 18; // Wedge Antilles

// Function to get the number of movies where the character is present
function getMovieCount (apiUrl, characterId) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      console.error('Error:', error);
      return;
    }

    const films = JSON.parse(body).results;
    const movieCount = films.reduce((count, film) => {
      if (film.characters.includes(`${apiUrl}people/${characterId}/`)) {
        return count + 1;
      }
      return count;
    }, 0);

    console.log(movieCount);
  });
}

// Call the function with the provided API URL and character ID
getMovieCount(apiUrl, characterId);
