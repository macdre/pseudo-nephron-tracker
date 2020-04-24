var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    configureWebpack: {
        mode: 'development',
        plugins: [
            new HtmlWebpackPlugin({template: './src/js/index.html'})
        ],
        externals: {
            // global app config object
            config: JSON.stringify({
                apiUrl: 'http://localhost:4000'
            })
        }
    }
}