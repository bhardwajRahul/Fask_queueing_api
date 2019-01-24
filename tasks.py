import os
from werkzeug.utils import secure_filename

def create_task(task_type):

    app_root = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(app_root, 'uplaods/')
    if not os.path.isdir(target):
        os.mkdir(target)

    for file in task_type:
        filename = secure_filename(file.filename)
        destination = "/".join([target, filename])
        file.save(destination)
    return True
