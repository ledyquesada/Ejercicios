//Acciones y reducers
// Acciones
export const addTask = createAction('[Task] Add Task', props<{ task: Task }>());
export const completeTask = createAction('[Task] Complete Task', props<{ taskId: string }>());

// Reducer
export const tasksReducer = createReducer(
  initialState,
  on(addTask, (state, { task }) => ({ ...state, tasks: [...state.tasks, task] })),
  on(completeTask, (state, { taskId }) => ({
    ...state,
    tasks: state.tasks.map(task => (task.id === taskId ? { ...task, completed: true } : task)),
  }))
);
