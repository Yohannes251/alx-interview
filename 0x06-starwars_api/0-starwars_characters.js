#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function getName (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) reject(error);
      resolve(JSON.parse(body).name);
    });
  });
}

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const name = await getName(character);
      console.log(name);
    }
  }
});
