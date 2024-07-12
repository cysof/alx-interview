#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie.id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch data from the given URL
const fetchData = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error); // Reject the promise if there's an error
      } else if (response.statusCode !== 200) {
        reject(
          new Error(`Failed to load data, status code: ${response.statusCode}`)
        ); // Reject the promise if the response status code is not 200
      } else {
        resolve(JSON.parse(body)); // Resolve the promise with the parsed JSON data
      }
    });
  });
};

// Fetch movie data and display character names
fetchData(apiUrl)
  .then((movieData) => {
    const characterPromises = movieData.characters.map(
      (characterUrl) => fetchData(characterUrl) // Create an array of promises to fetch character data
    );
    return Promise.all(characterPromises); // Wait for all promises to resolve
  })
  .then((characters) => {
    characters.forEach((character) => {
      console.log(character.name); // Print the name of each character
    });
  })
  .catch((error) => {
    console.log('Error:', error.message); // Handle any errors that occur during the process
  });