'use strict';

module.exports = app => {
  app.get('/', 'vba.vba');
  app.post('/upload', 'vba.upload');
};
