#### RestApi Example with DenoJs
A simple todo project create

#### Denojs
Install using shell (Linux):
First step was to install the deno using (Install using shell (Linux))
`curl -fsSL https://deno.land/x/install/install.sh | sh`

To run deno using the deno shortcut; it is necessary to add two files to .zshrc or .bashrc.
```
export DENO_INSTALL="/home/<USER>/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"
```
Testing your installation
`deno --version`

##### Todo-deno project
```
|-- deno-todo-api
|   |-- controllers
|   |   |-- todo.ts
|   |-- data
|   |   |-- todos.ts
|   |-- interfaces
|   |   |-- Todo.ts
|   |-- routes
|   |   |-- todo.ts
|--server.ts
```

run the server with the following command 
`deno run --allow-net server.ts`
Open the browser and hit the URL localhost:8080
| API | Method | Description|
| ------------- | ------------- |------------- |
| http://localhost:8000/todos/ |	GET |	All todos |
| http://localhost:8000/todos/{id} | GET | todo by ID |
| http://localhost:8000/todos/ | POST | Create New todo |
| http://localhost:8000/todos/{id} | PUT | Update todo by ID |
| http://localhost:8000/todos/{id} | DELETE	| Delete todo by ID |
