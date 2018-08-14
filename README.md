# dnd2.0
a major update and overhaul of the previous project: dnd. Mostly rebuilt from the ground up

#### Virtual Environment

It is advised to use a virtual environment (or some alternative) to manage dependencies

##### Activate

Enter your virtual environment and install dependencies first

```
source /venv/bin/activate
```

##### Deactivate

Deactivate virtual environment when no more manipulation of the virtual environment is needed

```bash
deactivate
```

#### Installing

```bash
pip install -r requirements.txt
```

#### Updating

Takes the dependencies installed in the virtual environment and places them in a requirements document

```bash
pip freeze > requirements.txt
```

### Testing

#### Unit Tests

Testing runs all unit and integration test that are packaged under the `test/unit_tests` folder.

```bash
python -m pytest test
```
Append ```-vv``` to see testing output responses.