const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hi There, it is working!!! in port 5757');
});

app.listen(5757, () => {
  console.log('Listening on port 5757');
});

