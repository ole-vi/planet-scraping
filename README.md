# planet-scraping

Script that scrapes the treehouses.io website, zips it and then uploads it to Planet.

## Password and username
The password and username is not supplied in the script for obvious privacy reasons. You need to set these up in environment variables before executing the planet script. I created a config.sh file that will automatically do this when planet.sh runs, all you need to do is fill in your planet login info in the provided environment variables. For example,
`export LOGIN_USERNAME='username'`
`export LOGIN_PASSWORD='password'
