var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');

// Pull in webpack for style template
module.exports = {
    configureWebpack: {
        mode: 'development',
        resolve: {
            extensions: ['.js', '.vue'],
            alias: {
                'vue$': 'vue/dist/vue.common.js'
            }
        },
        module: {
            rules: [
                {
                    test: /\.vue?$/,
                    exclude: /(node_modules)/,
                    use: 'vue-loader'
                },
                {
                    test: /\.js?$/,
                    exclude: /(node_modules)/,
                    use: 'babel-loader'
                }
            ]
        },
        plugins: [new HtmlWebpackPlugin({
            template: './src/js/index.html'
        })],
        devServer: {
            historyApiFallback: true
        },
        externals: {
            // global app config object
            config: JSON.stringify({
                apiUrl: 'http://localhost:4000'
            })
        }
    }
}