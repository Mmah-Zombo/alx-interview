#!/usr/bin/node
const request = require('request');

// Define the base URL for the Star Wars API
const baseUrl = 'https://swapi.dev/api';

// Function to fetch and print characters of a movie
function printMovieCharacters(movieId) {
  // Make a GET request to fetch the movie details
  request(`${baseUrl}/films/${movieId}/`, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const movie = JSON.parse(body);
        
        // Get the list of character URLs from the movie details
        const characterUrls = movie.characters;
        
        // Function to fetch and print character names
        function fetchAndPrintCharacterNames(index) {
          if (index < characterUrls.length) {
            // Make a GET request to fetch the character details
            request(characterUrls[index], (charError, charResponse, charBody) => {
              if (!charError && charResponse.statusCode === 200) {
                const character = JSON.parse(charBody);
                console.log(character.name);
              } else {
                console.error('Error fetching character:', charError);
              }
              
              // Fetch the next character
              fetchAndPrintCharacterNames(index + 1);
            });
          }
        }
        
        // Start fetching and printing character names
        fetchAndPrintCharacterNames(0);
      } else {
        console.error('Failed to fetch movie:', response.statusCode);
      }
    }
  });
}

// Usage: Pass the Movie ID as the first positional argument
const movieId = process.argv[2]; // Example: 3 for "Return of the Jedi"
if (movieId && movieId > 2) {
  printMovieCharacters(movieId);
} else {
  console.error('Please provide a Movie ID as a command-line argument.');
}
