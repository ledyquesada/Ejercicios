//Selector de estado

// Selector
export const selectCompletedTasks = createSelector(
  selectTaskState,
  state => state.tasks.filter(task => task.completed)
);
