from inline_example import inline_example
from pathlib import Path
   
def fastapi():
    inline_example(
        example_path=Path(__file__).parent / 'examples/with_fastapi.py')
