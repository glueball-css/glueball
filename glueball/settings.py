import os

DOCSITE = "http://glueball.io/docs/"

DIRNAME = os.path.dirname(__file__)

# Modules each have a directory at this location
MODULE_ROOT = 'glueball.modules'

# This is where the .css files will be written to
CSS_ROOT = os.path.join(DIRNAME, os.pardir, 'css')

MODULE_DIR = os.path.join(DIRNAME, 'modules')

# List of slugs identifying the modules
# The CSS file and documentation site are built from the modules
# listed here.
# Comment out the modules that are not desired for your project.
MODULES = (
    'position',
    'coordinates',
    'z_index',
    'background_position',
    'background_repeat',
    'background_size',
    'display',
    'font_weight',
    'float',
    'clear',
    'table',
    'flex_direction',
    'justify_content',
    'flex_wrap',
    'order',
    'align_items',
    'align_self',
    'align_content',
    'flex_grow',
    'flex_shrink',
    'box_sizing',
    'height',
    'max_width',
    'max_height',
    'min_width',
    'min_height',
    'width',
    'margin',
    'padding',
    'list_style_type',
    'color',
    'background_color',
    'box_shadow',
    'overflow',
    'border_style',
    'border_width',
    'border_radius',
    'border_color',
    'text_transform',
    'white_space',
    'text_align',
    'vertical_align',
    'line_height',
    'font_family',
    'font_size',
    'font_style',
    'letter_spacing',
    'transition',
)

# CSS files to include at the top of the generated CSS file
INCLUDES_DIR = os.path.join(DIRNAME, 'includes')
INCLUDES = (
    'normalize.css',
)

PSEUDO_LOOKUP = {
    'hvr': 'hover',
    'fcs': 'focus',
    'lst': 'last-child',
    'fst': 'first-child',
    'odd': 'nth-child(odd)',
    'evn': 'nth-child(even)',
}
