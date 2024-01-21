//Efectos

// Efecto
@Injectable()
export class TaskEffects {
  loadTasks$ = createEffect(() => this.actions$.pipe(
    ofType(loadTasks),
    mergeMap(() => this.taskService.getTasks().pipe(
      map(tasks => loadTasksSuccess({ tasks })),
      catchError(() => of(loadTasksFailure()))
    ))
  ));

  constructor(private actions$: Actions, private taskService: TaskService) {}
}
