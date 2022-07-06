import { v4 } from "https://deno.land/std/uuid/mod.ts";
// interface
import Todo from '../interfaces/todo.ts';

// First task "Hello world". Because this is first deno project example'
let todos: Todo[] = [
  {
    id: v4.generate(),
    task: 'Hello world',
    done: true,
  },
  {
    id: v4.generate(),
    task: 'Rest API with denoJs',
    done: false,
  },
  {
    id: v4.generate(),
    task: 'cv will be updated -> bayraktarulku.github.io',
    done: false,
  },
];

export default todos;