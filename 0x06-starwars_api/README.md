# 0x06. Star Wars API

# Star Wars Characters

This project contains a Node.js script that prints all character names from a specified Star Wars movie using the Star Wars API.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the folder is mandatory
- Code should be semistandard compliant. Rules of Standard + semicolons on top. Reference: [AirBnB style](https://github.com/airbnb/javascript)
- All files must be executable
- The length of files will be tested using `wc`
- You are not allowed to use `var`

## Concepts Needed

- **HTTP Requests in JavaScript:**
  - Understanding how to make HTTP requests to external services using the request module or alternatives like fetch in Node.js.
  - [A Complete Guide to Making HTTP Requests in Node.js](https://www.section.io/engineering-education/http-requests-in-nodejs/)

- **Working with APIs:**
  - Understanding the basics of RESTful APIs and how to interact with them.
  - Parsing JSON data returned by APIs.
  - [Working with APIs in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction)

- **Asynchronous Programming:**
  - Managing asynchronous operations with callbacks, promises, and async/await syntax.
  - Handling API response data asynchronously.
  - [Asynchronous Programming in JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous)

- **Command Line Arguments in Node.js:**
  - Using the `process.argv` array to access command-line arguments passed to a Node.js script.
  - [How to Parse Command Line Arguments in Node.js](https://nodejs.dev/learn/nodejs-accept-arguments-from-the-command-line)

- **Array Manipulation and Iteration:**
  - Iterating over arrays and manipulating data structures to format and display character names.
  - [JavaScript Array Methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Additional Resources

- [Mock Technical Interview](https://www.pramp.com/#/) - Practice coding interviews with peers or industry professionals.

## Installation

1. Install Node.js:
   ```sh
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. Install `semistandard` globally:
   ```sh
   sudo npm install semistandard --global
   ```

3. Install `request` module globally:
   ```sh
   sudo npm install request --global
   ```

4. Set the `NODE_PATH` environment variable:
   ```sh
   export NODE_PATH=/usr/lib/node_modules
   ```

## Usage

1. Create a file named `0-starwars_characters.js` and add the following content:

   ```javascript
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
   ```

2. Make the script executable:
   ```sh
   chmod +x 0-starwars_characters.js
   ```

3. Run the script with a Movie ID:
   ```sh
   ./0-starwars_characters.js <Movie ID>
   ```

   Replace `<Movie ID>` with the ID of the Star Wars movie you want to retrieve characters from, for example:
   ```sh
   ./0-starwars_characters.js 3
   ```

## Code Style

This project follows the `semistandard` JavaScript style guide. You can check the code style by running:
```sh
semistandard
```

## Author

This project was created as part of the ALX Interview preparation series.

This `README.md` file now includes sections to provide a comprehensive guide for understanding, setting up, and running the project.
