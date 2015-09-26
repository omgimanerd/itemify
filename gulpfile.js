/**
 * Javascript Task Runner
 * @author Alvin Lin (alvin.lin@stuypulse.com)
 */

var gulp = require('gulp');
var less = require('gulp-less');
var autoprefixer = require('gulp-autoprefixer');
var minifyCss = require('gulp-minify-css');
var notify = require('gulp-notify');

gulp.task('less', function() {
  console.log('Recompiling CSS');
  return gulp.src('./static/less/styles.less')
    .pipe(less({ compress: true }))
    .pipe(autoprefixer({ browsers: ['last 10 versions']}))
    .pipe(minifyCss())
    .pipe(gulp.dest('./static/css'))
    .pipe(notify('LESS compiled and minified'));
});

gulp.task('watch-less', function() {
  gulp.watch('./style/*.less', ['less']);
});
