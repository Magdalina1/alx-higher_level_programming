#!/usr/bin/node
// A script that prints all characters of a Star Wars movie.

// Import the request module
const request = require('request');

// Get the movie ID from the first argument
const movieID = process.argv[2];

// Build the URL to request using the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

// Make a GET request to the URL
request.get(url, (err, response, body) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, parse the body as JSON
    const data = JSON.parse(body);
    // Get the characters array of the movie
    const characters = data.characters;
    // Define a recursive function to print the character names
    const printNames = (index) => {
      // If the index is out of bounds, stop the recursion
      if (index >= characters.length) {
        return;
      }
      // Get the character URL from the array
      const characterUrl = characters[index];
      // Make a GET request to the character URL
      request.get(characterUrl, (err, response, body) => {
        // If an error occurred, print the error object
        if (err) {
          console.error(err);
        } else {
          // Otherwise, parse the body as JSON
          const characterData = JSON.parse(body);
          // Print the name of the character
          console.log(characterData.name);
          // Call the function recursively with the next index
          printNames(index + 1);
        }
      });
    };
    // Call the function with the initial index of 0
    printNames(0);
  }
});
