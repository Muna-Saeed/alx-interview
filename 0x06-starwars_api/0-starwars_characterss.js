#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  function fetchCharacterName(url, callback) {
    request(url, (error, response, body) => {
      if (error) {
        callback(error);
        return;
      }
      if (response.statusCode !== 200) {
        callback(new Error(`Failed to fetch character at ${url}`));
        return;
      }
      const characterData = JSON.parse(body);
      callback(null, characterData.name);
    });
  }

  let completedRequests = 0;
  const characterNames = [];

  characterUrls.forEach((url, index) => {
    fetchCharacterName(url, (error, name) => {
      if (error) {
        console.error(error);
        return;
      }
      characterNames[index] = name;
      completedRequests++;

      if (completedRequests === characterUrls.length) {
        characterNames.forEach((name) => console.log(name));
      }
    });
  });
});
