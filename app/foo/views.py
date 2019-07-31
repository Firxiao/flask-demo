from . import foo


@foo.route('/foo')
def get_index():
    return "This is foo!!!"



