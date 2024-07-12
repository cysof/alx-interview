#!/usr/bin/node

const request = require('request');

const API_BASE_URL = 'https://swapi.dev/api/films';

/**
 * Fetches character names from a Star Wars movie.
 *
 * @param {number} movieId The episode number of the Star Wars movie.
 * @returns {Promise<string[]>} A promise that resolves to a list of character names, or rejects with an error.
 */
const getStarWarsCharacters = async (movieId) => {
  const url = `${API_BASE_URL}/${movieId}`;

  try {
    const response = await request.get(url);
    const data = JSON.parse(response.body);
    const characters = data.characters || [];

    if (!characters.length) {
      throw new Error('No characters found for this movie');
    }

    const characterPromises = characters.map(fetchCharacterName);
    const characterNames = await Promise.all(characterPromises);

    return characterNames;
  } catch (error) {
    throw error;
  }
};

/**
 * Fetches the name of a Star Wars character.
 *
 * @param {string} characterUrl The URL of the character resource.
 * @returns {Promise<string>} A promise that resolves to the character's name, or rejects with an error.
 */
const fetchCharacterName = async (characterUrl) => {
  try {
    const response = await request.get(characterUrl);
    const data = JSON.parse(response.body);
    return data.name;
  } catch (error) {
    throw new Error(`Error fetching character data from ${characterUrl}`);
  }
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
