from task.app.main import run
from task.app.utils import get_model_name_from_input


model = get_model_name_from_input()

run(
    deployment_name=model.value,
    print_request=False,
    print_only_content=False,
)
