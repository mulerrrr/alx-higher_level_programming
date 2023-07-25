#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const movieId = '/' + parseInt(process.argv[2]) + '/';
const films = 'https://swapi-api.hbtn.io/api/films/';
request(films, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const filmsList = JSON.parse(body).results;
    for (let film = 0; film < filmsList.length; film++) {
      if (filmsList[film].url.includes(movieId)) {
        for (let character = 0; character < filmsList[film].characters.length; character++) {
          request(filmsList[film].characters[character], (error, response, body) => {
            if (error) {
              console.log(error);
            } else {
              const character = JSON.parse(body).name;
              console.log(character);
            }
          });
        }
        break;
      }
    }
  }
});
