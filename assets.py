from flask_assets import Environment, Bundle

JavaScript = [
    'js/jquery-3.2.1.js',
    'js/ie10-viewport.js',
    'js/transition.js',
    'js/alert.js',
    'js/button.js',
    'js/carousel.js',
    'js/collapse.js',
    'js/dropdown.js',
    'js/modal.js',
    'js/tooltip.js',
    'js/popover.js',
    'js/scrollspy.js',
    'js/tab.js',
    'js/affix.js'
]

CSS = [
    'less/bootstrap.less',
    'less/theme.less',
    'less/ie10-viewport.less'
]


def Assets(app):
    assets = Environment(app)
    assets.config['UGLIFYJS_EXTRA_ARGS'] = ['--mangle', '--compress']
    assets.config['LESS_BIN'] = 'lessc --autoprefix=">5%"'
    js = Bundle(*JavaScript, filters='uglifyjs', output='gen/packed.js')
    assets.register('js_all', js)
    css = Bundle(*CSS, filters='less,cssmin', output='gen/packed.css')
    assets.register('css_all', css)
