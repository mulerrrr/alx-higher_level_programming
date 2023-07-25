#!/usr/bin/node
// Prints all characters of a Star Wars movie in order.
const request = require('request');
const movieId = '/' + parseInt(process.argv[2]) + '/';
const films = 'https://swapi-api.hbtn.io/api/films/';
const orderCharacters = [];
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
            } else if (character === (filmsList[film].characters.length - 1)) {
              const character = JSON.parse(body);
              orderCharacters.push([character.name, parseInt(character.url.match(/[0-9]+/g).join(''))]);
              const nameList = orderCharacters.sort((a, b) => {
                return a[1] - b[1];
              });
              for (let name = 0; name < nameList.length; name++) {
                console.log(nameList[name][0]);
              }
            } else {
              const character = JSON.parse(body);
              orderCharacters.push([character.name, parseInt(character.url.match(/[0-9]+/g).join(''))]);
            }
          });
        }
        break;
      }
    }
  }
});
