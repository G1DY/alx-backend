import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
  redisClient.quit();
});
redisClient.on(`connect`, () => console.log('Redis client connected to the server'));

console.log(redisClient.connect);

// two functions to setNewSchool and displaySchoolValue

function setNewSchool(schoolName, value,) {
  redisClient.set(schoolName, value, redisClient.print);
}

function displaySchoolValue(schoolName) {
  redisClient.get(schoolName, (_error, value) => {
    if (value) console.log(value);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
