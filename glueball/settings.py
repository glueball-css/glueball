import os

DIRNAME = os.path.dirname(__file__)

# Modules each have a directory at this location
MODULE_ROOT = 'glueball.modules'

# This is where the .css files will be written to
CSS_ROOT = os.path.join(DIRNAME, os.pardir, 'css')

# List of slugs identifying the modules
MODULES = (
    'position',
    # 'coordinates',
    # 'z_index',
    # 'background_position',
    # 'background_repeat',
    # 'display',
    # 'font_weight',
    # 'float',
    # 'clear',
    # 'table',
    # 'flex_align_items',
    # 'flex_align_content',
    # 'flex_align_self',
    # 'flex_justify_content',
    # 'flex_direction',
    # 'flex_order',
    # 'flex_wrap',
    # 'box_sizing',
    # 'height',
    # 'max_width',
    # 'width',
    # 'margin',
    # 'padding',
    # 'list_style_type',
    # 'color',
    # 'background_color',
    # 'box_shadow',
    # 'overflow',
    # 'border_style',
    # 'border_width',
    # 'border_radius',
    # 'border_color',
    # 'line_height',
    # 'font_family',
    # 'font_size',
    # 'font_style',
    # 'letter_spacing',
    # 'transition',
)

# CSS files to include at the top of the generated CSS file
INCLUDES_DIR = os.path.join(DIRNAME, 'includes')
INCLUDES = (
    # 'normalize.css',
)
