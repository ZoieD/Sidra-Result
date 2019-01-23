'use strict';

module.exports = appInfo => {
  const config = {};

  // should change to your own
  config.keys = appInfo.name + '_1497704659432_959';

  config.view = {
    defaultViewEngine: 'nunjucks',
    mapping: {
      '.tpl': 'nunjucks',
    },
  };

  config.middleware = [ 'errorHandler', 'apiWrapper' ];
  config.errorHandler = {
    // 非 `/api/` 路径不在这里做错误处理，留给默认的 onerror 插件统一处理
    match: '/rest',
  };
  // config.security = {
  //   // csrf: {
  //   //   queryName: '_csrf', // 通过 query 传递 CSRF token 的默认字段为 _csrf
  //   //   bodyName: '_csrf', // 通过 body 传递 CSRF token 的默认字段为 _csrf
  //   // },
  // };
  config.cors = {
    allowMethods: 'GET,HEAD,PUT,OPTIONS,POST,DELETE,PATCH',
  };

  config.multipart = {
    mode: 'file',
    fileExtensions: [".xls", ".xlsx"]
  };
  return config;
};