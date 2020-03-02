var googlehome = require('google-home-notifier');
// var language = 'pl'; // if not set 'us' language will be used
// var language = 'us'; // if not set 'us' language will be used

var myArgs = process.argv.slice(2);
console.log('Sentence to read: ', myArgs);

googlehome.ip('192.168.0.115');

googlehome.notify(myArgs[0], function(res) {
  console.log(res);
});
