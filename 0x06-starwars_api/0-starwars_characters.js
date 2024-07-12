#!/usr/bin/node

const request = require('request');

/**
 * Fetches character names from a Star Wars movie using the SWAPI.
 *
 * @param {number} movieId The episode number of the Star Wars movie.
 * @returns {Promise<string[]>} A promise that resolves to a list of character names, or rejects with an error.
 */
const getStarWarsCharacters = (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}`;

  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Error: Failed to retrieve data for movie ID ${movieId}`));
        return;
      }

      try {
        const data = JSON.parse(body);
        const characters = data.characters;

        if (!characters) {
          reject(new Error('No characters found for this movie'));
          return;
        }

        const characterNames = [];
        characters.forEach((characterUrl) => {
          request(characterUrl, (characterError, characterResponse, characterBody) => {
            if (characterError) {
              console.error(`Error fetching character details: ${characterError}`);
              return;
            }

            if (characterResponse.statusCode !== 200) {
              console.error(`Error fetching character data from ${characterUrl}`);
              return;
            }

            try {
              const characterData = JSON.parse(characterBody);
              characterNames.push(characterData.name);
            } catch (parseError) {
              console.error(`Error parsing character data: ${parseError}`);
            }
          });
        });

        resolve(characterNames);
      } catch (parseError) {
        reject(new Error('Error parsing movie data'));
      }
    });
  });
};

(async () => {
  const movieId = parseInt(process.argv[2]);

  if (isNaN(movieId)) {
    console.error('Error: Movie ID must be an integer.');
    process.exit(1);
  }

  try {
    const characters = await getStarWarsCharacters(movieId);
    characters.forEach((character) => console.log(character));
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
})();
