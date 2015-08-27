module.exports = {
  entry: __dirname + '/photos/static/js/main.js',
  output: {
    filename: 'bundle.js',
    chunkFilename: '[hash].bundle.js',
    path: __dirname + '/photos/static/js/bundle'
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel'
      }
    ]
  }
};
