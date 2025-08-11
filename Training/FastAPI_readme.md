
# FastAPI Syntax Explanation:
```bash

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

```

## Step 1: import FastAPI
FastAPI is a Python class that provides all the functionality for your API.

--->FastAPI is a class that inherits directly from Starlette.

--->You can use all the Starlette functionality with FastAPI too.

## Step 2: create a FastAPI "instance"
--->app variable will be an "instance" of the class FastAPI.

--->This will be the main point of interaction to create all your API
## Step 3: create a path operation
### Path
--->"Path" here refers to the last part of the URL starting from the first /.
A "path" is also commonly called an "endpoint" or a "route".

--->While building an API, the "path" is the main way to separate "concerns" and "resources".
### Operation
"Operation" here refers to one of the HTTP "methods".

One of:

```bash
   POST
   GET
   PUT
   DELETE

```

...and the more exotic ones:

```bash
   OPTIONS
   HEAD
   PATCH
   TRACE
```

When building APIs, you normally use these specific HTTP methods to perform a specific action.

## Normally use:

```bash
   POST: to create data.
   GET: to read data.
   PUT: to update data.
   DELETE: to delete data.

```

--->in OpenAPI, each of the HTTP methods is called an "operation".

--->We are going to call them "operations" too.

## Step 4: define the path operation function¶
This is our "path operation function":

path: is /.
operation: is get.
function: is the function below the "decorator" (below @app.get("/")).



# Path Parameters:

Parameter: A parameter is a variable used to pass information into a function, method, or procedure.

```bash
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

```
parameter: item_id

Path Prameter: A path parameter is a variable part of a URL path, used to identify specific resources.

# Pydantic
All the data validation is performed under the hood by Pydantic

## Predefined values
If you have a path operation that receives a path parameter, but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.

# query parameter

When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

