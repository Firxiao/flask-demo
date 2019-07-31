from . import bar


@bar.route('/bar')
def get_index():
    return "This is bar!!!"



