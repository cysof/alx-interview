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

        const characterPromises = characters.map((characterUrl) => {
          return new Promise((characterResolve, characterReject) => {
            request(characterUrl, (characterError, characterResponse, characterBody) => {
              if (characterError) {
                characterReject(characterError);
                return;
              }

              if (characterResponse.statusCode !== 200) {
                characterReject(new Error(`Error fetching character data from ${characterUrl}`));
                return;
              }

              try {
                const characterData = JSON.parse(characterBody);
                characterResolve(characterData.name);
              } catch (parseError) {
                characterReject(new Error(`Error parsing character data: ${parseError}`));
              }
            });
          });
        });

        Promise.all(characterPromises)
          .then((characterNames) => {
            characterNames.forEach((character) => console.log(character));
            resolve();
          })
          .catch(reject);
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
    await getStarWarsCharacters(movieId);
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
})();
