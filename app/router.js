'use strict';

module.exports = app => {
  app.get('/', 'home.index');
  app.post('/calculate', 'home.calculate')
  app.get('/vba', 'vba.vba');
  app.post('/upload', 'vba.upload');
};
